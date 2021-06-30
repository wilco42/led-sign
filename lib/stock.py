import yfinance as yf
import io
import pandas as pd

def get_stock_info(symbol):
    ticker = yf.Ticker(symbol)

    previous_close_price = ticker.info['previousClose']
    market_price = ticker.info['regularMarketPrice']
    open_price = ticker.info['regularMarketPrice']
    day_high = ticker.info['dayHigh']
    day_low = ticker.info['dayLow']

    history = ticker.history(period="1d", interval="5m")
    colspecs = [(0,25), (27, 37), (39, 49), (51, 61), (63, 73), (76, 81), (91, 92), (105, 106)]
    processed_string = history.to_string().split("\n", 2)[2]
    data = io.StringIO(processed_string)
    df = pd.read_fwf(data, colspecs=colspecs, header=None)
    new_df = df.drop(columns=[0, 1, 2, 3, 5, 6, 7])
    max_value = round(new_df[4].max(), 2)
    min_value = round(new_df[4].min(), 2)
    diff = round(max_value - min_value, 2)
    increment = round(diff / 16, 2)
    rows = len(new_df.index)
    day_diff = round(market_price - previous_close_price, 2)
    percent = round((day_diff) / previous_close_price * 100, 2)
    info = {'symbol': symbol, 'current_price': market_price, 'day_diff': day_diff, 'max': max_value, 'min': min_value, 'increment': increment, 'total_rows': rows, 'percent': percent, data: new_df}
    return info

