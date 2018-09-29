import datetime
import resource
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

from .tickers import test_tickers

def get_all_stock_data(start, end, threads=(int)(resource.RLIMIT_NPROC*0.25)):
    assert isinstance(start, datetime.datetime), "Error: start time must be datetime object"
    assert isinstance(end, datetime.datetime), "Error: end time must be datetime object"
    yf.pdr_override()
    data = pdr.get_data_yahoo(test_tickers, start=start, end=end, group_by="ticker")
    return data

def get_stock_data(tick, start, end, threads=(int)(resource.RLIMIT_NPROC*0.25)):
    assert isinstance(start, datetime.datetime), "Error: start time must be datetime object"
    assert isinstance(end, datetime.datetime), "Error: end time must be datetime object"
    yf.pdr_override()
    if tick is str:
        gb = "column"
    else:
        gb = "ticker"
    data = pdr.get_data_yahoo(tick, start=start, end=end, group_by=gb)
    return data
