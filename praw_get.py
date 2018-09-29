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
payload = {'q' : 'subreddit:wallstreetbets flair:dd'}
reddit = praw.Reddit(client_id='Kq6zH6HM1m7VEg', \
                     client_secret='4Dqt6IHeYF2-weUzJ6zzirbP9zs', \
                     user_agent='lsenti', \
                     username='tendybot', \
                     password='NEvAijthivewAi5')

# remove hardcoded pw 
# https://praw.readthedocs.io/en/latest/getting_started/configuration.html#configuration

reddit.read_only = True
wsb = reddit.subreddit('wallstreetbets')

print(reddit.get('search', params=payload))