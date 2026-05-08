from fastapi import APIRouter

# Router for transaction-related endpoints.
router = APIRouter()


@router.get("/transactions")
def list_transactions() -> dict:
    # Returns a simple placeholder response for transaction listing.
    return {"message": "Transactions endpoint is working"}
