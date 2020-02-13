#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:47:51 2018

@author: gohar
"""

from Store_products import Store, ProductDetails
from Person_customer import Customer
from exceptionClass import ShoppingError



def test():
    store = Store()
    assert store.getCash() == 0, "Store has cash."
    assert store.getDistProductCt() == 0, "Store has products."
    store.addProduct("bread", ProductDetails("bread", 1, "ct", 1))
    store.addProduct("beer", ProductDetails("beer", 2, "ct", 10, True))
    store.addProduct("sugar", ProductDetails("sugar", 1.5, "lb", 5))
    
    assert store.getProductCount("beer") == 10
    
    assert store.getDistProductCt() == 3, "Store has {}.".format(store.getDistProductCt())
    
    assert store.priceCheck("bread") == 1, "Bread price is {}.".format(store.priceCheck("bread"))
    assert store.checkAvailability("bread", 1), "Bread is not available."
    assert store.checkAvailability("bread", 25) == False, "25 Breads should be unavailable."
    assert store.checkAvailability("wine", 1) == False, "Wine should be unavailable."
    
    customer = Customer("Dave", 20, 100)
    assert customer.personName == "Dave", ""
    assert customer.age == 20, ""
    assert customer.money == 100, ""
    
    customer.addBasket("bread", 1, store)
    customer.addBasket("sugar", 2, store)
    customer.addBasket("beer", 5, store)
    customer.addBasket("juice", 2, store)
    assert len(customer.getBasket()) == 3
    
    customer.checkout(store)
    
    assert store.getCash() == 4, "Store cash {}.".format(store.getCash())
    assert store.getDistProductCt() == 2, "Store has products."
    
    assert customer.money == 96, "Wrong calculation."
    
    details = ProductDetails("bread", 1, "ct", 1)
    assert details.getName() == "bread"
    assert details.getPrice() == 1
    assert details.getMeasure() == "ct"
    assert details.getCount() == 1
    assert details.getAgeRestriction() == False
    
    assert not details.getAgeRestriction(), "Restricted age."
    
    try:
        store.sell("juice", 5, customer)
        assert False
    except ShoppingError as e:
        assert str(e) == "No juice."
        
    try:
        store.sell("beer", 5, customer)
        assert False
    except ShoppingError as e:
        assert str(e) == "ATTENTION! Customer is not allowed to buy beer; age restriction."
    
    
test()