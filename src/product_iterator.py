# from src.product import Product
# from src.category import Category
from collections.abc import Iterator
from typing import Any

from src.category import Category


class ProductIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории, например в цикле for"""

    def __init__(self, category_obj: Category) -> None:
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Iterator:
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# if __name__ == "__main__":
#     product1 = Product(
#         "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый"
#     )
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Gray space")
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Синий")
#
#     category1 = Category(
#         "Смартфоны",
#         """Смартфоны, как средство не только коммуникации, но и получения дополнительных
# функций для удобства жизни""",
#         [product1, product2, product3],
#     )
#
#     iterator = ProductIterator(category1)
#
#     for pr in iterator:
#         print(pr)
#
#     print()
#     for pr in iterator:
#         print(pr)
