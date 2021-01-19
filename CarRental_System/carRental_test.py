#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
author:Xinye Chen
"""

import unittest
from rental_shop import *
from Customer import *


class CarRental_test(unittest.TestCase):

    def test1(self):
        shop = Rental_shop(10, 10, 10)
        c1 = Customer('Alice')
        res = c1.customer_return_car('hatchback', 9, shop)
        self.assertEqual(res,225)

if __name__ == '__main__':
    unittest.main()