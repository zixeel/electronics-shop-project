import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, pay_rate: float = 1) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_string):
        name = data_string[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_name):
        cls.all = []
        with open(file_name) as f:
            items = csv.DictReader(f)
            for item in items:
                name = item['name']
                price = float(item['price'])
                quantity = int(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num):
        return int(float(num))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name
