import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list:
    categories = []
    for categ in data:
        products = []
        for prod in categ["products"]:
            products.append(Product(**prod))
        categ["products"] = products
        categories.append(Category(**categ))

    return categories
