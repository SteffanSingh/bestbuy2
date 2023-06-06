import re
from typing import Dict, List


class Product:
    def __init__(self, name: str, price: float, quantity: int, active: bool = True):

        """constructor to initialize the all instance variables : """
        pattern = r'[^\w\s]'
        match = re.search(pattern, name)
        if name == " ":
            raise Exception("The name cant be empty")
        if match:
            raise TypeError(" The name contains alphanumeric characters or symbols :")
        if price < 0:
            raise Exception("The price cant be negative!")
        if quantity < 0:
            raise Exception("The quantity can not be negative! ")
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = active
        except Exception as error:
            print(error)

    def __repr__(self) -> str:
        return "{"+ self.name + ", Price=$" + str(self.price)+", Quantity="+str(self.quantity)+"}"

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
        if new_quantity == 0:
            self.active = False
        return self.quantity

    def is_active(self) -> bool:
        if self.active:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        # self.product = {}
        # self.product[self.name]["Price"] = self.price
        # "self.product[self.name]["Quantity"] = self.quantity
        product = f"{self.name}, Price:{self.price}, Quantity:{self.quantity}"
        return product

    def buy(self, buy_quantity) -> float:
        if buy_quantity < 0:
            raise Exception("The quantity cant be less than 0")
        self.total_price = buy_quantity * self.price
        self.quantity -= buy_quantity
        return self.total_price
