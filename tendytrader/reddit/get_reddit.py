from psaw import PushshiftAPI
import praw
import pandas as pd
import datetime as dt
import time
import os
import json
'''
fpath = os.path.join("")
with open('../tickers.txt') as f:
    tickers = f.read().split()
filename = test
'''
reddit = praw.Reddit(client_id='Kq6zH6HM1m7VEg', \
                     client_secret='4Dqt6IHeYF2-weUzJ6zzirbP9zs', \
                     user_agent='lsenti')

api = PushshiftAPI()

# See pushshift API for descriptions of arguments  https://pushshift.io/api-parameters/
def get_reddit_comments(search_terms, subreddits, sort, descending, size):
    for term in search_terms:
        data = api.search_comments(q=term, subreddit=subreddits, \
        sort=sort, size=size, filter=['subreddit','id', 'score', 'body', 'created_utc'])
        topics_dict = {
                "subreddit" : [],
                "id" : [],
                "score" : [],
                "body" : [],
                "created_utc" : []    
        }
        for comment in data:
            topics_dict["subreddit"].append(comment.subreddit)
            topics_dict["id"].append(comment.id)
            topics_dict["body"].append(comment.body.replace('\r', ' ').replace('\n', ' '))
            topics_dict["created_utc"].append(comment.created_utc)
            topics_dict["score"].append(comment.score)

        data = pd.DataFrame(topics_dict)

        data.to_csv(term + '.csv', index=False) 

def get_reddit_submissions(search_terms, subreddits, sort, descending, size):
    for term in search_terms:
        data = api.search_submissions(q=term, subreddit=subreddits, \
        sort=sort, size=size, filter=['subreddit', 'title', 'id', 'score', 'body', 'created_utc'])
        topics_dict = { "subreddit":[], 
            "title":[], 
            "score":[], 
            "id":[], 
            "created_utc": [], 
            "body":[]}

        for submission in term:
            topics_dict["subreddit"].append(submission.subreddit)
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["created_utc"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
        
        data = pd.DataFrame(topics_dict)

        data.to_csv(term + '.csv', index=False) 
    