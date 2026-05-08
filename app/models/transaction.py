"""Transaction ORM model.

This class maps Python attributes to columns in the `transactions` SQL table.
"""

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.database.base import Base


class Transaction(Base):
    """Represents a single financial transaction record."""

    # Table name in the SQLite database.
    __tablename__ = "transactions"

    # Primary key: unique identifier for each row.
    id = Column(Integer, primary_key=True, index=True)

    # Basic transaction fields.
    user = Column(String, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)

    # Server-side default timestamp (set by the database on insert).
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
