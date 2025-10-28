[![CI](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)](#)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#)
[![Cloud Run](https://img.shields.io/badge/cloud--run-ready-brightgreen)](#)


# AI-Assisted Hypothesis Explorer

**Stack:** FastAPI + Streamlit + (optional) LangChain/OpenAI

## Local (two terminals)
Backend:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.api:app --host 0.0.0.0 --port 8000
```

Frontend:
```bash
source .venv/bin/activate
streamlit run frontend/streamlit_app.py
```
Open http://localhost:8501

## Docker Compose
```bash
docker compose up
```

## Optional Env
- OPENAI_API_KEY, OPENAI_MODEL (backend)
- API_URL (frontend)


## Screenshots
![App Screenshot](docs/screenshots/screenshot.png)
