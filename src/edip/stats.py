"""Small, hand-written statistics helpers used in Phase 1.

They are deliberately simple so you can read every line, then check them
against NumPy/SciPy in the tests.
"""

from __future__ import annotations

import math
from collections.abc import Sequence

from scipy import stats as sp_stats


def mean(values: Sequence[float]) -> float:
    """Arithmetic mean: sum of values divided by how many there are."""
    if len(values) == 0:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)


def sample_std(values: Sequence[float]) -> float:
    """Sample standard deviation (divides by n - 1, 'Bessel's correction').

    We divide by n - 1 instead of n because the sample mean is itself
    estimated from the same data, which makes squared deviations slightly
    too small on average. Dividing by n - 1 corrects that bias in the variance.
    """
    n = len(values)
    if n < 2:
        raise ValueError("sample_std() needs at least two values")
    m = mean(values)
    squared_deviations = [(x - m) ** 2 for x in values]
    return math.sqrt(sum(squared_deviations) / (n - 1))


def mean_confidence_interval(
    values: Sequence[float], confidence: float = 0.95
) -> tuple[float, float]:
    """Confidence interval for the population mean using the t-distribution.

    interval = mean ± t* × (s / √n)
      - s / √n is the standard error: how much the sample mean would vary
        from sample to sample.
      - t* is the critical value from Student's t with n - 1 degrees of freedom.
    """
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    n = len(values)
    m = mean(values)
    standard_error = sample_std(values) / math.sqrt(n)
    t_critical = sp_stats.t.ppf((1 + confidence) / 2, df=n - 1)
    margin = t_critical * standard_error
    return (m - margin, m + margin)
