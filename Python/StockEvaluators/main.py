# main.py

import stock_validation
import validation_list
import sm_stock_evaluation
import buffett_stock_evaluation

def main():
    ticker = input("Enter a stock ticker: ")
    valid_stock = stock_validation.get_stock_name(ticker)
    if valid_stock:

        stock = sm_stock_evaluation.get_stock_info(ticker)
    else:
        print("Exiting program.")

if __name__ == "__main__":
    main()