"""Database connection setup for the FastAPI application.

This module is intentionally beginner-friendly:
- one place to define the SQLite URL
- one engine object shared by the app
- one SessionLocal factory used in routes/services
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database URL format:
# sqlite:///./<filename>
# The leading ./ means "create the file in the project root directory".
SQLALCHEMY_DATABASE_URL = "sqlite:///./fintech.db"

# The engine is SQLAlchemy's core interface to the database.
# For SQLite, check_same_thread=False allows usage across different
# request-handling threads in FastAPI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# SessionLocal is a "session factory".
# Each database operation should use a new session instance created by:
# db = SessionLocal()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
