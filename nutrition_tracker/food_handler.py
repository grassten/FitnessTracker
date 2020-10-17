import json
from typing import List

import uuid

from nutrition_tracker.food_item import FoodItem


def create_food(**kwargs) -> None:
    unique_id = str(uuid.uuid4())
    food_item = FoodItem(id=unique_id, **kwargs)
    with open('foods.txt', 'a') as f:
        f.write(f"{json.dumps(food_item.__dict__)}\n")


def search_food(query_string) -> List[FoodItem]:
    with open('foods.txt', 'r') as f:
        lines = f.readlines()
    return [FoodItem(**json.loads(line)) for line in lines if query_string.lower() in str(line).lower()]


def get_food_nutrition_by_id(food_id) -> FoodItem:
    return search_food(food_id)[0]
