import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from scripts.imputation import impute

def test_impute_one_value():
    data = pd.Series([1.0, np.nan, 3.0])    # 1. Define some input data
    expected = pd.Series([1.0, 2.0, 3.0])   # 2. Define what is expected to happen
    actual = impute(data)  				  	       # 3. Run function and record what happens 
    assert_series_equal(expected, actual)   # 4. Make sure expected and actual are equal

    

def test_impute_two_values():
    #exercise idea: use different arrays
    data = np.array([1, 2, 3, np.nan, 4, np.nan]) 
    input_series = pd.Series(data)

    output_data = np.array([1, 2, 3, 2.5, 4, 2.5])
    expected_series = pd.Series(output_data)

    output_series = impute(series=input_series)

    assert_series_equal(output_series, expected_series)


# add a happy test 
# how could your function be misused, edge cases
