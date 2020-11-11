import json
from typing import List, Dict

import uuid


def create_food(**kwargs) -> None:
    unique_id = str(uuid.uuid4())
    food_item = kwargs
    food_item["id"] = unique_id
    with open('foods.txt', 'a') as f:
        f.write(f"{json.dumps(food_item)}\n")


def search_food(query_string) -> List[Dict]:
    with open('foods.txt', 'r') as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines if query_string.lower() in str(line).lower()]


def get_food_nutrition_by_id(food_id) -> Dict:
    return search_food(food_id)[0]
