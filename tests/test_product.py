def test_product_init(product):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8
