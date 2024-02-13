class Category:
    """Класс категории"""
    count_of_category = 0

    def __init__(self, name: str, description: str, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_of_category += 1


class Product:
    """Класс продукт"""
    count_of_products = 0

    def __init__(self, name: str, description: str, price: float, count_in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.count_in_stock = count_in_stock

        Product.count_of_products += 1
