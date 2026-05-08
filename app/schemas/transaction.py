"""Pydantic schemas for transaction endpoints."""

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    """Payload used to add a transaction."""

    user_id: int
    amount: float
    category: str


class TransactionResponse(BaseModel):
    """Public response model for transaction data."""

    id: int
    user_id: int
    amount: float
    category: str

    model_config = {"from_attributes": True}
