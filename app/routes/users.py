"""User-related routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", summary="List users")
def list_users() -> dict[str, list[dict[str, str]]]:
    """Return a placeholder list of users."""
    return {"users": []}
