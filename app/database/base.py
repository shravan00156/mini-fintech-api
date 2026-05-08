"""Declarative Base class for SQLAlchemy models.

All future ORM models should inherit from `Base`.
That keeps table metadata in one shared registry.
"""

from sqlalchemy.orm import declarative_base

# Base is the parent class for all database models.
# Example later:
# class User(Base):
#     __tablename__ = "users"
#     ...
Base = declarative_base()
