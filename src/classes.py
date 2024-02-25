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

    @property
    def print_goods(self):
        """
        геттер, который выводит список товаров
        """
        result = ''
        for i in range(0, len(self.list_goods)):
            for j in range(0, len(self.list_goods[i])):
                result += (f'{self.list_goods[i][j]['name']}, {int(self.list_goods[i][j]['price'])} руб. '
                           f'Остаток: {self.list_goods[i][j]['quantity']} шт.\n')
        return result

    def __len__(self):
        """
        Определение количества продуктов на складе
        """
        return len(self.__goods)

    def __str__(self):
        return f'{self.name}, количество продуктов:'

    def __repr__(self):
        return (f"Category: ('{self.name}', {self.description}, '{self.__goods}', "
                f"'общее количество категорий={self.count_of_category} "
                f"количество уникальных продуктов={self.unique_goods}')")


class Product:
    """Класс продукт"""
    count_of_products = 0
    new_good = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.price = self.__price
        self.quantity = quantity

        Product.count_of_products += 1

    @classmethod
    def new_goods(cls, name: str, description: str, price: float, quantity: int):
        """
        создание товара
        """
        new_good = cls(name, description, price, quantity)
        return new_good

    @property
    def prices(self):
        return self.__price

    @prices.setter
    def prices(self, new_price):
        """
        Установка новой цены
        """
        if new_price == self.__price or new_price <= 0:
            print('Цена введена некорректная!')
        elif new_price < self.__price:
            choice = input('Введенная цена ниже установленой!\nСогласны понизить цену? (Y/N): ')
            if choice.upper() == 'Y':
                self.__price = new_price
        else:
            self.__price = new_price

    @prices.deleter
    def prices(self):
        self.__price = None
        # or del self.__price

    def __add__(self, other):
        """
        Сложение объектов между собой
        """
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __repr__(self):
        return (f"Product: ('{self.name}', '{self.description}', '{self.__price}', "
                f"'Количество продуктов в наличии={self.quantity}')")

# new_product = Product.new_goods("Sony", "мычит", 500.0, 1)
# print('Новый продукт:', new_product)
