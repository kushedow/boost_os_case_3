class Category:
    """Класс категории"""
    count_of_category = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_of_category += 1

    def __repr__(self):
        return f"Category: ('{self.name}', {self.description}, '{self.goods}', 'Количество категорий={self.count_of_category}')"


class Product:
    """Класс продукт"""
    count_of_products = 0

    def __init__(self, name: str, description: str, price: float, count_in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.count_in_stock = count_in_stock

        Product.count_of_products += 1

    def __repr__(self):
        return f"Product: ('{self.name}', {self.description}, '{self.price}', 'Количество продуктов={self.count_of_products}')"
