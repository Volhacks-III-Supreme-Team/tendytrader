from psaw import PushshiftAPI
import praw
import pandas as pd
import datetime as dt
import time
import os
import json

### TODO Finish whatever this is

'''
fpath = os.path.join("")
with open('../tickers.txt') as f:
    tickers = f.read().split()
filename = test
'''

api = PushshiftAPI()
search_str='Donald Trump'
subreddits = 'wallstreetbets'
for ticker in tickers:
ticker_data = api.search_comments(q=ticker, subreddit=subreddits, \
sort='desc', size=500, filter=['id', 'score', 'body', 'created_utc'])
topics_dict = {
        "id" : [],
        "score" : [],
        "body" : [],
        "created_utc" : []    
}
for comment in ticker_data:
    topics_dict["id"].append(comment.id)
    topics_dict["body"].append(comment.body.replace('\r', ' ').replace('\n', ' '))
    topics_dict["created_utc"].append(comment.created_utc)
    topics_dict["score"].append(comment.score)

ticker_data = pd.DataFrame(topics_dict)

ticker_data.to_csv(ticker + '.csv', index=False) 
