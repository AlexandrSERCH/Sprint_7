import allure
import requests

from setting import BASE_URL


@allure.epic("Заказы")
@allure.feature("Принять заказ")
class TestAcceptOrder:

    PATH = "/api/v1/orders/accept/"

    @allure.title("Успешное принятие заказа")
    def test_accept_order_returns_200(self, auth_courier, order_id):

        response = requests.put(f"{BASE_URL}{self.PATH}{order_id}?courierId={auth_courier}")
        body = response.json()

        assert response.status_code == 200
        assert body == {"ok": True}

    @allure.title("Ошибка валидации при отсутствии id курьера")
    def test_accept_order_without_courier_id_returns_400(self, order_id):

        response = requests.put(f"{BASE_URL}{self.PATH}{order_id}?courierId=")
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для поиска"

    @allure.title("Ошибка валидации при невалидном id курьера")
    def test_accept_order_invalid_courier_id_returns_404(self, order_id):

        invalid_courier_id = 123

        response = requests.put(f"{BASE_URL}{self.PATH}{order_id}?courierId={invalid_courier_id}")
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Курьера с таким id не существует"

    @allure.title("Ошибка валидации при отсутствии id заказа")
    def test_accept_order_without_order_id_returns_400(self, auth_courier):

        response = requests.put(f"{BASE_URL}{self.PATH}courierId={auth_courier}")
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для поиска"

    @allure.title("Ошибка валидации при невалидном id заказа")
    def test_accept_order_invalid_order_id_returns_404(self, auth_courier):

        invalid_order_id = 123

        response = requests.put(f"{BASE_URL}{self.PATH}{invalid_order_id}?courierId={auth_courier}")
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Заказа с таким id не существует"

