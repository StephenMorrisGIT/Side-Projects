
# TODO: 
# methods docs
# Add more attributes to pull from the stock API
# Fix get_consecutive_revenue_growth and get_consecutive_profit_growth
# Make Basic EPS a constant
# Give users the ability to manually change the information and then re-print
# Add different stock evaluation methods (Buffet method, personal method, etc). Ask chat gpt about typical stock evaluation methods
# Export to a word/txt file
# Do the market stock checks 
# Do the valuation comparisions
# Find an API that can do quarterly financials

import yfinance as yf

def get_stock_info(ticker: str):
    stock = yf.Ticker(ticker)
    if not stock.info:
        print("\033[91mNo information found for the given stock ticker\033[0m")
        return
    info = stock.info
    # print(info)
    financials = stock.financials
    
    # Grabbing stock attributes
    company_name = info.get("longName")
    industry = info.get("industry")
    sector = info.get("sector")
    market_cap = info.get("marketCap")
    stock_price = info.get("currentPrice")
    earnings_per_share = info.get("trailingEps")
    dividend_yield = info.get("dividendYield")
    price_to_book = info.get("priceToBook")
    price_to_sales = info.get("priceToSalesTrailing12Months")
    # price_to_earnings_growth = info.get("pegRatio")

    revenue_growth_years = get_consecutive_revenue_growth(financials)
    profit_growth_years = get_consecutive_profit_growth(financials)

    # Formatting/Calculations
    market_cap_billion = market_cap / 1_000_000_000
    price_to_earnings = stock_price / earnings_per_share
    
    # Get the latest two years' data
    latest_year = financials.columns[0]
    previous_year = financials.columns[1]

    if not financials[latest_year].empty or not financials[previous_year].empty:
        # Calculate the EPS growth for the last full fiscal year versus the fiscal year before that
        if (financials[previous_year].get("Basic EPS") is None or financials[previous_year].get("Basic EPS") <= 0 ) or (financials[latest_year].get("Basic EPS") is None or financials[latest_year].get("Basic EPS") <= 0):
            eps_growth_fy = -1
        else:
            eps_growth_fy = (financials[latest_year].get("Basic EPS") - financials[previous_year].get("Basic EPS")) / financials[previous_year].get("Basic EPS") * 100
    if earnings_per_share < 0 or eps_growth_fy < 0:
        price_to_earnings_growth = -1   
    else:
        price_to_earnings_growth = (stock_price / earnings_per_share)/eps_growth_fy

    # Printing
    print(f"\033[1mCompany Name:\033[0m {company_name}")
    print(f"\033[1mTicker:\033[0m {ticker}")
    print(f"\033[1mMarket Cap:\033[0m ${market_cap_billion:,.2f}b")
    print(f"\033[1mStock Price:\033[0m ${stock_price:,.2f}")
    print()
    print(f"\033[1mIndustry:\033[0m {industry}")
    print(f"\033[1mSector:\033[0m {sector}")
    print()
    print(f"\033[1mYears of Revenue Growth:\033[0m {revenue_growth_years}")
    print(f"\033[1mYears of Profit Growth:\033[0m {profit_growth_years}")
    print()
    
    if earnings_per_share < 0:
        print(f"\033[91mEarnings Per Share:\033[0m ${earnings_per_share:,.2f}\033[0m")
    else:
        print(f"\033[1mEarnings Per Share (TTM):\033[0m ${earnings_per_share:,.2f}")
    
    if dividend_yield is None or dividend_yield == 0:
        print("\033[91mStock does not currently pay a dividend\033[0m")
    else:
        print(f"\033[1mDividend Yield:\033[0m {dividend_yield*100:.2f}%")
    
    if price_to_earnings < 0:
        print("\033[91mPrice/Earnings is currently negative\033[0m")
    else:
        print(f"\033[1mPrice to Earnings Ratio:\033[0m {price_to_earnings:.2f}")
    
    if eps_growth_fy == -1:
        print("\033[91mAnnual EPS Growth could not be calculated\033[0m")
    elif eps_growth_fy < 0:
        print("\033[91mEPS GROWTH (ANNUAL):\033[0m {:.2f}%\033[0m".format(eps_growth_fy)) 
    else:
        print("\033[1mEPS GROWTH (ANNUAL):\033[0m {:.2f}%".format(eps_growth_fy))  

    if price_to_earnings_growth == -1:
        print("\033[91mPEG could not be calculated\033[0m")
    else:   
        print(f"\033[1mPrice/Earnings Growth:\033[0m {price_to_earnings_growth:.2f}")
    
    print(f"\033[1mPrice to Book Ratio:\033[0m {price_to_book:.2f}")
    
    if price_to_sales is None or price_to_sales == 0:
        print("\033[91mPrice to Sales Ratio: N/A\033[0m")
    else:
        print(f"\033[1mPrice to Sales Ratio:\033[0m {price_to_sales:.2f}")

def get_consecutive_revenue_growth(financials):
    # Extract revenue data
    revenue = financials.loc['Total Revenue']

    # Initialize the count for consecutive growth years
    consecutive_growth_count = 0

    # Check for consecutive revenue growth from the most recent year
    for i in range(1, len(revenue)):
        if revenue[i] > revenue[i - 1]:
            consecutive_growth_count += 1
        else:
            consecutive_growth_count = 0  # Reset the count if growth is not consecutive

    return consecutive_growth_count

def get_consecutive_profit_growth(financials):
    profit_data = financials.iloc[3, :-1]  # Get the net income data from the 4th row
    profit_growth_years = 0
    for i in range(1, len(profit_data)):
        if profit_data[i] > profit_data[i-1]:
            profit_growth_years += 1
        else:
            break
    return profit_growth_years


# ticker = input("Enter a stock ticker: ")
# get_stock_info(ticker)

