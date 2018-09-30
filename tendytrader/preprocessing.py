import os
import datetime as dt
import pandas
from reddit.sentiment_analysis import average_sentiment
import heapq

# Takes phat dataframe from long time, 
def split_sentiment_by_day(df):
    ''' 
    epoch = dt.datetime.utcfromtimestamp(0)
    def unix_time_s(det):
        return int((det - epoch).total_seconds())

    def get_date(created):
        return dt.datetime.fromtimestamp(created)
    '''
    DFList = []
    for group in df.groupby(df.index.day):
        DFList.append(group[1])
    print(DFList)
    return DFList
    
def pull_dataset(terms, begin_time, end_time)
    pass

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
        sentiment_dict = {
            "sentiment" : [],
            "polarity" : [],
            "term_count" : []
        }
        # Organizes sentiments from per term to per day
        for df in split_sentiment_by_day(comments_df):
            sentiment_dict.append(average_sentiment(df))

        sentiments = pandas.DataFrame(sentiment_dict)
        financials_df.join(sentiments)
        df_list.append(financials_df)
    
    return df_list
