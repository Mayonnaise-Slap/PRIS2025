from fastapi import FastAPI
from routes.order_routes import router as order_routes

app = FastAPI(title="Orders API")

app.include_router(order_routes, prefix="/orders", tags=["Orders"])
