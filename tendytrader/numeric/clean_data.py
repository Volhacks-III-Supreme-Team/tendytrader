import pandas as pd
import numpy as np

def clean_stock_nan(data):
    nans = np.where(np.asarray(np.isnan(data)))
    nans = np.array(nans)
    col_labels = data.columns.values.tolist()
    row_labels = list(data.index)
    for row, col in nans.T:
        rlabel = row_labels[row]
        clabel = col_labels[col]
        e0 = row-1
        e1 = row+1
        if e0 < 0:
            e0 = row+2
        if e1 >= len(data.index):
            e1 = row-2
        while np.isnan(data.loc[row_labels[e0], clabel]):
            e0 -= 1
        while np.isnan(data.loc[row_labels[e1], clabel]):
            e1 += 1
            if e1 >= len(row_labels):
                e1 = 0
            if e1 == e0:
                break
        e0 = row_labels[e0]
        e1 = row_labels[e1]
        data.loc[rlabel, clabel] = (data.loc[e0, clabel]+data.loc[e1, clabel]) / 2
