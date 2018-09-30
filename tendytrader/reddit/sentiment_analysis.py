from TextBlob import TextBlob
import os
from pandas import DataFrame

# kwargs: num_posts, subreddit,
def average_sentiment(term, **kwargs):
    # There is also polarity
    sum_polarity = 0.0
    sum_sentiment = 0.0
    abs_in = os.path.abspath('../data/reddit/')
    pd = read_csv(os.path.join(abs_in, term + '.csv'))
    if 'subreddit' in kwargs:
        for i, sr in pd['subreddit'] 
            if sr != kwargs['subreddit']
                pd.drop(i) 

    for body in pd['body']:
        text = TextBlob(body)
        # Tokenize
        if 'num_posts' in kwargs:
            for i, sentence in enumerate(text.sentences):
                st = TextBlob(sentence)
                if i >= kwargs['num_posts']-1:
                    break
                sum_polarity, sum_sentiment += st.sentiment
        else:
            for sentence in text.sentences:
                st = TextBlob(sentence)
                sum_polarity, sum_sentiment += st.sentiment

            
