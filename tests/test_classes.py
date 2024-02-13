import pytest
from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    [{
                        'name': "Samsung Galaxy C23 Ultra",
                        'description': "256GB, Серый цвет, 200MP камера",
                        'price': 180000.0,
                        'quantity': 5
                    }])


def test_category_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert class_category.goods == [{
                        'name': "Samsung Galaxy C23 Ultra",
                        'description': "256GB, Серый цвет, 200MP камера",
                        'price': 180000.0,
                        'quantity': 5
                    }]
    assert class_category.count_of_category == 1


@pytest.fixture
def class_products():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера',
                   180000.0, 5)


def test_products_init(class_products):
    assert class_products.name == 'Samsung Galaxy C23 Ultra'
    assert class_products.description == '256GB, Серый цвет, 200MP камера'
    assert class_products.price == 180000.0
    assert class_products.count_in_stock == 5
    assert class_products.count_of_products == 1
