import allure
import requests

from setting import BASE_URL


@allure.epic("Заказы")
@allure.feature("Получение заказов")
class TestGetOrders:

    PATH = "/api/v1/orders"

    @allure.title("Получить список заказов")
    def test_get_orders_returns_200(self):

        response = requests.get(f"{BASE_URL}{self.PATH}")
        body = response.json()
        print(body)

        assert response.status_code == 200
        assert body.get("orders") is not None