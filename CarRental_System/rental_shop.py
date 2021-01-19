#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
author:Xinye Chen
"""

class Rental_shop:
    hatchback_count = 10
    sedan_count = 10
    SUV_count = 10
    hatchback_shortPrice = 30
    sedan_shortPrice = 50
    SUV_shortPrice = 100
    hatchback_longPrice = 25
    sedan_longPrice = 40
    SUV_longPrice = 90


    def __init__(self, hatchback_count, sedan_count, SUV_count):
        self.hatchback_count = hatchback_count
        self.sedan_count = sedan_count
        self.SUV_count = SUV_count

    def display(self):
        print("The number of hatchback: %d" % Rental_shop.hatchback_count)
        print("The price for less than a week of hatchback: %d per day" % Rental_shop.hatchback_shortPrice)
        print("The price for a longer period of hatchback: %d per day" % Rental_shop.hatchback_longPrice)
        print("The number of sedan: %d" % Rental_shop.sedan_count)
        print("The price for less than a week of sedan: %d per day" % Rental_shop.sedan_shortPrice)
        print("The price for a longer period of sedan: %d per day" % Rental_shop.sedan_longPrice)
        print("The number of SUV: %d" % Rental_shop.SUV_count)
        print("The price for less than a week of SUV: %d per day" % Rental_shop.SUV_shortPrice)
        print("The price for a longer period of SUV: %d per day" % Rental_shop.SUV_longPrice)

    def rent(self, CarType, days):
        if CarType == "hatchback":
            if Rental_shop.hatchback_count == 0:
                print("There is no hatchback")
            else:
                Rental_shop.hatchback_count = Rental_shop.hatchback_count-1
                if days < 7:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service."%(CarType,days,30))
                else:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service."%(CarType, days, 25))

        if CarType == "sedan":
            if Rental_shop.sedan_count == 0:
                print("There is no sedan")
            else:
                Rental_shop.sedan_count = Rental_shop.sedan_count-1
                if days < 7:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service."%(CarType,days,50))
                else:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service."%(CarType, days, 40))

        if CarType == "SUV":
            if Rental_shop.SUV_count == 0:
                print("There is no SUV")
            else:
                Rental_shop.SUV_count = Rental_shop.SUV_count - 1
                if days < 7:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service." % (CarType, days, 100))
                else:
                    print("You have rented a %s car for %d days.You will be charged %d per day, We hope that you enjoy our service." % (CarType, days, 90))

    def return_car(self, CarType, days):
        if CarType == "hatchback":
            Rental_shop.hatchback_count = Rental_shop.hatchback_count + 1
            if days < 7:
                print("type:%s"%(CarType))
                print("period:%d"%(days))
                print("rate:%d"%(30))
                print("total payment:%d"%(days*30))
                res = days*30
            else:
                print("type:%s" % (CarType))
                print("period:%d" % (days))
                print("rate:%d" % (25))
                print("total payment:%d" % (days * 25))
                res = days * 25

        if CarType == "sedan":
            Rental_shop.sedan_count = Rental_shop.sedan_count + 1
            if days < 7:
                print("type:%s" % (CarType))
                print("period:%d" % (days))
                print("rate:%d" % (50))
                print("total payment:%d" % (days * 50))
                res = days * 50
            else:
                print("type:%s" % (CarType))
                print("period:%d" % (days))
                print("rate:%d" % (40))
                print("total payment:%d" % (days * 40))
                res = days * 40

        if CarType == "SUV":
            Rental_shop.SUV_count = Rental_shop.SUV_count + 1
            if days < 7:
                print("type:%s" % (CarType))
                print("period:%d" % (days))
                print("rate:%d" % (100))
                print("total payment:%d" % (days * 100))
                res = days * 100
            else:
                print("type:%s" % (CarType))
                print("period:%d" % (days))
                print("rate:%d" % (90))
                print("total payment:%d" % (days * 90))
                res = days * 90
        return res