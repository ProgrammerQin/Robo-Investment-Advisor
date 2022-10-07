# https://twelvedata.com/docs#getting-started
# API key: 13142851cdfe4856bd76e5297106e00b
# Present Stock Value PLOT


# pip install twelvedata
# pip install matplotlib
# pip install mplfinance


stock = 'TLSA'
# stock = 'AAPL'
# stock = 'AMZN'
investment = stock


# foreign_currency = 'EUR/USD'
# foreign_currency = 'CNY/USD'
# foreign_currency = 'CAD/USD'
# investment = foreign_currency


# digital_currency = 'BTC/USD'
# digital_currency = 'ETH/USD'
# investment = digital_currency


from twelvedata import TDClient

td = TDClient(apikey="13142851cdfe4856bd76e5297106e00b")
ts = td.time_series(
    symbol=investment,
    outputsize=75,
    interval="1day",
)

# 1. Returns OHLCV chart
# ts.as_pyplot_figure()


# 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
ts.with_bbands().with_percent_b().with_stoch().as_pyplot_figure()
