#!/usr/bin/env python
"""
Pro-rated refund forecast model for the SaaS project.
This Application provides basic support for forecasting pro-rated refunds
in order to provide a company a better understanding of the cash reserves
needed to be kept.
----------------------------------------------------------------------------

Usage
-----
Use the following line to run this application:

    $ ipython forecast.py ../input/model_input.yml ../output/mode_output.txt

----------------------------------------------------------------------------
"""

# --- Imports

# Standard libraries
import yaml
import argparse
import sys
import json
import seaborn as sns
import matplotlib.pyplot as plt

# Application classes
from finances import Finances

# --- Helper functions

def process_command_line():
    """
    Process command-line arguments and options.

    Arguments
    ---------
    None

    Return values
    -------------
    Namespace object containing parsed command-line arguments and options.
    """

    # Create parser
    parser = argparse.ArgumentParser(description= 'Parse command line arguments')

    # Add positional arguments
    parser.add_argument('model_input', help='name of yml input file')
    parser.add_argument('savefile_name', help='filename to save output to')

    # Parse arguments
    return parser.parse_args()

def plot_(d):
    """
    Plots the cash percentage in the finances reserve needed to the kept
    depending on a time scale, month or day.

    Arguments
    ---------
    Dictinary

    Return values
    -------------
    None
    """

    sns.barplot(x=d.keys(), y=d.values())
    plt.title('Percentage Cash to Keep')
    plt.ylabel('Cash')
    plt.xlabel('Time')
    plt.show()

# --- Main program

def main():
    """
    Main program.
    """

    # Define command line arguments
    args = process_command_line()
    #print 'Arguments are: {}'.format(args)

    # --- Preparations
    model_inputs = yaml.load(open(args.model_input).read())
    outname = args.savefile_name

    # Initialize Finances
    fin = Finances(model_inputs)

    # Get pro-rated refund forecast
    perc_refund = fin.percentage_refund_cumulative()

    # Json output
    with open(outname, 'w') as output:
        json.dump(perc_refund, output, sort_keys = True, indent = 4)

    # Plot result
    plot_(perc_refund)

# --- Main script

if __name__ == '__main__':
    # Run main()
    status_code = main()

    # Exit with status code
    sys.exit(status_code)
