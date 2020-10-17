from datetime import datetime

from nutrition_tracker import food_handler, diary_handler
from nutrition_tracker.constants import DATE_FORMAT


def _view_diary_for_date(date_to_pull):
    entries = diary_handler.get_entries_by_date(date_to_pull)
    [print(entry) for entry in entries]


def view_diary_for_today():
    _view_diary_for_date(datetime.today())


def view_diary_for_another_day():
    diary_date = input(f"Enter date in format {DATE_FORMAT}.")
    _view_diary_for_date(datetime.strptime(diary_date, DATE_FORMAT))


def search_for_food():
    search_term = input("Enter search term.")
    [print(i) for i in food_handler.search_food(search_term)]


def _add_food_to_date(food_id, date_to_pull):
    diary_handler.add_food_to_diary(food_id, date_to_pull)


def add_food_to_today():
    food_id = input("Enter food unique ID.")
    _add_food_to_date(food_id, None)


def delete_from_diary():
    record = input("Enter unique ID of record you want to delete.")
    diary_handler.delete_record_from_diary(record)


def add_food_to_another_day():
    food_id = input("Enter food unique ID.")
    diary_date = input(f"Enter date in format {DATE_FORMAT}.")
    diary_date_formatted = datetime.strptime(diary_date, DATE_FORMAT)
    _add_food_to_date(food_id, diary_date_formatted.strftime(DATE_FORMAT))


def create_new_food():
    description = input("Description: ")
    brand = input("Brand: ")
    serving_size = input("Serving size: ")
    serving_unit = input("Serving unit: ")
    calories = input("Calories: ")
    total_fat = input("Total fat: ")
    total_carbs = input("Total carbs: ")
    protein = input("Protein: ")
    food_handler.create_food(
        description=description,
        serving_size=serving_size,
        serving_unit=serving_unit,
        calories=calories,
        total_fat=total_fat,
        total_carbs=total_carbs,
        protein=protein,
        brand=brand
    )


def print_options():
    print("1. View diary for today.")
    print("2. View diary for another day.")
    print("3. Search for food.")
    print("4. Add food to today's diary.")
    print("5. Add food to another day's diary.")
    print("6. Delete from diary.")
    print("7. Create food.")


def main():
    print_options()
    while True:
        selection = input("What would you like to do?")
        if str(selection) == "0":
            print_options()
        elif str(selection) == "1":
            view_diary_for_today()
        elif str(selection) == "2":
            view_diary_for_another_day()
        elif str(selection) == "3":
            search_for_food()
        elif str(selection) == "4":
            add_food_to_today()
        elif str(selection) == "5":
            add_food_to_another_day()
        elif str(selection) == "6":
            delete_from_diary()
        elif str(selection) == "7":
            create_new_food()
        else:
            exit()


if __name__ == "__main__":
    main()
