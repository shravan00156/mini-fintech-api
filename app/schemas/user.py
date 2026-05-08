"""Pydantic schemas for user endpoints."""

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Payload used to create a new user."""

    email: EmailStr
    full_name: str


class UserResponse(BaseModel):
    """Public response model for user data."""

    id: int
    email: EmailStr
    full_name: str

    model_config = {"from_attributes": True}
