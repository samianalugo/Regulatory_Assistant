# Regulatory Report Assistant — Frontend

This repository contains a React frontend that works with a FastAPI backend to process mini regulatory report assistant, extract structured fields (drug, adverse events, severity, outcome), display results, keep history, and translate outcomes.

This file README adds setup details, API examples, database notes, and test instructions so you can run the full stack locally, but i forgot to take screenshots of installing dependencies.

## Repo layout (relevant parts)

- `Backend/` — FastAPI backend (Python)
- `frontend/` — React app (this folder)
- `reports.db` — SQLite DB (created by the backend in `Backend/reports.db`)

## Prerequisites

- Node.js + npm (for frontend)
- Python 3.10+ (for backend)


## Quick start (recommended)

1. Start the backend API

Windows (cmd.exe):

```cmd
cd C:\Users\DELL\Desktop\Regulatory_Assistant\Backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

 (bash):

```bash
cd ~/Desktop/Regulatory_Assistant/Backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Notes:
- The backend automatically creates/initializes the SQLite DB (`Backend/reports.db`) when started.
- If you see CORS errors in the browser, confirm the backend is running on the expected host/port (default is 127.0.0.1:8000).

2. Start the frontend

```bash
cd C:\Users\DELL\Desktop\Regulatory_Assistant\frontend
npm install
npm start
```

The React app will open in your browser (usually http://localhost:3000) and call the backend at http://127.0.0.1:8000 by default.

## Backend API (endpoints)

- POST /process-report
   - Request JSON: { "report": "<text>" }
   - Response JSON: { "id": int, "drug": str, "adverse_events": [str], "severity": str, "outcome": str }

- GET /reports
   - Response JSON: [ { "id": int, "report_text": str, "drug": str, "adverse_events": [str], "severity": str, "outcome": str, "created_at": str }, ... ]

- POST /translate
   - Request JSON: { "outcome": "recovered", "lang": "fr" }
   - Supported langs: `fr`, `sw`
   - Response JSON: { "original": "recovered", "lang": "fr", "translated": "rétabli" }

## Example curl (Windows cmd)

Process a report:

```cmd
curl -X POST http://127.0.0.1:8000/process-report -H "Content-Type: application/json" -d "{\"report\":\"Patient took DrugX and experienced nausea and recovered\"}"
```

Translate outcome:

```cmd
curl -X POST http://127.0.0.1:8000/translate -H "Content-Type: application/json" -d "{\"outcome\":\"recovered\",\"lang\":\"fr\"}"
```

## Database notes

- The backend uses SQLite and creates `Backend/reports.db` automatically when the app starts.
- If you want to reset the DB, stop the backend and delete `Backend/reports.db`.

## Tests (backend)

Run tests from the `Backend/` folder using pytest:

```bash
cd Backend
.venv\Scripts\activate   # windows
pytest -q
```

The repository contains unit tests for the extractors, database logic and an end-to-end pipeline test.

## Troubleshooting

- AttributeError: 'NoneType' object has no attribute 'cursor'
   - Ensure the backend was started (`uvicorn main:app ...`) so the DB is initialized. The backend code initializes the DB on import/start.
- CORS issues in browser
   - Confirm frontend and backend hosts/ports match what the frontend expects, or update the allowed origins in `Backend/main.py`.

## Development notes

- Backend code is in `Backend/` (FastAPI). Key files:
   - `main.py` — fastapi app + router registration
   - `database.py` — sqlite connection and init
   - `crud.py` — DB helpers for saving and reading reports
   - `extractors.py` — text extraction logic
- Frontend components are in `frontend/src/components/`.

