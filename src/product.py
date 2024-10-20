from typing import Any, Optional


class Product:
    """Класс описывает продукт"""

    def __init__(self, name: str, description: str, price: float, quantity: int, product_sum: float=0):
        """Инициализация экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.poduct_sum = product_sum

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, amount: float) -> None:
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return None
        self.__price = amount


# if __name__ == "__main__":
#     product0 = Product("","",0,0)
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     for i in (product1, product3):
#         product0.sum_price = product0 + i
#
#     print(product0.sum_price)
#     print(product1)
