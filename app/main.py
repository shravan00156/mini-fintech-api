"""Application entrypoint for the Mini Fintech API."""

from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.transactions import router as transactions_router
from app.routes.users import router as users_router

app = FastAPI(
    title="Mini Fintech API",
    description="Starter FastAPI backend for a beginner-friendly fintech project.",
    version="0.1.0",
)

# Register API route groups.
app.include_router(health_router)
app.include_router(users_router)
app.include_router(transactions_router)
