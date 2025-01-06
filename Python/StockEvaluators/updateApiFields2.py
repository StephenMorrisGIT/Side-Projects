import yfinance as yf

def get_yfinance_field_constants(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    field_constants = list(info.keys())
    return field_constants

def write_fields_to_file(fields, filename):
    with open(filename, 'w') as f:
        f.write("\n".join(fields))

def get_financials_data(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    return financials

def write_financials_to_file(financials, filename):
    with open(filename, 'w') as f:
        f.write("\n".join(map(str, financials.index)))

# Example usage:
ticker = "AAPL"
field_constants = get_yfinance_field_constants(ticker)
write_fields_to_file(field_constants, 'yfinanceFieldConstants.txt')

financials = get_financials_data(ticker)
write_financials_to_file(financials, 'yfinanceFinancialColumnsConstants.txt')

print("\033[92mFinancial data and field constants have been successfully retrieved and written to files.\033[0m")