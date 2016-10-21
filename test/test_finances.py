#!/usr/bin/env python
'''
Unit tests for Finances class

***Currently not implemented***
TO DO: need to find a way to read command line...

Usage: from root directory run: make test
'''

# --- Imports

# Standard libraries
import unittest as unittest
import yaml
import argparse
import pandas as pd
import numpy as np
from code.finances import Finances
from code.forecast import process_command_line


# -- Preparations

# Define command line arguments
args = process_command_line()

# Get inputs from yaml file
model_inputs = yaml.load(open(args.model_input).read())

# Initialize Finances
fin = Finances(model_inputs)

class TestFinances(unittest.TestCase):

    def test_aver_membership(self):
        fin.aver_membership()

        # Does the dataset have exactlty three columns?
        self.assertEqual(len(df.columns), 3)

    def test_year_refund_per_client(self):
        pass

    def test_refund_cumulative(self):
        pass

    def test_percentage_refund_cumulative(self):
        pass
