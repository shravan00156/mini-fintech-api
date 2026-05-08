from pydantic import BaseModel, Field, field_validator


class TransactionCreate(BaseModel):
    """Schema for creating a new transaction from incoming JSON."""

    user: str = Field(..., min_length=1, description="Username who owns the transaction")
    amount: float = Field(..., description="Transaction amount; must be greater than 0")
    type: str = Field(..., min_length=1, description="Transaction type, for example: deposit or withdrawal")

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value: float) -> float:
        # We only allow positive amounts to prevent invalid transactions.
        if value <= 0:
            raise ValueError("Amount must be greater than 0")
        return value
