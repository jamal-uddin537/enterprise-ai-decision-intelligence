import numpy as np
import pytest
from scipy import stats as sp_stats

from edip.stats import mean, mean_confidence_interval, sample_std

VALUES = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]


def test_mean_matches_numpy():
    assert mean(VALUES) == pytest.approx(np.mean(VALUES))


def test_sample_std_matches_numpy_ddof1():
    assert sample_std(VALUES) == pytest.approx(np.std(VALUES, ddof=1))


def test_confidence_interval_matches_scipy():
    low, high = mean_confidence_interval(VALUES, 0.95)
    expected = sp_stats.t.interval(
        0.95, df=len(VALUES) - 1, loc=np.mean(VALUES), scale=sp_stats.sem(VALUES)
    )
    assert (low, high) == pytest.approx(expected)


def test_interval_contains_mean():
    low, high = mean_confidence_interval(VALUES)
    assert low < mean(VALUES) < high


@pytest.mark.parametrize("bad", [[], [1.0]])
def test_sample_std_rejects_short_input(bad):
    with pytest.raises(ValueError):
        sample_std(bad)


def test_confidence_must_be_between_0_and_1():
    with pytest.raises(ValueError):
        mean_confidence_interval(VALUES, confidence=1.5)
