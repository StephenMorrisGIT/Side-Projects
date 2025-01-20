
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
import math
from Objects.output import Output
#from docx import Document

#constants
revenue_growth_target = 5

def get_stock_info(ticker: str, output_obj: Output):
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
    print_and_add_to_output(output_obj, f"Company Name: {company_name}", None)
    print_and_add_to_output(output_obj, f"Ticker: {ticker}", None)
    if market_cap_billion:
        print_and_add_to_output(output_obj, f"Market Cap: ${market_cap_billion:,.2f}b", None)
    print_and_add_to_output(output_obj, f"Stock Price: ${stock_price:,.2f}", None)
    print_and_add_to_output(output_obj, "", None)
    print_and_add_to_output(output_obj, f"Industry: {industry}", None)
    print_and_add_to_output(output_obj, f"Sector: {sector}", None)
    print_and_add_to_output(output_obj, "", None)
    if revenue_growth_years >= revenue_growth_target:
        print_and_add_to_output(output_obj, f"Years of Revenue Growth: {revenue_growth_years}", "green")
    else:
        print_and_add_to_output(output_obj, f"Years of Revenue Growth: {revenue_growth_years}", "red")
    print_and_add_to_output(output_obj, f"Years of Profit Growth: {profit_growth_years}", None)
    print_and_add_to_output(output_obj, "", None)
    
    
    if earnings_per_share < 0:
        print_and_add_to_output(output_obj, f"Earnings Per Share (TTM): ${earnings_per_share:,.2f}", "red")
    else:
        print_and_add_to_output(output_obj, f"Earnings Per Share (TTM): ${earnings_per_share:,.2f}",None)
    
    if dividend_yield is None or dividend_yield == 0:
        print_and_add_to_output(output_obj, "Stock does not currently pay a dividend", "red")
    else:
        print_and_add_to_output(output_obj, f"Dividend Yield: {dividend_yield*100:.2f}%", None)
    
    if price_to_earnings < 0:
        print_and_add_to_output(output_obj, f"Price/Earnings is currently negative", "red")
    else:
        print_and_add_to_output(output_obj, f"Price to Earnings Ratio: {price_to_earnings:.2f}", None)
    
    if eps_growth_fy == -1 or math.isnan(eps_growth_fy):
        print_and_add_to_output(output_obj, "Annual EPS Growth could not be calculated", "red")
    elif eps_growth_fy < 0:
        print_and_add_to_output(output_obj, "EPS GROWTH (ANNUAL): {:.2f}%".format(eps_growth_fy), "green")
    else:
        print_and_add_to_output(output_obj, "EPS GROWTH (ANNUAL): {:.2f}%".format(eps_growth_fy), None)

    if price_to_earnings_growth == -1 or math.isnan(price_to_earnings_growth):
        print_and_add_to_output(output_obj, "PEG could not be calculated", "red")
    else:   
        print_and_add_to_output(output_obj, f"Price/Earnings Growth: {price_to_earnings_growth:.2f}", None)
    
    print_and_add_to_output(output_obj, f"Price to Book Ratio: {price_to_book:.2f}", None)
    
    if price_to_sales is None or price_to_sales == 0:
        print_and_add_to_output(output_obj, "Price to Sales Ratio: N/A", "red")
    else:
        print_and_add_to_output(output_obj, f"Price to Sales Ratio: {price_to_sales:.2f}", None)
    
    return output_obj    

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

def print_and_add_to_output(output_obj, line, color):
    if color == "green":
        print(f"\033[92m{line}\033[0m")
    elif color == "red":
        print(f"\033[91m{line}\033[0m")
    else:
        print(line)
    output_obj.add(line, color)

# ticker = input("Enter a stock ticker: ")
# get_stock_info(ticker)

