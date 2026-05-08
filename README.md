# Mini Fintech API

A beginner-friendly learning project to practice **backend engineering** concepts by building a production-style **FastAPI fintech backend**.

## Project Goals

- Learn clean backend architecture fundamentals.
- Build RESTful APIs with FastAPI.
- Organize code in a scalable, professional structure.
- Add fintech-focused features incrementally (accounts, transactions, balances, etc.).

## Current Scope

This initial scaffold includes:

- Core FastAPI app entrypoint.
- Feature-oriented package structure.
- A simple health-check endpoint.
- Dependency list for local development.

> Note: Docker and authentication are intentionally **not added yet**.

## Project Structure

```text
mini-fintech-api/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI application startup and router registration
│   ├── routes/                # API endpoints grouped by feature/domain
│   │   ├── __init__.py
│   │   └── health.py
│   ├── models/                # ORM/database models
│   │   └── __init__.py
│   ├── schemas/               # Pydantic request/response schemas
│   │   └── __init__.py
│   ├── services/              # Business logic layer
│   │   └── __init__.py
│   └── database/              # DB connection/session config and utilities
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open docs:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Next Steps

- Add domain routes (accounts, users, transactions).
- Integrate a real database and migrations.
- Add validation schemas and service-layer logic.
- Introduce authentication and authorization later.
