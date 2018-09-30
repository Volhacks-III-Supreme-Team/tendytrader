from get_reddit import get_reddit_submissions, get_reddit_comments
from reddit_preprocessing import split_by_day
from sentiment_analysis import average_sentiment

get_reddit_submissions(["AMD"], "wallstreetbets", 100)
average_sentiment("AMD", )