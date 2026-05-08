"""Business logic for transaction operations."""

from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate


def create_transaction(db: Session, payload: TransactionCreate) -> Transaction:
    """Create and persist a new transaction."""
    item = Transaction(user_id=payload.user_id, amount=payload.amount, category=payload.category)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_transactions(db: Session) -> list[Transaction]:
    """Return all transactions."""
    return db.query(Transaction).all()
