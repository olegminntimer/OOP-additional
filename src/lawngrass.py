from src.product import Product


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        color: str,
        country: str,
        germination_period: int,
    ):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other) -> float:
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError