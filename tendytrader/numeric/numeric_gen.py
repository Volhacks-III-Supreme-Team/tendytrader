import pandas as pd
import datetime as dt
import os
import resource
from get_finance import get_all_stock_data, get_stock_data
from clean_data import clean_stock_nan

def export_all_data_to_csv(start, end, threads=(int)(resource.RLIMIT_NPROC*0.25),
                           out_dir="../data/numeric"):
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
    data = get_all_stock_data(start, end, threads)
    for ticker, stime, df in data:
        clean_stock_nan(df)
        df["ticker"] = ticker
        df["start_time"] = stime.replace(tzinfo=dt.timezone.utc).timestamp()
        df.to_csv(os.path.join(abs_out, "{0:s}.csv".format(ticker)))

def export_ticker_to_csv(ticker, start, end, threads=(int)(resource.RLIMIT_NPROC*0.25),
                         out_dir="../data/numeric"):
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
    data = get_stock_data(ticker, start, end, threads)
    for tick, df in data:
        clean_stock_nan(df)
        df["ticker"] = ticker
        df.to_csv(os.path.join(abs_out, "{0:s}.csv".format(ticker)))
