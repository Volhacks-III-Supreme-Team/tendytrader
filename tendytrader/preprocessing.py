import os
import datetime as dt
import pandas
from reddit.sentiment_analysis import average_sentiment

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

# Binary decision, up or down. Not mixed with other tickers
def gen_label_data(financial_df):
    labels = []
    for i in range(len(financials_df.index)-1):
        labels.append(int(financials_df['Open'][i] <= financials_df['Open'][i+1]))

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
        gen_label_data(financials_df)
        df_list.append(financials_df)
    
    return df_list


