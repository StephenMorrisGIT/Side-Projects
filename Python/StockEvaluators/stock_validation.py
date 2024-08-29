# stock_valuation.py
# Todo:
# Make it so it loops back if the user chooses n

import yfinance as yf

def get_stock_name(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if info:
            stock_name = info.get("longName")
            if stock_name:
                print(f"Stock Name: {stock_name}")
                while True:
                    validate = input("Is this correct? (y/n): ").lower()
                    if validate == 'y':
                        return True
                    elif validate == 'n':
                        return False
                    else:
                        print("Invalid input. Please enter y or n.")
            else:
                print("\033[91mError: Unable to retrieve stock name.\033[0m")
                return False
        else:
            print("\033[91mError: Stock ticker does not exist.\033[0m")
            return False
    except Exception as e:
        print("\033[91mError: {}\033[0m".format(str(e)))
        return False