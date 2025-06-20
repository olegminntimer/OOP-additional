import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description="""Смартфоны, как средство не только коммуникации, но и получения дополнительных функций \
для удобства жизни""",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый"),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Gray space"),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Синий"),
        ],
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Телевизоры",
        description="""Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом \
и помощником""",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7, "")],
    )


@pytest.fixture
def product() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Gray space")


@pytest.fixture
def product1() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый")


@pytest.fixture
def product2() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Синий")


@pytest.fixture
def products_() -> list:
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "Серый"),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Gray space"),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "Синий"),
    ]


@pytest.fixture
def product_iterator(first_category: Category):
    return ProductIterator(first_category)


@pytest.fixture
def smartphone_1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 95, "Note 11", 1024, "Синий")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 96, "Note 11", 1024, "Gray space")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Трава", "Трава зеленая", 5000, 5, "Зеленый", "Россия", 7)


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Трава", "Трава светло-зеленая", 6000, 10, "Светло-зеленый", "Россия", 10)


@pytest.fixture
def category_without_products():
    return Category(
        name="Смартфоны",
        description="""Смартфоны, как средство не только коммуникации, но и получения дополнительных функций \
    для удобства жизни"""
    )