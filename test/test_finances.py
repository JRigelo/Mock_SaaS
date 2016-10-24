#!/usr/bin/env python
'''
Unit tests for Finances class

Usage: from root directory run: make test
'''

# --- Imports

# Standard libraries
import unittest as unittest
import pandas as pd
import numpy as np
from SaaSModel.finances import Finances
from SaaSModel.forecast import process_command_line


# -- Preparations

# Define mock command line arguments
model_inputs = {'monthly': True, 'filepath': 'data/membership.csv'}
# Initialize Finances
fin = Finances(model_inputs)

class TestFinances(unittest.TestCase):

    def test_aver_membership(self):
        fin.aver_membership()

        # Does the dataset have exactlty three columns?
        self.assertEqual(len(fin.df.columns), 3)

    def test_year_refund_per_client(self):
        pass

    def test_refund_cumulative(self):
        pass

    def test_percentage_refund_cumulative(self):
        pass
