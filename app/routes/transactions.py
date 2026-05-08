"""Transaction routes for the FastAPI app."""

from fastapi import APIRouter

from app.schemas.transaction import TransactionCreate

router = APIRouter(tags=["transactions"])


@router.post("/transactions")
def create_transaction(transaction: TransactionCreate):
    """Create a transaction and return the validated request payload."""
    # FastAPI validates `transaction` with Pydantic before this function runs.
    # If the amount is invalid (<= 0), FastAPI returns a 422 validation error.
    return {
        "message": "Transaction accepted",
        "transaction": transaction.model_dump(),
    }
