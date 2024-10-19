from typing import Any, Optional


class Product:
    """Класс описывает продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int, sum_price: float=0):
        """Инициализация экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.sum_price = sum_price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if self.sum_price == 0:
            return self.price * self.quantity + other.price * other.quantity
        else:
            return self.sum_price + other.price * other.quantity

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

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    for i in (product1, product2, product3):
        a = product1 + product2
        print(product1 + product2 + product3)