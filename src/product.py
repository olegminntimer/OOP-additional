from typing import Any, Optional


class Product:
    """Класс описывает продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, amount: float) -> Optional[float]:
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return None
        self.__price = amount
        return self.__price
