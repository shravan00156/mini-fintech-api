"""Application entrypoint for the Mini Fintech API."""

from fastapi import FastAPI

from app.routes.health import router as health_router

app = FastAPI(
    title="Mini Fintech API",
    description="Starter FastAPI backend for a beginner-friendly fintech project.",
    version="0.1.0",
)

# Register API route groups.
app.include_router(health_router)
