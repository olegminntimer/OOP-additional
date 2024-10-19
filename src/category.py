from typing import Optional

from src.product import Product


class Category:
    """
    Класс описывает категорию продукта
    """

    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        """Инициализация экземпляра класса Category"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        products_count = 0
        for product_ in self.__products:
            products_count += product_.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    @property
    def products(self) -> str:  #
        products_str = ""
        for product_ in self.__products:
            products_str += f"{str(product_)}\n"
        return products_str

    def add_product(self, product_: Product) -> None:
        self.__products.append(product_)
        Category.product_count += 1

    @property
    def products_in_list(self) -> list:
        return self.__products

    def sum_of_cost_all_goods(self):
        """Функция считает стоимость всех товаров в категории"""
        product_sum = Product("Стоимость всего", "Стоимость всех товаров в категории", 0, 0)
        for prod in self.__products:
            product_sum.sum_price = product_sum + prod
            # product_sum.quantity += prod.quantity
        return product_sum.sum_price

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации, но и получения дополнительных
функций для удобства жизни""",
        [product1, product2, product3],
    )
#     print(category1.name)
#     print(category1.description)
#     print(category1.products)
#     print(Category.product_count)
#
#     product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
    print(category1.products)
    print(Category.product_count)
    print(category1)

    print(category1.sum_of_cost_all_goods())

