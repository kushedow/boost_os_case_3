import pytest
from src.classes import Category, Product


@pytest.fixture
def class_category():
    return Category('Планшеты', 'Lenovo', ['aaa', 'bbb'])


def test_category_init(class_category):
    assert class_category.name == 'Планшеты'


