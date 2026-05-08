"""Transaction route module.

This module keeps transaction-related endpoints separate so the app can
scale as more transaction APIs are added.
"""

from fastapi import APIRouter

# This router groups all transaction endpoints under a single module.
router = APIRouter(tags=["transactions"])


@router.get("/transactions")
def list_transactions() -> dict:
    """Return a simple placeholder list of transactions."""
    return {
        "message": "Transaction route is working.",
        "transactions": [],
    }
