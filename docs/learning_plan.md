# Learning Plan & Timeline

## Starting assessment (25 Oct 2026)

| Area | Question | Result |
|---|---|---|
| Python | List comprehension with a filter | Correct |
| SQL | `HAVING` vs `WHERE` for aggregated filters | Correct |
| Statistics / ML | Accuracy on a 1%-positive imbalanced problem | Correct |
| Git | add → commit → push | Correct |

**Reading:** solid fundamentals across all four. Phase 1 is therefore a *fast review* (1–2 weeks), focusing on the gaps intermediate learners usually have: packaging (`src/` layout, editable installs), testing with pytest, window functions/CTEs, confidence intervals, and branch/PR workflow.

Pending: one more self-check on statistics depth — be ready to explain a p-value and a 95% confidence interval in one sentence each (we'll do this in the Phase 1 review).

## Timeline (assumes ~10–12 hours/week)

| Weeks | Phase | Main outcome |
|---|---|---|
| 1–2 | 1. Foundations | Environment, notebook 01, tests passing, first PR |
| 3 | 2. Dataset selection | Dataset comparison report + data dictionary |
| 4–5 | 3. Data engineering | Ingestion, validation, SQLite DB, data quality report |
| 6–7 | 4. EDA | EDA notebook, hypothesis tests, dashboard prototype |
| 8–10 | 5. Machine learning | Baselines, CV, tuning, SHAP, evaluation report |
| 11–12 | 6. Advanced ML | Forecasting, anomaly detection, calibration, honest comparisons |
| 13–15 | 7. GenAI & RAG | Grounded assistant with citations + retrieval evaluation |
| 16–17 | 8. Agentic AI | Read-only multi-agent workflow with audit log |
| 18–20 | 9. Application | Streamlit + FastAPI app |
| 21–22 | 10. MLOps | MLflow, Docker, CI, monitoring, deployment |
| 23 | 11. Portfolio | README, screenshots, demo video |
| 24 | 12. Career | Review score, resume bullets, interview prep |

About **6 months** part-time. Full-time study can roughly halve this. Slipping a week is normal — quality beats speed.

## Phase 1 study list (by topic)

1. **Python** — functions, type hints, modules/packages, exceptions, f-strings, comprehensions. Exercise: read `src/edip/stats.py` and explain every line.
2. **NumPy** — arrays, vectorisation, broadcasting, `axis`, boolean masks.
3. **Pandas** — `loc`/`iloc`, `groupby().agg()`, `merge`, `pivot_table`, missing values, dtypes.
4. **Visualisation** — Matplotlib (control), Seaborn (statistical plots), Plotly (interactive).
5. **SQL** — SELECT → JOIN → GROUP BY/HAVING → CTEs → window functions. Practice in `sql/01_sql_practice.sql`.
6. **Git/GitHub** — branches, PRs, `.gitignore`, meaningful commit messages (`feat:`, `fix:`, `docs:`, `test:`).
7. **Statistics** — mean/median/std, distributions, standard error, confidence intervals, hypothesis tests, p-values, correlation vs causation.
8. **Tooling** — venv, `pyproject.toml`, pytest, ruff, VS Code + Jupyter.
