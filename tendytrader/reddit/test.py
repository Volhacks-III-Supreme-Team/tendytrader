import datetime as dt
import time
from praw_get import reddit_get_comments, reddit_get_submissions
payload = {'q' : 'subreddit:wallstreetbets flair:\"Daily Discussion\"',
'limit': '100',
'sort' : 'new',
't' : 'month'}

# See reddit api for d

# reddit_get_comments('subreddit:wallstreetbets flair:\"Daily Discussion\"', \
        # date_begin, date_end, 'test')

reddit_get_comments(payload, 'test')