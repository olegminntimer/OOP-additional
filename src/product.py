class Product:
    """Класс описывает продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация экземпляра класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description,  price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return None
        self.__price = amount
        return self.__price



# if __name__ == "__main__":
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     # print(product1.name)
#     # print(product1.description)
#     # print(product1.price)
#     # print(product1.quantity)
#     #
#     product2 = Product.new_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     #
#     # print(product2.name)
#     # print(product2.description)
#     # print(product2.price)
#     # print(product2.quantity)
#     print(product1.price)
#     product2.price = 40000
#     print(product2.price)
#     product2.price = -40000
#     print(product2.price)

