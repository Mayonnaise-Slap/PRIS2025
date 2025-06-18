from fastapi import FastAPI
from api.user_routes import router as user_router

app = FastAPI(title="Users API")

app.include_router(user_router, prefix="/users", tags=["Users"])
