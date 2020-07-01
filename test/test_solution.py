
import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

from scripts.transformation import is_greater_than_average

@pytest.mark.skip(reason="comment out when we get here")
def test_is_returning_series():
    input_series = pd.Series([1, 2, 3, 2.5, 4])
    output_series = is_greater_than_average(series=input_series)

    type_as_string = type(output_series).__name__
    assert type_as_string == "Series"