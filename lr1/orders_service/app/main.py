from fastapi import FastAPI
from app.routes.product_routes import router as product_router

app = FastAPI(title="Products API")

app.include_router(product_router, prefix="/products", tags=["Products"])
