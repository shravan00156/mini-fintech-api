"""Health check routes."""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Simple service liveness endpoint."""
    return {"status": "ok"}
