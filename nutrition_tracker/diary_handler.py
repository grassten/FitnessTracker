import json
from datetime import datetime
import uuid

from nutrition_tracker.constants import DATE_FORMAT
from nutrition_tracker.food_handler import get_food_nutrition_by_id


def add_food_to_diary(food_id, date=None):
    food_item = get_food_nutrition_by_id(food_id)
    diary_item = {
        "id": str(uuid.uuid4()),
        "date": date or datetime.utcnow().strftime(DATE_FORMAT),
        "food_item": food_item
    }
    with open("database.txt", "a+") as f:
        f.write(json.dumps(diary_item) + '\n')


def delete_record_from_diary(record_id):
    with open("database.txt", "r") as f:
        lines = f.readlines()
    with open("database.txt", "w") as f:
        for line in lines:
            row_dict = json.loads(line)
            if row_dict["id"] == record_id:
                continue
            f.write(line)


def get_entries_by_date(date_object):
    with open("database.txt", "r") as f:
        lines = f.readlines()
    results = []
    for line in lines:
        row_dict = json.loads(line)
        timestamp = datetime.strptime(row_dict["date"], DATE_FORMAT)
        if timestamp.date() == date_object.date():
            results.append(row_dict)
    return results
