"""Health-check route(s) used for quick service verification."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Simple health endpoint to confirm the API is running."""
    return {"status": "ok"}
