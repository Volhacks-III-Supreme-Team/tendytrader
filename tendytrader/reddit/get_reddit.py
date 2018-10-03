from psaw import PushshiftAPI
import pandas as pd
import datetime as dt
import time
import os
import json
import praw

api = PushshiftAPI()
epoch = dt.datetime.utcfromtimestamp(0)

def epoch_time(dtdt):
    return (dtdt - epoch).total_seconds()

def get_date(created):
    return dt.datetime.fromtimestamp(created)
    
# See pushshift API for descriptions of arguments  https://pushshift.io/api-parameters/
def get_reddit_comments(search_terms, subreddits, begin_time, end_time, size, out_dir="../data/reddit/comments"):
        
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
    for term in search_terms:
        
        data = api.search_comments(q=term, subreddit=subreddits, after=int(begin_time.timestamp()), 
            before=int(end_time.timestamp()), sort='asc', size=size, \
            filter=['subreddit','id', 'score', 'body', 'created_utc'])
        
        topics_dict = {
                "subreddit" : [],
                "id" : [],
                "score" : [],
                "body" : [],
                #"created_utc" : []    
        }
        tstamps = []

        for comment in data:
            topics_dict["subreddit"].append(comment.subreddit)
            topics_dict["id"].append(comment.id)
            topics_dict["body"].append(comment.body.replace('\r', ' ').replace('\n', ' '))
            # topics_dict["created_utc"].append(comment.created_utc)
            tstamps.append(comment.created_utc)
            topics_dict["score"].append(comment.score)

        tstamps = [get_date(i).isoformat() for i in tstamps]

        for key in topics_dict:
            print(key + " len: " + str(len(topics_dict[key])))

        data = pd.DataFrame(topics_dict)
        data.index = tstamps
        localname = 'comments_' + term + '.csv'
        data.to_csv(os.path.join(abs_out, localname), index=False) 

def get_reddit_submissions(search_terms, subreddits, begin_time, end_time, size, out_dir="../data/reddit/submissions"):
    abs_out = os.path.abspath(out_dir)
    if (not os.path.isdir(abs_out)):
        os.makedirs(abs_out)
    for term in search_terms:
        data = api.search_submissions(q=term, subreddit=subreddits, 
            sort='asc', size=size, after=epoch_time(begin_time), before=epoch_time(end_time),  
            filter=['subreddit', 'title', 'id', 'score', 'body', 'created_utc'])
        topics_dict = { "subreddit":[], 
            "title":[], 
            "score":[], 
            "id":[], 
            #"created_utc": [], 
            "body":[]
        }
        tstamps = []
        for submission in data:
            topics_dict["subreddit"].append(submission.subreddit)
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            tstamps.append(submission.created)
            #topics_dict["created_utc"].append(submission.created)
            #topics_dict["body"].append(submission.selftext)
            topics_dict["body"].append(submission.title.replace('\r', ' ').replace('\n', ' '))
        tstamps = [get_date(i).isoformat() for i in tstamps]
        data = pd.DataFrame(topics_dict)
        data.index = tstamps
        #_timestamp = data["created_utc"].apply(get_date)
        #topics_data = data.assign(timestamp = _timestamp)
        localname = 'submissions_' + term + '.csv'
        data.to_csv(os.path.join(abs_out, localname), index=False) 
