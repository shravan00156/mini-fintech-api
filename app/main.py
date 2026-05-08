"""Main FastAPI application entry point."""

from fastapi import FastAPI

from app.routes.transactions import router as transactions_router
from app.routes.users import router as users_router

app = FastAPI(title="Mini Fintech API")


@app.get("/")
def root() -> dict:
    """Basic welcome endpoint for quick API checks."""
    return {"message": "Welcome to the Mini Fintech API"}


@app.get("/health")
def health_check() -> dict:
    """Health endpoint used to confirm that the API is running."""
    return {"status": "ok"}


# Register modular routers so route files stay clean and scalable.
app.include_router(transactions_router)
app.include_router(users_router)
