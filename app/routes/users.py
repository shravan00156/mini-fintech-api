from fastapi import APIRouter

# Router for user-related endpoints.
router = APIRouter()


@router.get("/users")
def list_users() -> dict:
    # Returns a simple placeholder response for user listing.
    return {"message": "Users endpoint is working"}
