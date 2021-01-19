"""
author:Xinye Chen
"""
import rental_shop

class Customer:
    def __init__(self,name):
        self.name = name

    def inquire(self,type):
        type.display()

    def rent_car(self,car_type,days,type):
        type.rent(car_type,days)

    def customer_return_car(self,car_type,days,type):
        return type.return_car(car_type,days)

class vip_Curstomer(Customer):
    def __init__(self,name):
        self.name = name