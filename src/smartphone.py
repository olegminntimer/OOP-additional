from src.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        color: str,
        efficiency: str,
        model: str,
        memory: int,
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
#     smrt = Smartphone("", )
#     print(smrt.efficiency)
#     print(smrt.model)
#     print(smrt.memory)