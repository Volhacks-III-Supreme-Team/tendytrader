from textblob import TextBlob
import os
from pandas import DataFrame, read_csv

# kwargs: num_posts, subreddit,
def average_sentiment(term_df, comments=True, **kwargs):
    # There is also polarity
    sum_polarity = 0.0
    sum_sentiment = 0.0
    num = 0
    '''
    if comments:
        abs_in = os.path.abspath('../data/reddit/comments')
        pd = read_csv(os.path.join(abs_in, 'comments_' + term + '.csv'))
    else:
        abs_in = os.path.abspath('../data/reddit/submissions')
        pd = read_csv(os.path.join(abs_in, 'submissions_' + term + '.csv'))
    '''
    if 'subreddit' in kwargs:
        for i, sr in term_df['subreddit']:
            if sr != kwargs['subreddit']:
                term_df.drop(i) 

    for body in term_df['body']:
        text = TextBlob(body)
        # Tokenize
        if 'num_posts' in kwargs:
            for i, sentence in enumerate(text.sentences):
                st = TextBlob(sentence)
                if i >= kwargs['num_posts']-1:
                    break
                sent = st.sentiment
                sum_polarity += sent[0]; sum_sentiment += sent[1]
                num += 1
        else:
            for sentence in text.sentences:
                sent = sentence.sentiment
                sum_polarity += sent[0]; sum_sentiment += sent[1]
                num += 1
    avg_polarity = sum_polarity / num
    avg_sentiment = sum_sentiment / num
    return avg_polarity, avg_sentiment, num
