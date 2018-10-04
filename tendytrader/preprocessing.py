import os
import datetime as dt
import pandas
from reddit.sentiment_analysis import average_sentiment
from reddit.get_reddit import get_reddit_comments, get_reddit_submissions
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
import heapq

def get_date(created):
    return dt.datetime.fromtimestamp(float(created))

# Splits dataframe, presumably by timeseries. freq can equal d for day,
# or CustomBusinessDay(calendar=USFederalHolidayCalendar()) for open days   
def split_df(df, freq):
    df = df.groupby(pandas.Grouper(freq=freq))
    df = [group for _, group in df]
    return df

def merge_comments_submissions():
    pass

def get_sentiment_series(df_list):
    sentiment_dict = {
        "sentiment" : [],
        "polarity" : [],
        "term_count" : []
    }
    # Organizes sentiments from per term to per day
    for df in split_df(df_list, 'D'):
        sentiment = average_sentiment(df)
        sentiment_dict['sentiment'].append(sentiment[0])
        sentiment_dict['polarity'].append(sentiment[1])
        sentiment_dict['term_count'].append(sentiment[2])

    return pandas.DataFrame(sentiment_dict)


def get_terms():    
    abs_terms = os.path.abspath('../')
    terms = []
    with open(os.path.join(abs_terms, 'terms.txt'), 'r') as f:
        terms = f.read().split(',')
    return terms

def get_tickers():
    return get_terms()

# Pulls with uniform timeframe for financial and sentiment data
def pull_dataset(terms, begin_time, end_time):
    pass
  
# Binary decision, up or down. Not mixed with other tickers
def gen_label_data(financials_df):
    labels = []
    for i in range(len(financials_df.index)-1):
        labels.append(int(financials_df['Open'][i] <= financials_df['Open'][i+1]))
    labels.append(0)
    financials_df["label"] = labels
    
def kill_weekends(sentiments, financials):
    sent_heap = heapq.heapify(sentiments.index[:])
    fin_heap = heapq.heapify(financials.index[:])
    sent_weekends = []
    while len(sent_heap) != 0 and len(fin_heap) != 0:
        sent_date = heapq.heappop(sent_heap)
        fin_date = heapq.heappop(fin_heap)
        if sent_date < fin_date:
            sent_weekends.append(sent_date)
            heapq.heappush(fin_date)
    sentiments.drop(index=sent_weekends)

# Merges financial dataset with financial dataset
def merge_datasets(terms):
    # load csvs from reddit comments, submissions, 
    abs_in_comments = os.path.abspath('../data/reddit/comments/')
    abs_in_finance = os.path.abspath('../data/numeric/')
    # abs_in_submissions = os.path.abspath('../data/reddit/submissions')
    df_list = []
    for term in terms:
        reddit_localname = 'comments_' + term + '.csv'
        comments_df = pandas.read_csv(os.path.join(abs_in_comments, reddit_localname))
        financials_df = pandas.read_csv(os.path.join(abs_in_finance, term + '.csv'))
        sentiments = get_sentiment_series(split_df(comments_df, 'D'))
        financials_df.join(sentiments)
        gen_label_data(financials_df)
        df_list.append(financials_df)
    
    return df_list
