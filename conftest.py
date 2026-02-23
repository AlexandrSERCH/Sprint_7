import pytest
import requests

from data.order_data import get_order_data
from helpers.generate_data import get_login, get_password, get_firstname
from constants import COURIER_URL, LOGIN_COURIER_URL, CREATE_ORDER_URL, TRACK_ORDER_URL

@pytest.fixture
def courier_data():
    data = {
        "login": get_login(),
        "password": get_password(),
    }

    yield data

    response = requests.post(f"{LOGIN_COURIER_URL}", data=data)
    body = response.json()
    courier_id = body.get("id")

    if courier_id is not None:
        requests.delete(f"{COURIER_URL}/{courier_id}")

@pytest.fixture
def order_data():
    return get_order_data()

@pytest.fixture
def registered_courier():
    payload = {
        "login": get_login(),
        "password": get_password(),
        "firstName": get_firstname()
    }

    response = requests.post(f"{COURIER_URL}", data=payload)

    if response.status_code == 201:
        login = payload["login"]
        password = payload["password"]

        yield {"login": login, "password": password}

    response = requests.post(f"{LOGIN_COURIER_URL}", data=payload)
    body = response.json()
    courier_id = body.get("id")

    if courier_id is not None:
        requests.delete(f"{COURIER_URL}/{courier_id}")


@pytest.fixture
def auth_courier(registered_courier):

    payload = {
        "login": registered_courier["login"],
        "password": registered_courier["password"]
    }

    response = requests.post(f"{LOGIN_COURIER_URL}", data=payload)
    body = response.json()
    courier_id = body.get("id")

    yield courier_id

    if courier_id is not None:
        requests.delete(f"{COURIER_URL}/{courier_id}")

@pytest.fixture
def created_order(order_data):

    response = requests.post(f"{CREATE_ORDER_URL}", json=order_data)
    body = response.json()

    if response.status_code == 201:
        return {"id": body["track"]}
    return None

@pytest.fixture
def order_id(created_order):

    response = requests.get(f"{TRACK_ORDER_URL}?t={created_order["id"]}")
    body = response.json()

    if response.status_code == 200:
        return body["order"]["id"]
    return None

