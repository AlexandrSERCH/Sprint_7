import requests
from faker import Faker

from helpers.generate_data import get_login, get_password, get_firstname
from setting import BASE_URL


def register_new_courier_and_return_login_password():
    PATH = '/api/v1/courier'

    payload = {
        "login": get_login(),
        "password": get_password(),
        "firstName": get_firstname()
    }

    response = requests.post(f"{BASE_URL}{PATH}", data=payload)

    if response.status_code == 201:
        return [payload["login"], payload["password"]]
    return None


print(register_new_courier_and_return_login_password())