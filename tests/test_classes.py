import pytest
from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Смартфоны', 'Смартфоны', 'fhfgh')
    # {
    #     "name": "Samsung Galaxy C23 Ultra",
    #     "description": "256GB, Серый цвет, 200MP камера",
    #     "price": 180000.0,
    #     "quantity": 5
    # })


def test_category_init(class_category):
    assert class_category.name == 'Смартфоны'
    assert class_category.description == 'Смартфоны'
    # assert class_category.goods == [{
    #                     "name": "Samsung Galaxy C23 Ultra",
    #                     "description": "256GB, Серый цвет, 200MP камера",
    #                     "price": 180000.0,
    #                     "quantity": 5
    #                 }]
