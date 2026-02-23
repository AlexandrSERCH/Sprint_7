import allure
import requests

from constants import GET_ORDER_URL


@allure.epic("Заказы")
@allure.feature("Получение заказов")
class TestGetOrders:

    @allure.title("Получить список заказов")
    def test_get_orders_returns_200(self):

        response = requests.get(f"{GET_ORDER_URL}")
        body = response.json()

        assert response.status_code == 200
        assert body.get("orders") is not None