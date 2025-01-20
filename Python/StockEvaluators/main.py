# main.py
# OOTB Python libraries
import time
import csv
import importlib
import os
import sys

# Custom Library Imports
import stock_validation
from ValuationMethods import valuation_method_selection
from ValuationMethods import sm_stock_evaluation
# import buffett_stock_evaluation

# Constants
valuation_methods_dir = 'ValuationMethods'

def main():
    ticker = input("Enter a stock ticker: ")
    valid_stock = stock_validation.get_stock_name(ticker)
    print() # spacing
    if valid_stock:
        valuation_method = valuation_method_selection.get_valuation_method()
        time.sleep(3)  # Makes Python wait for 3 seconds
        print() # spacing

        # Dynamically import the Python file based on the user's choice
        file_name = f"{valuation_methods_dir}.{valuation_method}"
        module = importlib.import_module(file_name)

        # Get the stock info from the selected module
        stock_info = module.get_stock_info(ticker)
        # stock_info = sm_stock_evaluation.get_stock_info(ticker)
    else:   
        print("Exiting program.")

if __name__ == "__main__":
    main()