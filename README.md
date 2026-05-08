# Mini Fintech API

A beginner-friendly, production-style backend learning project built with **FastAPI**.

## Project Goals

- Learn clean backend architecture for fintech-style APIs.
- Practice scalable folder organization used in real projects.
- Start simple (no Docker/auth yet) and expand feature by feature.

## Project Structure

```text
app/
├── main.py                # FastAPI app entrypoint
├── routes/                # API endpoints grouped by domain
├── models/                # ORM/database models
├── schemas/               # Pydantic request/response models
├── services/              # Business logic layer
└── database/              # Database setup and helpers
```

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open docs:
   - Swagger UI: `http://127.0.0.1:8000/docs`

## Current Scope

- ✅ Clean starter structure
- ✅ FastAPI app bootstrapped
- ✅ Health-check route example
- ⏳ Authentication (planned later)
- ⏳ Docker setup (planned later)
