import json
import os
from src.classes import Category, Product


def load_data(file_name):
    """
    Подгрузка данных по категориям и товарам из файла JSON
    """
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(ROOT_DIR, "src", file_name)
    with open(PATH, encoding='UTF-8') as file:
        data = json.loads(file.read())
    return data


def get_category_and_product(data):
    categories = []
    products = []
    i = 0
    for category in data:
        categories.append(Category(category["name"], category["description"], category["products"]))
        for el in category["products"]:
            products.append(Product(el["name"], el["description"], el["price"], el["quantity"]))
            Category.unique_goods += 1
        categories[i].add_list_goods()
        i += 1
    categories[0].print_goods()
    products[0].new_goods({
            "name": "Samsung Galaxy C23 Ultra",
            "description": "мычит",
            "price": 1000.0,
            "quantity": 1
        }, products)
    return categories, products
