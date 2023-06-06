import products
from products import Product
from typing import List


class Store():
    def __init__(self, products):
        self.product_list = products

    def add_product(self, product):
        self.product_list.append(product)
        return self.product_list

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity_list = []
        for product in self.product_list:
            total_quantity_list.append(product.get_quantity())
        return sum(total_quantity_list)

    def get_all_products(self) -> List:
        return self.product_list

    def order(self, shopping_list) -> float:
        total_price = 0
        for product,quant in shopping_list:
            total_price += product.price* quant
        print(shopping_list)
        return total_price


