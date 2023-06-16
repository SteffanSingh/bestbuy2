from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, promotion_name):
        self.name = promotion_name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, promotion_name, percent):
        super().__init__(promotion_name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:

        price1 = product.price - product.price * self.percent / 100
        return price1 * quantity


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity) -> float:
        free_items= quantity//3
        full_price_quantity = quantity-free_items
        total_price = product.price*full_price_quantity
        return total_price



        #price1 = product.price * 2
        #quantity = 3


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity) -> float:


        if quantity == 1:
            total_price1 = product.price * quantity
            return total_price1
        elif quantity%2 == 0:
            total_price1 = product.price*quantity*3/4
            return total_price1
        elif quantity %2 !=0:

            total_price1 = product.price*(quantity-1)*3/4 + product.price*1
            return total_price1
