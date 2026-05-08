from fastapi import FastAPI

from app.routes.transactions import router as transactions_router

app = FastAPI(title="Mini Fintech API")
app.include_router(transactions_router)
