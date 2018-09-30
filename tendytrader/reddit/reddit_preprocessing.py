import os
import datetime

def get_day_terms(terms, day_begin):
    abs_in = os.path.abspath('../data/reddit/')
    pd = read_csv(os.path.join(abs_in, term + '.csv'))
