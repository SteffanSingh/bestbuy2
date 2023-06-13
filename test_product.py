import pytest

from test_function import creating_prod
from test_function import creating_prod_invalid_details
from products import Product
import products

def test_creating_prod():
    product = products.Product("MacBook Air M2", 1450, 100, True)
    assert product.show() ==  f"{product.name}, Price:{product.price}, Quantity:{product.quantity}"


def test_creating_prod_invalid_details():

    with pytest.raises(Exception):
        products.Product("MacBook Air M2", -1450, 100, True)
    with pytest.raises(Exception):
        products.Product(" ", 1450, 100, True)


def test_prod_become_inactive():
    product = products.Product("MacBook Air M2", 1450, 0, False)
    if product.quantity == 0:
        assert product.active == False


def test_buy_modifies_quantity():
    product = products.Product("MacBook Air M2", 1450, 100, True)
    assert product.buy(40) == 40*1450
    assert product.quantity == 60


def test_buy_too_much():
    product = products.Product("MacBook Air M2", 1450, 100, True)
    with pytest.raises(Exception):
        product.buy(200)







