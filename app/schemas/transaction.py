"""Pydantic schemas for transaction API payloads."""

from pydantic import BaseModel, Field, field_validator


class TransactionCreate(BaseModel):
    """Schema for creating a new transaction from request JSON."""

    user: str
    amount: float = Field(..., description="Transaction amount. Must be greater than 0.")
    type: str

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, value: float) -> float:
        """Reject zero or negative amounts so invalid transactions are blocked."""
        if value <= 0:
            raise ValueError("amount must be greater than 0")
        return value
