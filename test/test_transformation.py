import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from scripts.transformation import is_greater_than_average



@pytest.mark.skip(reason="comment out when we get here")
def test_is_greater_than_average():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    expected_series = pd.Series([0, 0, 1, 0, 1])

    output_series = is_greater_than_average(series=input_series)

    assert_series_equal(output_series, expected_series)
