import pandas as pd 
import numpy as np 



#fix this!
def is_greater_than_average(series: pd.Series) -> pd.Series:
    avg = series.mean()
    new_series = [0 if x <= avg else 1 for x in series]

    return new_series


def get_sum_score_by_brand_and_gender(frame: pd.DataFrame, brand_col="brand", gender_col="menWomen", score_by="size_greater_than_average") -> pd.DataFrame :
    aggr = frame.groupby(by=[brand_col, gender_col],as_index=False)[score_by].sum()

    return aggr