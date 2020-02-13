#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:04:10 2018

@author: gohar
"""

from exceptionClass import ShoppingError


class ProductDetails:
    def __init__(self, name, price, measure, count, ageRestriction = False):
        self.__name = name
        self.__price = price
        self.__measure = measure
        self.__count = count
        self.__ageRestriction = ageRestriction
        
    def getAgeRestriction(self):
        return self.__ageRestriction
        
    def getName(self):
        return self.__name
        
    def getPrice(self):
        return self.__price
    
    def getCount(self):
        return self.__count
    
    def getMeasure(self):
        return self.__measure
    
    def setPrice(self, price):
        self.__price = price
    
    def setCount(self, count):
        self.__count = count
    
    def setMeasure(self, measure):
        self.__measure = measure
        
    def setName(self, name):
        self.__name = name
    
    def setAgeRestriction(self, ageRestriction):
        self.__ageRestriction = ageRestriction
        
    def __str__(self):
        return self.__name + " " + "$" + str(self.__price) + " " + self.__measure + " " + str(self.__count)
        

class Store:
    def __init__(self):
        self.__products = dict()
        self.__cash = 0
        
    def getCash(self):
        return self.__cash

    def getDistProductCt(self):
        return len(self.__products)
    
    def getProductCount(self, name):
        if not name in self.__products:
            return 0
        else:
            return self.__products[name].getCount()
        
    def addProduct(self, product, volume):
        self.__products[product] = volume
        
    def saveToFile(self, filename):
        with open(filename, "w") as f:
            for (k, v) in self.__products.items():
                f.write("{} {} {} {} {}\n".format(
                        v.getName(), v.getPrice(), v.getMeasure(),
                        v.getCount(), int(v.getAgeRestriction())))

    def __str__(self):
        st = str(self.__cash) + " in cash\n"
        for (k, v) in self.__products.items():
            st += str(v) + "\n"
        return st
    
    def checkAvailability(self, name, count):
        if not name in self.__products:
            return False
        else:
            volume = self.__products[name]
            return count <= volume.getCount()
    
    def priceCheck(self, name):
        if not name in self.__products:
            return -1
        else:
            volume = self.__products[name]
            return volume.getPrice()
    
    def __repr__(self):
        return self.__str__()
    
    def sell(self, name, count, customer):
        if not name in self.__products:
            raise ShoppingError("No {}.".format(name))
        else:
            details = self.__products[name]
            if details.getAgeRestriction() and customer.age < 21:
                raise ShoppingError("ATTENTION! Customer is not allowed to buy {}; age restriction.".format(name))
            if details.getCount() < count:
                ShoppingError("\nNo enough {}!".format(name))
            self.__upadteStoreDetails(name, details, count)
            print("\n\nSold {} {} {} with {} dollar(s) each, total {} dollar(s). \n".format(count,
                  details.getMeasure(), name, details.getPrice(), count * details.getPrice()))
            
    def __upadteStoreDetails(self, name, details, count):
        self.__cash += count * details.getPrice()
        details.setCount(details.getCount() - count)
        if details.getCount() == 0:
            del self.__products[name]