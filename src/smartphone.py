from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other) -> float:
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


# if __name__ == "__main__":
#     smrt = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
#                       "Синий", "Good", "Note 11", 1024)
#     print(smrt.efficiency)
#     print(smrt.model)
#     print(smrt.memory)
