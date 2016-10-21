#!/usr/bin/env python
"""
Class Client: Contains support functions used by class Finances to compute
expected prorated refunds in various forms for yearly, monthly or daily
forecast.
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


class Client(object):
    """
    The Client class provides few functions to compute refunds for each client
    """
    def __init__(self, aver_mem, monthly):
        # Average time of a subscription
        self.aver_membership = aver_mem
        # True is time scale is month
        self.monthly = monthly

    def get_parameters(self, cost):
        """
        Provides
                  1) unit value: "total subscription cost"
                                   -----------------------
                                      "total time units"

                  2) lifetime average of the subscriptions conditioned to
                     the time scale

                  3) array with the time units.

        Arguments
        ---------
        Numpy float

        Return values
        -------------
        Numpy float, Numpy float, Numpy array
        """
        # If monthly case
        if self.monthly:
            unit_value = cost/12.0
            lifetime_aver = self.aver_membership/30.0
            x = np.arange(1, 13, 1, dtype=float)

        else:
            unit_value = cost/365.0
            lifetime_aver = self.aver_membership
            x = np.arange(1, 366, 1, dtype=float)

        return unit_value, lifetime_aver, x

    def cum_exponential(self, x, theta):
        """
        Computes the cumulative exponential distribution depending on the
        average time of the subscriptions, theta.

        Arguments
        ---------
        Numpy array, Numpy float

        Return values
        -------------
        Numpy array
        """
        return 1 - np.exp(-x/theta)

    def exponential(self, x, theta):
        """
        Computes the exponential distribution depending on the
        average time of the subscriptions, theta.

        Arguments
        ---------
        Numpy array, Numpy float

        Return values
        -------------
        Numpy array
        """
        return 1.0/theta*np.exp(-x/theta)

    def expected_cum_refund(self, cost, time):
        """
        Computes the expected value of a subscription refund up to a certain
        time in the year

        Example:
              The average lifetime of memberships costing 1200 is exponentially
              distributed with mean of 9 months. Thus it has the following
              expected refund (for monthly time scale)

              E(Y) = 1200P(X<=1) + 1100P(1<X<=2) + 1000P(2<X<=3) + ...
                   = 1200(1 - exp(-1/9)) + 1100((1 - exp(-2/9)) -
                     (1 - exp(-1/9))) + ...

        Arguments
        ---------
        Numpy float, Int

        Return values
        -------------
        Numpy float
        """
        # Get the parameters needed
        unit_value, lifetime_aver, x = self.get_parameters(cost)

        # Array of subscription value in decreasing order
        values = np.arange(cost,  0, -unit_value, dtype=np.float)

        # First month or day
        if time == 1:

            return cost*self.cum_exponential(1.0, lifetime_aver)

        else:
            x = x[:time]
            values = values[:time]
            pos_values = values*self.cum_exponential(x, lifetime_aver)
            x_neg = x[:-1]
            neg_values = values[1:]
            neg_values = neg_values*self.cum_exponential(x_neg, lifetime_aver)

            # Expected value
            return np.sum(pos_values) - np.sum(neg_values)

    def expected_refund(self, cost, time):
        """
        Computes the expected value of a subscription refund for a month
        or day t

        Example:
              The average lifetime of memberships costing 1200 is exponentially
              distributed with mean of 9 months. Thus it has the following
              expected refund for month 2

              E(Y) = 1100P(1<X<=2)
                   = 1100((1 - exp(-2/9))

        Arguments
        ---------
        Numpy float, Int

        Return values
        -------------
        Numpy float
        """
        # Get the parameters needed
        unit_value, lifetime_aver, x = self.get_parameters(cost)

        # Array of subscription value in decreasing order
        values = np.arange(cost,  0, -unit_value, dtype=np.float)

        # First month or day
        if time == 1:

            return cost*self.exponential(1.0, lifetime_aver)

        else:
            x = x[time - 1:time]
            values = values[time - 1:time]
            pos_values = values*self.exponential(x, lifetime_aver)
            x_neg = x[:-1]
            neg_values = values[1:]
            neg_values = neg_values*self.exponential(x_neg, lifetime_aver)

            # Expected value
            return np.sum(pos_values) - np.sum(neg_values)


if __name__ == '__main__':
    aver_mem = 4
    monthly = True
    cl = Client(aver_mem, monthly)
