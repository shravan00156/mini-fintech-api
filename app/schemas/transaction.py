from pydantic import BaseModel, Field, field_validator


class TransactionCreate(BaseModel):
    """Schema for incoming transaction requests."""

    user: str
    amount: float = Field(..., description="Transaction amount. Must be greater than 0.")
    type: str

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: float) -> float:
        # Reject zero or negative numbers so invalid transactions fail early.
        if value <= 0:
            raise ValueError("amount must be greater than 0")
        return value
