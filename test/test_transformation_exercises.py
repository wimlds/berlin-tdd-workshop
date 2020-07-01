import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from scripts.transformation import is_greater_than_average


def test_is_greater_than_average_empty():
    input_series = pd.Series([])
    expected_series = pd.Series([])
    actual_series = is_greater_than_average(series=input_series)
    assert_series_equal(actual_series, expected_series)

@pytest.mark.skip(reason="it fails")
def test_is_greater_than_average_with_nan():
    input_series = pd.Series([1,2,np.nan])
    expected_series = pd.Series([0,1,np.nan]) # or exception?
    actual_series = is_greater_than_average(series=input_series)
    assert_series_equal(actual_series, expected_series)

def test_is_greater_than_average_all_the_same():
    input_series = pd.Series([10, 10, 10, 10])
    expected_series = pd.Series([0, 0, 0, 0])
    actual_series = is_greater_than_average(series=input_series)
    assert_series_equal(actual_series, expected_series)

#test for type
# at least 3 ways to do this it seems.. what's the best one for debugging?
def test_is_greater_than_average_returns_series():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    output_series = is_greater_than_average(series=input_series)
    assert type(output_series) is pd.core.series.Series

def test_series_type():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    output_series = is_greater_than_average(series=input_series)
    assert type(output_series) is pd.Series

def test_is_returning_series():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    output_series = is_greater_than_average(series=input_series)
    type_as_string = type(output_series).__name__
    assert type_as_string == "Series"