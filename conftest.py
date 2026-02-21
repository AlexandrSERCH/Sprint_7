import pytest
import requests

from helpers.generate_data import get_login, get_password, get_firstname
from setting import BASE_URL

@pytest.fixture
def registered_courier():
    PATH = '/api/v1/courier'

    payload = {
        "login": get_login(),
        "password": get_password(),
        "firstName": get_firstname()
    }

    response = requests.post(f"{BASE_URL}{PATH}", data=payload)

    if response.status_code == 201:
        login = payload["login"]
        password = payload["password"]
        return {"login": login, "password": password}
    return None

@pytest.fixture
def auth_courier(registered_courier):
    PATH = "/api/v1/courier/login"

    payload = {
        "login": registered_courier["login"],
        "password": registered_courier["password"]
    }

    response = requests.post(f"{BASE_URL}{PATH}", data=payload)
    body = response.json()
    courier_id = body["id"]

    yield courier_id

    requests.delete(f"{BASE_URL}{PATH}/{auth_courier}")

@pytest.fixture
def created_order():
    PATH = "/api/v1/orders"

    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }

    response = requests.post(f"{BASE_URL}{PATH}", json=payload)
    body = response.json()

    if response.status_code == 201:
        return {"id": body["track"]}
    return None

@pytest.fixture
def order_id(created_order):

    PATH = "/api/v1/orders/track"

    response = requests.get(f"{BASE_URL}{PATH}?t={created_order["id"]}")
    body = response.json()

    if response.status_code == 200:
        return body["order"]["id"]
    return None

