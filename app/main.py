from fastapi import FastAPI

from app.routes.customer_routes import router as customer_router


app = FastAPI(title="Banking System")

app.include_router(customer_router)


@app.get("/")
def home():
    return {"message": "Banking System API is running"}