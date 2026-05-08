"""User API routes."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import users as user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    """Create a user account."""
    return user_service.create_user(db, payload)


@router.get("", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    """List all users."""
    return user_service.list_users(db)
