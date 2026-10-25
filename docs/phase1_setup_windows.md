# Phase 1 — Windows Development Environment Setup

Follow these steps in order. Each step ends with a **check** — don't move on until it passes.

## 1. Install the tools

| Tool | Why | Install |
|---|---|---|
| **Python 3.12** | Language for the whole project. 3.12 has the widest library support in 2026. | https://www.python.org/downloads/windows/ → tick **"Add python.exe to PATH"** during install. Or: `winget install Python.Python.3.12` |
| **Git** | Version control | https://git-scm.com/download/win (defaults are fine; choose VS Code as editor). Or: `winget install Git.Git` |
| **VS Code** | Editor | https://code.visualstudio.com/ Or: `winget install Microsoft.VisualStudioCode` |
| **DB Browser for SQLite** (optional) | Look inside `.db` files visually | `winget install DBBrowserForSQLite.DBBrowserForSQLite` |

Open a **new** PowerShell window after installing (so PATH updates), then check:

```powershell
py -3.12 --version     # Python 3.12.x
git --version          # git version 2.x
code --version         # prints a version
```

VS Code extensions (Ctrl+Shift+X): **Python**, **Pylance**, **Jupyter**, **Ruff**, **GitLens** (optional), **SQLite Viewer** (optional).

## 2. Configure Git (one time)

```powershell
git config --global user.name "Jamal"
git config --global user.email "your-github-email@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true     # Windows line endings handled for you
```

Check: `git config --global --list` shows your name and email.

## 3. Get the project

```powershell
mkdir $HOME\projects -Force
cd $HOME\projects
git clone https://github.com/<your-username>/enterprise-ai-decision-intelligence.git
cd enterprise-ai-decision-intelligence
```

The first push/pull will open a browser window to sign in to GitHub (Git Credential Manager). Never paste tokens into files.

## 4. Create a virtual environment

A virtual environment (`.venv`) is a private folder of packages just for this project, so versions here never clash with other projects.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell says *"running scripts is disabled"*, run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Check: your prompt starts with `(.venv)` and `python -c "import sys; print(sys.prefix)"` prints a path ending in `.venv`.

## 5. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

`-e` = "editable": your `src/edip` code is importable everywhere, and edits take effect immediately.

## 6. Verify everything

```powershell
pytest              # expect: 11 passed
ruff check src tests
jupyter lab         # opens the browser; run notebooks/01_intro_data_analysis.ipynb top to bottom
```

In VS Code: `code .` → Ctrl+Shift+P → **Python: Select Interpreter** → pick `.venv`.

## 7. Your first commit

```powershell
git checkout -b phase-1-setup
# make a small change, e.g. complete an exercise in the notebook
git add .
git commit -m "chore: complete Phase 1 environment setup"
git push -u origin phase-1-setup
```

Then open a Pull Request on GitHub and merge it into `main`. Working on branches + PRs is how professional teams work, and it shows on your GitHub history.

## Common mistakes

- Installing packages **without** the venv active → they go to global Python. Always look for `(.venv)`.
- Committing `.venv/` or data files → `.gitignore` already blocks them; don't force-add.
- Having several Pythons and `python` pointing to the Microsoft Store stub → use `py -3.12` to create the venv.
- Running notebooks out of order → before committing, use **Kernel → Restart & Run All**.

## Acceptance criteria for setup

- [ ] `pytest` shows 11 passed on your machine
- [ ] Notebook 01 runs top to bottom with Restart & Run All
- [ ] You made a commit on a branch, pushed it, and merged a PR
