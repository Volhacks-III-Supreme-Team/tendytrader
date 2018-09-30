from psaw import PushshiftAPI
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
api = PushshiftAPI()

# See pushshift API for descriptions of arguments  https://pushshift.io/api-parameters/
def get_reddit_comments(search_terms, subreddits, sort, size, out_dir="../data/reddit"):
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
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
        localname = 'comments_' + term + '.csv'
        data.to_csv(os.path.join(abs_out, localname), index=False) 

def get_reddit_submissions(search_terms, subreddits, sort, size, out_dir="../data/reddit"):
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
    for term in search_terms:
        data = api.search_submissions(q=term, subreddit=subreddits, \
        sort=sort, size=size, filter=['subreddit', 'title', 'id', 'score', 'body', 'created_utc'])
        topics_dict = { "subreddit":[], 
            "title":[], 
            "score":[], 
            "id":[], 
            "created_utc": [], 
            "body":[]
        }

        for submission in data:
            topics_dict["subreddit"].append(submission.subreddit)
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["created_utc"].append(submission.created)
            #topics_dict["body"].append(submission.selftext)
            topics_dict["body"].append(submission.title.replace('\r', ' ').replace('\n', ' '))
        
        data = pd.DataFrame(topics_dict)
        localname = 'submissions_' + term + '.csv'
        data.to_csv(os.path.join(abs_out, localname), index=False) 
