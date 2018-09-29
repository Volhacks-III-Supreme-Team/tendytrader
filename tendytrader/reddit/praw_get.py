#! usr/bin/env python3
# textblob
import praw
import pandas as pd
import datetime as dt
import time

'''
Retrieves wsb reddit dataset. 
Will be more configurable in the future
Brainstorming: actual reddit bot that posts & builds off
of user feedback
fires on new post
download only tickers mentioned in wsb
hindsight bias?
'''
epoch = dt.datetime.utcfromtimestamp(0)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

def unix_time_s(det):
    return int((det - epoch).total_seconds())

reddit = praw.Reddit(client_id='Kq6zH6HM1m7VEg', \
                     client_secret='4Dqt6IHeYF2-weUzJ6zzirbP9zs', \
                     user_agent='lsenti')


def reddit_get_comments(payload, filename):
    # search by day range, #TODO currently assumes 1 post per day which is just not true
    
        search = reddit.get('search', params=payload)

        topics_dict = {
            "id" : [],
            "body" : [],
            "created_utc" : [],
            "score" : []    
        }

        for submission in search:
            submission.comments.replace_more(limit=0)

            for comment in submission.comments.list():
                topics_dict["id"].append(comment.id)
                topics_dict["body"].append(comment.body.replace('\r', '').replace('\n', ''))
                topics_dict["created_utc"].append(comment.created_utc)
                topics_dict["score"].append(comment.score)

        topics_data = pd.DataFrame(topics_dict)

        _timestamp = topics_data["created_utc"].apply(get_date)
        topics_data = topics_data.assign(timestamp = _timestamp)
        topics_data.to_csv(filename + '_' + _timestamp[0].isoformat()[:10] + '.csv', index=False) 
    
def reddit_get_submissions(payload, filename):
    search = reddit.get('search', params=payload)

    topics_dict = { "title":[], 
                "score":[], 
                "id":[], "url":[],  
                "comms_num": [], 
                "created": [], 
                "body":[]}

    for submission in search:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
    
        topics_data = pd.DataFrame(topics_dict)
        _timestamp = topics_data["created_utc"].apply(get_date)
        topics_data = topics_data.assign(timestamp = _timestamp)

        topics_data.to_csv(filename + _timestamp[0].isoformat()[:10] + '.csv', index=False) 
