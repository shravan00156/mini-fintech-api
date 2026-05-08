"""Database setup for SQLAlchemy ORM.

This module defines:
- the SQLite engine (connection to `fintech.db`)
- the session factory used by the app
- the declarative Base class all ORM models inherit from
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLAlchemy database URL for a local SQLite file.
# `./fintech.db` means the file will live at the project root.
DATABASE_URL = "sqlite:///./fintech.db"

# Engine manages low-level DB connections.
# `check_same_thread=False` is needed for SQLite when used by FastAPI.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# SessionLocal creates one ORM session per request/task.
# A Session tracks objects and writes changes to the DB.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class for all ORM models.
# Inheriting from Base tells SQLAlchemy a class maps to a table.
Base = declarative_base()
