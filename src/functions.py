import json, os
from classes import Category, Product


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
    for category in data:
        categories.append(Category(category["name"], category["description"], category["products"]))
        for el in category["products"]:
            # print('el-', el["price"])
            products.append(Product(el["name"], el["description"], el["price"], el["quantity"]))
            print('all prod', products)
        print('all cat', categories)
    return categories


def get_product(data):
    products = []
    print('DATA ', data)
    for product in data:
        print('****', product)
        products.append(Product(product["products"]["name"], product["products"]["description"], product["products"]["price"]))
        print('123=', products)
    return products
