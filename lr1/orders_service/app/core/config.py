import os

USERS_SERVICE_URL = f"http://{os.getenv('USERS_SERVICE_HOST')}:8000/users"
PRODUCTS_SERVICE_URL = f"http://{os.getenv('PRODUCTS_SERVICE_HOST')}:8000/products"
