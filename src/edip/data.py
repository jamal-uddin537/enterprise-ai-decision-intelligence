"""Data loading helpers.

Phase 1 uses the Wine dataset that ships inside scikit-learn, so no download
is needed. Source: UCI Machine Learning Repository, "Wine" (Aeberhard &
Forina, 1991), CC BY 4.0. https://archive.ics.uci.edu/dataset/109/wine
"""

from __future__ import annotations

import sqlite3

import pandas as pd
from sklearn.datasets import load_wine


def load_wine_frame() -> pd.DataFrame:
    """Return the Wine data as a DataFrame with a readable `cultivar` column."""
    bunch = load_wine(as_frame=True)
    df = bunch.frame.rename(columns={"target": "cultivar"})
    df["cultivar"] = df["cultivar"].map(lambda i: f"cultivar_{i}")
    return df


def to_sqlite(df: pd.DataFrame, table: str, conn: sqlite3.Connection) -> None:
    """Write a DataFrame to a SQLite table (replacing it if it exists)."""
    df.to_sql(table, conn, if_exists="replace", index=False)


def run_query(sql: str, conn: sqlite3.Connection) -> pd.DataFrame:
    """Run a read-only SQL query and return the result as a DataFrame."""
    if not sql.lstrip().lower().startswith(("select", "with")):
        raise ValueError("Only SELECT / WITH queries are allowed here")
    return pd.read_sql_query(sql, conn)
