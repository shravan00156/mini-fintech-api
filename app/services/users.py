"""Business logic for user operations."""

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, payload: UserCreate) -> User:
    """Create and persist a new user."""
    user = User(email=payload.email, full_name=payload.full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session) -> list[User]:
    """Return all users."""
    return db.query(User).all()
