# https://twelvedata.com/docs#getting-started
# API key: 13142851cdfe4856bd76e5297106e00b

# pip install twelvedata
from twelvedata import TDClient

td = TDClient(apikey="13142851cdfe4856bd76e5297106e00b")
ts = td.time_series(
    symbol="TLSA",
    outputsize=75,
    interval="1day",
)

# 1. Returns OHLCV chart
ts.as_pyplot_figure()

# 2. Returns OHLCV + BBANDS(close, 20, 2, SMA) + %B(close, 20, 2 SMA) + STOCH(14, 3, 3, SMA, SMA)
ts.with_bbands().with_percent_b().with_stoch(slow_k_period=3).as_pyplot_figure()