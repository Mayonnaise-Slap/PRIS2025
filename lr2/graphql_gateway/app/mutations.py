import requests
from ariadne import MutationType
from config import USERS_SERVICE_URL, PRODUCTS_SERVICE_URL, ORDERS_SERVICE_URL

mutation = MutationType()

# User Mutations
@mutation.field("createUser")
def resolve_create_user(_, info, name, email):
    response = requests.post(f"{USERS_SERVICE_URL}/users/", json={"name": name, "email": email})
    return response.json() if response.status_code == 201 else None

@mutation.field("updateUser")
def resolve_update_user(_, info, id, name=None, email=None):
    response = requests.put(f"{USERS_SERVICE_URL}/users/{id}", json={"name": name, "email": email})
    return response.json() if response.status_code == 200 else None

@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    response = requests.delete(f"{USERS_SERVICE_URL}/users/{id}")
    return response.status_code == 204

# Product Mutations
@mutation.field("createProduct")
def resolve_create_product(_, info, name, description, price):
    response = requests.post(f"{PRODUCTS_SERVICE_URL}/products/", json={"name": name, "description": description, "price": price})
    return response.json() if response.status_code == 201 else None

@mutation.field("updateProduct")
def resolve_update_product(_, info, id, name=None, description=None, price=None):
    response = requests.put(f"{PRODUCTS_SERVICE_URL}/products/{id}", json={"name": name, "description": description, "price": price})
    return response.json() if response.status_code == 200 else None

@mutation.field("deleteProduct")
def resolve_delete_product(_, info, id):
    response = requests.delete(f"{PRODUCTS_SERVICE_URL}/products/{id}")
    return response.status_code == 204

# Order Mutations
@mutation.field("createOrder")
def resolve_create_order(_, info, user_id, product_id, quantity, status):
    response = requests.post(f"{ORDERS_SERVICE_URL}/orders/", json={"user_id": user_id, "product_id": product_id, "quantity": quantity, "status": status})
    return response.json() if response.status_code == 201 else None

@mutation.field("updateOrder")
def resolve_update_order(_, info, id, user_id=None, product_id=None, quantity=None, status=None):
    response = requests.put(f"{ORDERS_SERVICE_URL}/orders/{id}", json={"user_id": user_id, "product_id": product_id, "quantity": quantity, "status": status})
    return response.json() if response.status_code == 200 else None

@mutation.field("deleteOrder")
def resolve_delete_order(_, info, id):
    response = requests.delete(f"{ORDERS_SERVICE_URL}/orders/{id}")
    return response.status_code == 204
