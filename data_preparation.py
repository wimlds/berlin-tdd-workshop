import pandas as pd 
import numpy as np 

def impute_mean(series: pd.Series) :
    mean = series.mean()
    return series.fillna(mean)



