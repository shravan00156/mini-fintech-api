from fastapi import FastAPI

from app.routes.transactions import router as transactions_router
from app.routes.users import router as users_router

app = FastAPI(title="Mini Fintech API")


@app.get("/")
def root() -> dict:
    # Root route for quick API discovery.
    return {"message": "Welcome to Mini Fintech API"}


@app.get("/health")
def health_check() -> dict:
    # Basic health-check route to confirm the backend is running.
    return {"status": "ok"}


# Register the transactions and users routers.
app.include_router(transactions_router)
app.include_router(users_router)
