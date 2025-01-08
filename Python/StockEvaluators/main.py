# main.py
# OOTB Python libraries
import time
import csv
import importlib

# Custom Library Imports
import stock_validation
from ValuationMethods import valuation_method_selection
from ValuationMethods import sm_stock_evaluation
# import buffett_stock_evaluation


def main():
    ticker = input("Enter a stock ticker: ")
    valid_stock = stock_validation.get_stock_name(ticker)
    print() # spacing
    if valid_stock:
        valutation_method = valuation_method_selection.get_valuation_method()
        time.sleep(5)  # Makes Python wait for 5 seconds
        print() # spacing

        # Dynamically import the Python file based on the user's choice
        module = importlib.import_module(valutation_method)

        # Get the stock info from the selected module
        stock_info = module.get_stock_info(ticker)
        # stock = sm_stock_evaluation.get_stock_info(ticker)
    else:   
        print("Exiting program.")

if __name__ == "__main__":
    main()