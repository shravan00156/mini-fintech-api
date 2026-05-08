"""Transaction-related routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("", summary="List transactions")
def list_transactions() -> dict[str, list[dict[str, str]]]:
    """Return a placeholder list of transactions."""
    return {"transactions": []}
