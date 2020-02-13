#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:07:03 2018

@author: gohar
"""


from Store_products import Store
from Store_products import ProductDetails
from Person_customer import Customer



def createCustomer():
    while True:
        age = input("Enter the customer's age: ")
        if age.isdigit():
            break
        else:
            if not age:
                print("Store exited.")
                return None
            print("\nInvalid age. Please enter a positive integer number.\n")
    while True:   
        money = input("Enter how much cash the customer has at the moment: ")
        if money.replace('.','').isdigit():
            break
        else:
             if not money:
                print("Store exited.")
                return None
             print("\nInvalid money format. Please enter a positive integer or float number.\n")
            
    return Customer("Anna", int(age), eval(money)) 



def main():
    store = Store()
    with open("products.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            details = line.split()
            if len(details) == 4 or len(details) == 5:
                try:
                    tup = (details[0], float(details[1]), details[2], float(details[3]), False if len(details) == 4 else (int(details[4]) == 1))
                    store.addProduct(tup[0], ProductDetails(
                            tup[0], tup[1], tup[2], tup[3], tup[4]))
                except ValueError as e:
                    print(e)
        
    print("\n\nStore details at the beginning of the transaction:\n\n{}".format(repr(store)))

    customer = createCustomer()
    if not customer:
        return
    
    distinct_items = set() # To store the entered distinct items. Not used in the project (set type example).
    while True:
        product = input("Enter the product name and the amount to buy and press enter when you are done to exit: ")
        if not product:
            break
        p = product.split()
        if len(p) != 2:
            print("\nInvalid input. Please follow the instructions for correct input.")
            continue
        if len(p) == 2 and not p[1].replace('.','').isdigit() or int(p[1]) <= 0:
            print("\nInvalid input. Please enter a valid amount to buy.")
            continue
                 
        try:
            name = p[0]
            distinct_items.add(name)
            amount = float(p[1])
            customer.addBasket(name, amount, store)
        except ValueError as e:
            print("\nInvalid input. ", e)
    
    print("\n\nDistinct item(s) amount in the basket is {}.".format(len(customer.getBasket())))
    customer.checkout(store)
    print("\n\nNow the customer has ${} in cash.".format(customer.money))
    print("\n\nUpdated store details at the end of the transaction:\n\n{}".format(store))
    
    store.saveToFile("updatedProducts.txt")

if __name__ == "__main__":
    main()