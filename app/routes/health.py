"""Health-check routes.

This module is a simple example of how to keep API endpoints organized by domain.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", summary="Health check")
def health_check() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok"}
