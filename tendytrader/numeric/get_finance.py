import datetime
import resource
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

from tickers import test_tickers

def get_all_stock_data(start, end, threads=(int)(resource.RLIMIT_NPROC*0.25)):
    assert isinstance(start, datetime.datetime), "Error: start time must be datetime object"
    assert isinstance(end, datetime.datetime), "Error: end time must be datetime object"
    yf.pdr_override()
    data = []
    for t in test_tickers:
        df = pdr.get_data_yahoo(t, start=start, end=end, threads=threads)
        df.index = range(len(df.index))
        data.append((t, start, df))
    return data

def get_stock_data(tick, start, end, threads=(int)(resource.RLIMIT_NPROC*0.25)):
    assert isinstance(start, datetime.datetime), "Error: start time must be datetime object"
    assert isinstance(end, datetime.datetime), "Error: end time must be datetime object"
    yf.pdr_override()
    data = []
    if type(tick) is str:
        df = pdr.get_data_yahoo(tick, start=start, end=end, threads=threads)
        df.index = range(len(df.index))
        data.append((tick, start, df))
    else:
        for t in tick:
            df = pdr.get_data_yahoo(t, start=start, end=end, threads=threads)
            df.index = range(len(df.index))
            data.append((t, start, df))

    return data
