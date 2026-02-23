import allure
import pytest
import requests

from constants import CREATE_ORDER_URL


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Успешное создание заказа без указания цвета")
    def test_create_order_without_color_returns_201(self, order_data):

        response = requests.post(f"{CREATE_ORDER_URL}", json=order_data)
        body = response.json()

        assert response.status_code == 201
        assert body.get("track") is not None

    @allure.title("Успешное создание заказа c разными цветами")
    @pytest.mark.parametrize("color", [["BLACK"], ['GREY'], ['BLACK', 'GREY']])
    def test_create_order_with_color_returns_201(self, color, order_data):

        order_data["color"] = color

        response = requests.post(f"{CREATE_ORDER_URL}", json=order_data)
        body = response.json()

        assert response.status_code == 201
        assert body.get("track") is not None