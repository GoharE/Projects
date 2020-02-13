#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:05:58 2018

@author: gohar
"""
from exceptionClass import ShoppingError

class Person:
    def __init__(self, personName, age):
        self.personName = personName
        self.age = age
            

class Customer(Person):
    def __init__(self, personName, age, money):
        super().__init__(personName, age)
        self.money = money
        self.__basket = dict()
        
    def addBasket(self, product, amount, store):
        new_amount = self.__basket.get(product, 0) + amount
        if store.checkAvailability(product, new_amount):
            self.__basket[product] = new_amount
        else:
            print("\nNo {} available!".format(product))
    
    def getBasket(self):
        return self.__basket
    
    def checkout(self, store):
        for (p, v) in self.__basket.items():
            try:
                price = store.priceCheck(p)
                amount = price * v
                if amount < self.money:
                    store.sell(p, v, self)
                    self.money -= amount
                else:
                    print("\nNo enough money to buy {}!".format(p))
            except ShoppingError as e:
                print("\n\n\n{}".format(e))

