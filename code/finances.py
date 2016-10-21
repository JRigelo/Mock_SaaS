#!/usr/bin/env python
"""
Class Finances: Computes expected prorated refunds in various forms
for yearly, monthly or daily forecast.
----------------------------------------------------------------------------

Usage
-----
The following line uses/access this class and its methods:

    $ ipython forecast.py ../input/model_input.yml ../output/mode_output.txt

----------------------------------------------------------------------------
"""

# --- Imports

# Standard libraries
import numpy as np
import pandas as pd

# Application classes
from client import Client


class Finances(object):
    """
    The Finances class provides few methods for forecasting prorated refunds
    """
    def __init__(self, model_inputs):
        # True if time scale is month
        self.monthly = model_inputs['monthly']
        # Company's data
        self.df = pd.read_csv(model_inputs['filepath'])
        # Total subscription reserve
        self.sum_values = np.sum(self.df.ix[:, 2])

        # Initialize Class Client
        self.client = Client(self.aver_membership(), self.monthly)

    def aver_membership(self):
        """
        Computes the average time of the subscriptions.

        Arguments
        ---------
        None

        Return values
        -------------
        Numpy float
        """
        # Make a copy of dataset
        df = self.df.copy()
        # Calculate the duration of each subscription
        lifetime = pd.to_datetime(df.ix[:, 1]) - pd.to_datetime(df.ix[:, 0])

        # Average time (in days) of the subscriptions
        return np.mean(lifetime.astype('timedelta64[D]'))

    def value_dict(self):
        """
        Creates a dictionary with the each subscription value

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        return dict(zip(xrange(self.df.ix[:, 2].size), self.df.ix[:, 2]))

    def year_refund_per_client(self):
        """
        Computes the expected refund in a year for each client

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        # Get dictionary with subscription values
        values = self.value_dict()

        if self.monthly:
            for key, value in values.iteritems():
                values[key] = self.client.expected_cum_refund(value, 12)
        else:
            for key, value in values.iteritems():
                values[key] = self.client.expected_cum_refund(value, 365)

        # Expected refunds for each client
        return values

    def refund_cumulative(self):
        """
        Computes the monthly or daily expected cash reserve amounts through the
        year

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        if self.monthly:
            return {t: self.client.expected_cum_refund(self.sum_values, t)
                    for t in range(1, 13)}
        else:
            return {t: self.client.expected_cum_refund(self.sum_values, t)
                    for t in range(1, 366)}

    def percentage_refund_cumulative(self):
        """
        Computes the monthly or daily expected percentage cash reserve amounts
        through the year

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        return {key: round(refund*100/self.sum_values)
                for key, refund in self.refund_cumulative().iteritems()}

    def refund(self):
        """
        Computes the monthly or daily expected cash reserve amounts for each
        month or day t

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        if self.monthly:
            return {t: self.client.expected_refund(self.sum_values, t)
                    for t in range(1, 13)}
        else:
            return {t: self.client.expected_refund(self.sum_values, t)
                    for t in range(1, 366)}

    def percentage_refund(self):
        """
        Computes the monthly or daily expected percentage cash reserve amounts
        through the year

        Arguments
        ---------
        None

        Return values
        -------------
        Dictinary
        """
        return {key: round(refund*100/self.sum_values)
                for key, refund in self.refund().iteritems()}

if __name__ == '__main__':
    pass
