class Category:
    """
    Класс описывает категорию продукта
    """
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация экземпляра класса Category"""
        self.name = name
        self.description = description
        self.products =products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
