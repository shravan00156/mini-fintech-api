"""User route module.

This module keeps user-related endpoints separate so the project stays
clean and easy to extend.
"""

from fastapi import APIRouter

# This router groups all user endpoints under a single module.
router = APIRouter(tags=["users"])


@router.get("/users")
def list_users() -> dict:
    """Return a simple placeholder list of users."""
    return {
        "message": "User route is working.",
        "users": [],
    }
