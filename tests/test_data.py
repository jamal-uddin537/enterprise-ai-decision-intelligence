import sqlite3

import pytest

from edip.data import load_wine_frame, run_query, to_sqlite


@pytest.fixture
def wine():
    return load_wine_frame()


def test_wine_shape_and_no_missing(wine):
    assert wine.shape == (178, 14)
    assert wine.isna().sum().sum() == 0


def test_cultivar_labels(wine):
    assert set(wine["cultivar"]) == {"cultivar_0", "cultivar_1", "cultivar_2"}


def test_sql_group_by_matches_pandas(wine):
    conn = sqlite3.connect(":memory:")
    to_sqlite(wine, "wine", conn)
    sql_counts = run_query(
        "SELECT cultivar, COUNT(*) AS n FROM wine GROUP BY cultivar ORDER BY cultivar", conn
    )
    pandas_counts = wine["cultivar"].value_counts().sort_index()
    assert sql_counts["n"].tolist() == pandas_counts.tolist()


def test_run_query_blocks_writes(wine):
    conn = sqlite3.connect(":memory:")
    to_sqlite(wine, "wine", conn)
    with pytest.raises(ValueError):
        run_query("DELETE FROM wine", conn)
