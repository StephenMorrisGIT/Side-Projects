import yfinance as yf

def get_yfinance_field_constants(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    field_constants = list(info.keys())
    return field_constants

def write_fields_to_file(fields, filename):
    with open(filename, 'w') as f:
        f.write("\n".join(fields))

# Example usage:
ticker = "SOFI"
field_constants = get_yfinance_field_constants(ticker)
write_fields_to_file(field_constants, 'yfinanceFieldConstants.txt')