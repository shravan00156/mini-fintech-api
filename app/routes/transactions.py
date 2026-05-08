from fastapi import APIRouter

from app.schemas.transaction import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/")
def create_transaction(payload: TransactionCreate):
    # FastAPI validates payload against TransactionCreate before this function runs.
    # Returning the parsed model data keeps the endpoint simple for beginners.
    return {
        "message": "Transaction accepted",
        "transaction": payload.model_dump(),
    }
