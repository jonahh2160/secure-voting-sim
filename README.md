# secure-voting-sim

Simulated Python voting system in which votes are encrypted to protect anonymity and ensure data integrity.

## Goals

- Votes will be encrypted before storage
- Vote tallying should not reveal individual votes
- A simple and accessible GUI for voters

## Skills

- Cryptography
- Data integrity
- GUI design

## Tools

- Python
- PyCryptodome
- CustomTkinter

## Build / Run

Prerequisites
- Python 3.8+ installed and on your PATH
- A terminal (PowerShell on Windows)

Recommended quick steps (Windows PowerShell)

1. Open PowerShell and change to the project directory:

```powershell
Set-Location 'C:\Users\David\OneDrive\Documents\GitHub\csc455-vote-project\secure-voting-sim'
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
# Activate the venv in PowerShell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies (a `requirements.txt` is provided):

```powershell
python -m pip install --upgrade pip
pip install -r .\requirements.txt
```

If you prefer to install directly without `requirements.txt`:

```powershell
pip install customtkinter pycryptodome
```

4. Run the app (entry point is `main.py`):

```powershell
python .\main.py
```

You should see a printed election tally similar to:

```
Election Results: {'Candidate A': 1, 'Candidate B': 1}
```

Notes and troubleshooting
- Ensure `python` points to a Python 3.x interpreter. If not, use `python3` or the full path to the executable.
- `customtkinter` requires a working Tkinter installation (usually included with the standard Windows Python installer).
- If pip install fails for `customtkinter`, try a specific version or check PyPI for the package name.
- Consider pinning dependency versions in `requirements.txt` for reproducible installs.

Optional follow-ups
- Add a short "Build / Run" section to this README (done).
- Pin package versions in `requirements.txt`.
- Add a tiny smoke test script or a CI job to validate installs and a successful run.
