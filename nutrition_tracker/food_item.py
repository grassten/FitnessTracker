from dataclasses import dataclass


@dataclass
class FoodItem:
    id: str
    description: str
    serving_unit: str  # TODO: make this an enum
    serving_size: float
    calories: float
    total_fat: int
    total_carbs: int
    protein: int
    saturated_fat: int = None
    trans_fat: int = None
    dietary_fiber: int = None
    sugar: int = None
    barcode: int = None
    brand: str = None
