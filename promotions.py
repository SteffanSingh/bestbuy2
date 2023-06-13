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
        price1 = product.price * 2
        quantity = 3
        return price1 * quantity


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity) -> float:
        price1 = product.price + product.price / 2
        quantity = 2
        return price1 * quantity
