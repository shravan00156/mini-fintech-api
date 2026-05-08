"""Transaction API routes."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services import transactions as transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("", response_model=TransactionResponse)
def create_transaction(payload: TransactionCreate, db: Session = Depends(get_db)) -> TransactionResponse:
    """Create a transaction record."""
    return transaction_service.create_transaction(db, payload)


@router.get("", response_model=list[TransactionResponse])
def list_transactions(db: Session = Depends(get_db)) -> list[TransactionResponse]:
    """List all transactions."""
    return transaction_service.list_transactions(db)
