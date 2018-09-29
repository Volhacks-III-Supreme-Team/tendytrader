#! usr/bin/env python3
# textblob
import praw
import pandas as pd
import datetime as dt

'''
Retrieves wsb reddit dataset. 
Will be more configurable in the future
Brainstorming: actual reddit bot that posts & builds off
of user feedback
fires on new post
download only tickers mentioned in wsb
hindsight bias?
'''
subreddit = 'wallstreetbets'

payload = {'q' : 'subreddit:wallstreetbets flair:dd'
            ''}
reddit = praw.Reddit(client_id='Kq6zH6HM1m7VEg', \
                     client_secret='4Dqt6IHeYF2-weUzJ6zzirbP9zs', \
                     user_agent='lsenti')

# remove hardcoded pw 
# https://praw.readthedocs.io/en/latest/getting_started/configuration.html#configuration

wsb = reddit.subreddit(subreddit)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

search = reddit.get('search', params=payload)

# search by day range
for submission in search:
    print(submission.title, submission.id)

topics_dict = { "title":[], \
            "score":[], \
            "id":[], "url":[], \ 
            "comms_num": [], \
            "created": [], \
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

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('FILENAME.csv', index=False) 

