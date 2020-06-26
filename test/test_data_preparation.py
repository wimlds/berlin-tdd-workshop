import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from data_preparation import impute_mean, is_greater_than_average

def test_impute_mean():
    #exercise idea: use different arrays
    data = np.array([1, 2, 3, np.nan, 4]) 
    input_series = pd.Series(data)

    output_data = np.array([1, 2, 3, 2.5, 4])
    expected_series = pd.Series(output_data)

    output_series = impute_mean(series=input_series)

    assert_series_equal(output_series, expected_series)

@pytest.mark.skip(reason="comment out when we get here")
def test_is_greater_than_average():

    data = np.array([1, 2, 3, 2.5, 4])
    input_series = pd.Series(data)
    output = np.array([0, 0, 1, 0, 1])
    expected_series = pd.Series(output)

    output_series = is_greater_than_average(series=input_series)

    assert_series_equal(output_series, expected_series)
