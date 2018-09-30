from get_reddit import get_reddit_submissions, get_reddit_comments
import datetime as dt

get_reddit_comments(["AMD", "TSLA"], "wallstreetbets,stocks", dt.datetime(2018,9,25), \
    dt.datetime(2018,9,26), 100)