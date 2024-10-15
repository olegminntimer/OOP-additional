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
        self.price = price
        self.quantity = quantity
