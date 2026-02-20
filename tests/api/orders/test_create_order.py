from http.client import responses

import allure
import pytest
import requests

from setting import BASE_URL


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    PATH = "/api/v1/orders"

    @allure.title("Успешное создание заказа без указания цвета")
    def test_create_order_without_color_returns_201(self):

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

        response = requests.post(f"{BASE_URL}{self.PATH}", json=payload)
        body = response.json()

        assert response.status_code == 201
        assert body.get("track") is not None

    @allure.title("Успешное создание заказа c разными цветами")
    @pytest.mark.parametrize("color", [["BLACK"], ['GREY'], ['BLACK', 'GREY']])
    def test_create_order_with_color_returns_201(self, color):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", json=payload)
        body = response.json()

        assert response.status_code == 201
        assert body.get("track") is not None