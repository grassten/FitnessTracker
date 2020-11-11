import json
from typing import List, Dict

import uuid


def create_food(**kwargs) -> None:
    unique_id = str(uuid.uuid4())
    food_item = kwargs
    food_item["id"] = unique_id
    with open('foods.txt', 'a') as f:
        f.write(f"{json.dumps(food_item)}\n")


def _get_foods():
    with open('foods.txt', 'r') as f:
        return f.readlines()


def search_food(query_string) -> List[Dict]:
    return [json.loads(line) for line in _get_foods() if query_string.lower() in str(line).lower()]


def get_food_nutrition_by_id(food_id) -> Dict:
    lines = _get_foods()
    for line in lines:
        line_dict = json.loads(line)
        if line_dict["id"] == food_id:
            return line_dict
