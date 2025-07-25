from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "Dashboard Review API",
    description = "Submit and store reviews for the uploaded dashboards with text or file.",
    version = "1.0.0"
)

app.include_router(router)