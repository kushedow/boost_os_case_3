class Category:
    """Класс категории"""
    count_of_category = 0
    unique_goods = 0
    list_goods = []

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.count_of_category += 1

    def add_list_goods(self):
        """
        добавление товаров в категорию
        """
        return self.list_goods.append(self.__goods)

    def print_goods(self):
        """
        геттер, который выводит список товаров
        """
        for i in range(0, len(self.list_goods)):
            for j in range(0, len(self.list_goods[i])):
                print(
                    f'{self.list_goods[i][j]['name']}, {int(self.list_goods[i][j]['price'])} руб. Остаток: {self.list_goods[i][j]['quantity']} шт.')

    def __repr__(self):
        return f"Category: ('{self.name}', {self.description}, '{self.__goods}', 'общее количество категорий={self.count_of_category} количество уникальных продуктов={self.unique_goods}')"


class Product:
    """Класс продукт"""
    count_of_products = 0
    new_good = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.count_of_products += 1

    @classmethod
    def new_goods(cls, goods):
        """
        создание товара
        """
        cls.new_good = goods

    def __repr__(self):
        return f"Product: ('{self.name}', {self.description}, '{self.price}', 'Количество продуктов в наличии={self.quantity}')"
