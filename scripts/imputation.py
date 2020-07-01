
import pandas as pd 
import numpy as np 



def impute(series):
    mean_val = series.mean()
    return series.fillna(mean_val)


# EXERCISE 1 - solutions

def impute_min(series: pd.Series) -> pd.Series:
    min_val = series.min()
    return series.fillna(min_val)

def impute_with_max(series):
    mx = series.max()
    return series.fillna(mx)