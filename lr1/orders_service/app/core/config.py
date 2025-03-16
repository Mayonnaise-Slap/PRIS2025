import os

from dotenv import load_dotenv

load_dotenv()
USERS_SERVICE_URL = f"http://{os.getenv('USERS_SERVICE_HOST')}:{os.getenv('USERS_SERVICE_PORT')}/users"
PRODUCTS_SERVICE_URL = f"http://{os.getenv('PRODUCTS_SERVICE_HOST')}:{os.getenv('PRODUCTS_SERVICE_PORT')}/products"
