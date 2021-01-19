"""
author:Xinye Chen
"""
from rental_shop import *
from Customer import *

shop = Rental_shop(10, 10, 10)
c1 = Customer('Alice')
c2 = Customer('Bob')
c3 = Customer('Cheer')
c1.inquire(shop)
c1.rent_car('hatchback', 9, shop)
c2.rent_car('sedan', 2, shop)
c3.rent_car('SUV',10,shop)
c1.customer_return_car('hatchback', 9, shop)