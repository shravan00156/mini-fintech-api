from fastapi import APIRouter

from app.schemas.transaction import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/")
def create_transaction(payload: TransactionCreate):
    """Create a transaction using validated request body data."""
    # FastAPI + Pydantic validate payload before this function runs.
    # If amount is invalid, FastAPI automatically returns a validation error response.
    return {
        "message": "Transaction created successfully",
        "transaction": payload.model_dump(),
    }
