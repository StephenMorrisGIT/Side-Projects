
# TODO: 
# Add more attributes to pull from the stock API
# Add different stock evaluation methods (Buffet method, ETC)
# Export to a word/txt file
# Do the market stock checks 
# Do the valuation comparisions

import yfinance as yf

def get_stock_info(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    # print(info)
    financials = stock.financials

    # Grabbing stock attributes
    company_name = info.get("shortName")
    industry = info.get("industry")
    sector = info.get("sector")
    market_cap = info.get("marketCap")
    stock_price = info.get("currentPrice")
    earnings_per_share = info.get("trailingEps")
    dividend_yield = info.get("dividendYield")
    price_to_book = info.get("priceToBook")
    price_to_sales = info.get("priceToSalesTrailing12Months")
    revenue_growth_years = get_consecutive_revenue_growth(financials)
    profit_growth_years = get_consecutive_profit_growth(financials)

    # Formatting
    market_cap_billion = market_cap / 1_000_000_000
    price_to_earnings = stock_price / earnings_per_share

    # Printing
    print(f"Company Name: {company_name}")
    print()
    print(f"Industry: {industry}")
    print(f"Sector: {sector}")
    print()
    print(f"Years of Revenue Growth: {revenue_growth_years}")
    print(f"Years of Profit Growth: {profit_growth_years}")
    print()
    print(f"Market Cap: ${market_cap_billion:,.2f}b")
    print(f"Stock Price: ${stock_price:,.2f}")
    if earnings_per_share < 0:
        print(f"\033[91mEarnings Per Share: ${earnings_per_share:,.2f}\033[0m")
    else:
        print(f"Earnings Per Share: ${earnings_per_share:,.2f}")
    if dividend_yield is None or dividend_yield == 0:
        print("\033[91mStock does not currently pay a dividend\033[0m")
    else:
        print(f"Dividend Yield: {dividend_yield*100:.2f}%")
    
    if price_to_earnings < 0:
        print("\033[91mEPS is currently negative\033[0m")
    else:
        print(f"Price to Earnings Ratio: {price_to_earnings:.2f}")

    print(f"Price to Book Ratio: {price_to_book:.2f}")
    
    if price_to_sales is None or price_to_sales == 0:
        print("\033[91mPrice to Sales Ratio: N/A\033[0m")
    else:
        print(f"Price to Sales Ratio: {price_to_sales:.2f}")

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

# Example usage:
ticker = input("Enter a stock ticker: ")
get_stock_info(ticker)
