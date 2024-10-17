from unicodedata import category

from src.product import Product


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
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):#
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @products.setter
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products


# if __name__ == "__main__":
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         """Смартфоны, как средство не только коммуникации, но и получения дополнительных
# функций для удобства жизни""",
#         [product1, product2, product3],
#     )
#     print(category1.name)
#     print(category1.description)
#     print(category1.products)
#     print(Category.product_count)
#
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(Category.product_count)

