import pandas as pd
import numpy as np
import warnings
from pandas import Series, datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import os
import pickle as pkl

def generate_models(ticks, out_dir="./data/numeric"):
    abs_out = os.path.abspath(out_dir)
    if not os.path.isdir(abs_out):
        raise OSError("Could not find directory {}".format(abs_out))
    if type(ticks) is str:
        ticks = [ticks]
    for t in ticks:
        fname = os.path.join(abs_out, t + ".csv")
        merged_data = pd.read_csv(fname)
        merged_data = merged_data.drop(columns="ticker")
        
        from preprocessing import gen_label_data

        gen_label_data(merged_data)
        X = merged_data.iloc[:, :-1]
        X = X.drop(columns="Close")
        Y = merged_data.loc[:, 'label']
        x_train, x_test, y_train, y_test = train_test_split(X, Y)
        x_train = x_train.values
        x_test = x_test.values
        y_train = y_train.values
        y_test = y_test.values
        x_train = x_train[:, 1:]; x_test = x_test[:, 1:]
        model = XGBClassifier()
        n_estimators = [150, 200, 250, 350, 450, 500, 550, 750, 1000, 1100, 1250, 1350, 1500]
        max_depth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        best_depth = 0
        best_estimator = 0
        max_score = 0
        for n in n_estimators:
            for md in max_depth:
                model = XGBClassifier(n_estimators=n, max_depth=md)
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                score = accuracy_score(y_test, y_pred)
                if score > max_score:
                    max_score = score
                    best_depth = md
                    best_estimator = n
        xgb = XGBClassifier(n_estimators=best_estimator, max_depth=best_depth)
        xgb.fit(x_train, y_train)
        abs_mod = os.path.abspath("./models")
        if not os.path.isdir(abs_mod):
            os.mkdir(abs_mod)
        pkl.dump(xgb, open(os.path.join(abs_mod, t + ".dat"), "wb+"))

def predict(tick, stock_data, input_dir="./models"):
    abs_in = os.path.abspath(input_dir)
    if not os.path.isdir(abs_in):
        raise OSError("Could not find directory {}".format(abs_in))
    fname = os.path.join(abs_in, tick + ".dat")
    print(fname)
    assert os.path.exists(fname)
    model = pkl.load(open(fname, "rb"))
    print(type(model))
    return model.predict(stock_data)
