#!/usr/bin/env python
'''
Unit tests for class Client

Usage: from root directory run: make test
'''

# --- Imports

# Standard libraries
import unittest as unittest
import pandas as pd
import numpy as np
from code.client import Client

# -- Preparations

# Initialize class Client
aver_memb_durantion = 4
monthly = True
cl = Client(aver_memb_durantion, monthly)

class TestClient(unittest.TestCase):

    def test_get_parameters(self):
        """
        Test for parameters on cost calculation
        """
        cost = np.random.uniform(low=0.0, high=1200, size=None)
        unit_value, lifetime_aver, x = cl.get_parameters(cost)
        result = len(x)*unit_value
        self.assertEqual(round(result, 4), round(cost, 4))

        # For daily based case
        cl.monthly = False
        unit_value, lifetime_aver, x = cl.get_parameters(cost)
        result = len(x)*unit_value
        self.assertEqual(round(result, 4), round(cost, 4))

    def test_cum_exponential(self):
        """
        Test for exponetial cumulative distribution function.
        Cumulative distribution is zero for x -> -inf, and 1 for x -> inf
        """
        x1 = 0
        x2 = 10000
        theta = 10

        zero = cl.cum_exponential(x1, theta)
        self.assertEqual(zero, 0) # cum distribution is zero

        one = cl.cum_exponential(x2, theta)
        self.assertEqual(one, 1)  # cum distribution is one

    def test_expected_cum_refund(self):
        """
        Test for expected refund method.
        Expected refund increases with time
        """
        # Mock cost
        cost = np.random.uniform(low=1.0, high=1200, size=None)

        # Assuming monthly time unit
        unit_value = cost/12.0
        values = np.arange(cost,  0, -unit_value, dtype=np.float)
        refunds = {t: cl.expected_cum_refund(cost, t)/values[t]
                   for t in range(12)}

        # Checking key order by value
        check_order = sorted(refunds, key=lambda x : refunds[x])
        self.assertEqual(check_order, range(12))



if __name__ == '__main__':
    unittest.main()
