
import pandas as pd 
import numpy as np 

def impute(series):
    mean = series.mean()
    return series.fillna(mean)


def impute_min(series: pd.Series) -> pd.Series:
    return series