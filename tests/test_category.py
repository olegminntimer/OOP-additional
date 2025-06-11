import pytest

from src.category import Category, sum_of_cost_all_goods
from src.product import Product


def test_category_count(first_category: Category, second_category: Category) -> None:
    """Тест проверяет подсчет количества продуктов и подсчет количества категорий"""
    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_init(first_category: Category, second_category: Category) -> None:
    """Тест проверяет корректность инициализации объектов класса Category"""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения" " дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_in_list) == 3


def test_category_products_property(first_category: Category) -> None:
    """Тест проверяет геттер свойства products"""
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_products_setter(first_category: Category, product: Product) -> None:
    """Тест проверяет сеттер свойства products"""
    assert len(first_category.products_in_list) == 3
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 4


def test_category_str(first_category: Category) -> None:
    """Тест проверяет __str__"""
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_sum_of_cost_all_goods(products_: list) -> None:
    """Тест проверяет функцию подсчета стоимости всех товаров в категории"""
    assert sum_of_cost_all_goods(products_) == 3014000.0


def test_category_products_setter_error(first_category: Category, product: Product) -> None:
    """Тест проверяет сеттер свойства products"""
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_category_products_setter_smartphone(first_category, smartphone_1):
    first_category.add_product(smartphone_1)
    assert first_category.products_in_list[-1].name == "Xiaomi Redmi Note 11"


def test_middle_price(first_category):
    assert first_category.middle_price() == 9.0


def test_middle_price_zero(category_without_products):
    assert category_without_products.middle_price() == 0


def test_custom_exception(capsys, first_category):
    assert first_category.category_count == 12

    category_add = Product("Xiaomi 9", "16GB, Синий", 23000.0, 23, "Синий")
    first_category.add_product(category_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен."
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."

