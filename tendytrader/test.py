from reddit.get_reddit import get_reddit_submissions, get_reddit_comments
import datetime as dt
import preprocessing
from reddit.sentiment_analysis import average_sentiment
import os
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

# Testing sentiment analysis
date1 = dt.datetime(2018,3,25)
date2 = dt.datetime(2018,9,25)
#get_reddit_comments(["TSLA"], "wallstreetbets", date1, date2)

# Retrieve dataframe from csv
abs_in = os.path.abspath('../data/reddit/comments')
pd = read_csv(os.path.join(abs_in, 'comments_TSLA.csv'), \
parse_dates=True, date_parser=preprocessing.get_date, \
index_col='created_utc')

# Split into dataframes by day
sentiments = preprocessing.get_sentiment_series(pd)

delta = dt.timedelta(days=1)
dates = drange(date1, date2, delta)
fig, ax = plt.subplots()
ax.plot_date(dates, sentiments['sentiment'], 'r-')
ax.plot(dates, sentiments['polarity'], 'b-')

# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_minor_locator(HourLocator(arrange(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()
plt.show()