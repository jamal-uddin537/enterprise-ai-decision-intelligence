# Enterprise AI Data Analyst & Decision Intelligence Platform

An end-to-end analytics and machine learning platform, built step by step as a learning portfolio project: data validation, SQL, statistics, dashboards, predictive models, forecasting, a document-grounded AI assistant (RAG), controlled AI agents, and a deployed web app with MLOps.

> **Status:** Phase 1 (Environment & Foundations) — in progress. See [docs/progress_tracker.md](docs/progress_tracker.md).
> No results, metrics or business conclusions are reported yet. They will be added only after the code has actually been run.

## Problem statement

Business teams hold data in spreadsheets and databases but lack a single, trustworthy place to validate it, explore it, predict outcomes and ask questions in plain English. This project builds that place, with every number traceable to code and source data.

## Planned architecture

```
Public dataset ──► Ingestion & validation ──► SQL database (SQLite → PostgreSQL)
                                                  │
              ┌───────────────┬──────────────────┼───────────────────┐
              ▼               ▼                  ▼                   ▼
          EDA & stats     ML models         Forecasting /       RAG assistant
          (notebooks)     (scikit-learn,    anomaly detection   (embeddings +
                          LightGBM, SHAP)                       vector store)
              └───────────────┴────────┬─────────┴───────────────────┘
                                       ▼
                     Agent workflow (read-only tools, audit log)
                                       ▼
                 FastAPI backend ◄──► Streamlit app  ──► Docker ──► Cloud
                                       ▲
                          MLflow · pytest · GitHub Actions · monitoring
```

## Repository layout

```
enterprise-ai-decision-intelligence/
├── data/
│   ├── raw/          # original downloads — never edited (git-ignored)
│   └── processed/    # outputs of the pipeline (git-ignored)
├── docs/             # setup guide, learning plan, progress tracker
├── notebooks/        # numbered, reproducible notebooks
├── reports/figures/  # exported charts
├── sql/              # SQL practice and analysis queries
├── src/edip/         # reusable Python package
├── tests/            # pytest tests
├── pyproject.toml    # project metadata + dependencies
└── requirements.txt  # pinned-ish install list for pip users
```

## Quick start (Windows, PowerShell)

Full instructions: [docs/phase1_setup_windows.md](docs/phase1_setup_windows.md).

```powershell
git clone https://github.com/<your-username>/enterprise-ai-decision-intelligence.git
cd enterprise-ai-decision-intelligence
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
jupyter lab
```

## Data

Phase 1 uses the **Wine** dataset bundled with scikit-learn (originally from the UCI Machine Learning Repository, licensed CC BY 4.0) purely to practise tools. The main business dataset will be chosen and documented in Phase 2.

## Roadmap

| Phase | Topic | Status |
|---|---|---|
| 1 | Environment & foundations | In progress |
| 2 | Dataset selection | Pending |
| 3 | Data engineering | Pending |
| 4 | Exploratory data analysis | Pending |
| 5 | Machine learning | Pending |
| 6 | Advanced ML | Pending |
| 7 | Generative AI & RAG | Pending |
| 8 | Agentic AI | Pending |
| 9 | Application development | Pending |
| 10 | MLOps & deployment | Pending |
| 11 | Portfolio polish | Pending |
| 12 | Career & interview prep | Pending |

## License

Code: MIT (see [LICENSE](LICENSE)). Datasets keep their original licenses.
