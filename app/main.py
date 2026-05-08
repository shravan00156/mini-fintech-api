"""Main FastAPI application entrypoint.

Run locally with:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.routes.health import router as health_router

# Create one FastAPI app instance for the whole backend.
# This object is what Uvicorn imports and serves.
app = FastAPI(
    title="Mini Fintech API",
    description="Beginner-friendly FastAPI backend structure.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint used as a quick connectivity check."""
    return {
        "message": "Mini Fintech API is running",
        "docs": "/docs",
    }


# Register feature routers on the main app.
# This keeps main.py small while allowing scalable route modules.
app.include_router(health_router)
