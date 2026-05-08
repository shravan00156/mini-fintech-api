"""Helpers for creating database tables."""

from app.database.base import Base
from app.database.session import engine
from app.models import transaction, user  # noqa: F401 (import for table registration)


def create_tables() -> None:
    """Create database tables for all imported models."""
    Base.metadata.create_all(bind=engine)
