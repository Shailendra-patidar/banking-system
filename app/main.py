from fastapi import FastAPI

from app.routes.customer_routes import router as customer_router
from app.routes.account_routes import router as account_router

app = FastAPI(title="Banking System")

app.include_router(customer_router)
app.include_router(account_router)


@app.get("/")
def home():
    return {"message": "Banking System API is running"}