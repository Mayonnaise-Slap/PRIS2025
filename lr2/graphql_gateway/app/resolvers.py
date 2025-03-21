import requests
from ariadne import QueryType
from config import USERS_SERVICE_URL, PRODUCTS_SERVICE_URL, ORDERS_SERVICE_URL

query = QueryType()

@query.field("getUser")
def resolve_get_user(_, info, id):
    response = requests.get(f"{USERS_SERVICE_URL}/users/{id}")
    return response.json() if response.status_code == 200 else None

@query.field("listUsers")
def resolve_list_users(_, info):
    response = requests.get(f"{USERS_SERVICE_URL}/users/")
    return response.json() if response.status_code == 200 else []

@query.field("getProduct")
def resolve_get_product(_, info, id):
    response = requests.get(f"{PRODUCTS_SERVICE_URL}/products/{id}")
    return response.json() if response.status_code == 200 else None

@query.field("listProducts")
def resolve_list_products(_, info):
    response = requests.get(f"{PRODUCTS_SERVICE_URL}/products/")
    return response.json() if response.status_code == 200 else []

@query.field("getOrder")
def resolve_get_order(_, info, id):
    order = requests.get(f"{ORDERS_SERVICE_URL}/orders/{id}").json()
    if "user_id" in order and "product_id" in order:
        order["user"] = requests.get(f"{USERS_SERVICE_URL}/users/{order['user_id']}").json()
        order["product"] = requests.get(f"{PRODUCTS_SERVICE_URL}/products/{order['product_id']}").json()
    return order

@query.field("listOrders")
def resolve_list_orders(_, info):
    response = requests.get(f"{ORDERS_SERVICE_URL}/orders/")
    return response.json() if response.status_code == 200 else []
