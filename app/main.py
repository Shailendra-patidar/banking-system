from fastapi import FastAPI

app = FastAPI(title="Banking System")


@app.get("/")
def home():
    return {"message": "Banking System API is running"}