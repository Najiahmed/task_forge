from fastapi import FastAPI
from routers import tasks

app = FastAPI(title="TaskForge API")

app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "Welcome to TaskForge"}
