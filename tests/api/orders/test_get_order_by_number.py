import allure
import requests

from setting import BASE_URL


@allure.epic("Заказы")
@allure.feature("Получить заказ по номеру")
class TestGetOrderByNumber:

    PATH = "/api/v1/orders/track"

    @allure.title("Успешное получение заказа по его номеру")
    def test_get_order_by_number_returns_200(self, created_order):

        response = requests.get(f"{BASE_URL}{self.PATH}?t={created_order["id"]}")
        body = response.json()

        assert response.status_code == 200
        assert body["order"]["id"] is not None

    @allure.title("Ошибка валидации при получении заказа без передачи номера")
    def test_get_order_by_number_without_track_returns_400(self, created_order):

        response = requests.get(f"{BASE_URL}{self.PATH}?t=")
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для поиска"

    @allure.title("Ошибка валидации при получении заказа с несуществующим номером")
    def test_get_order_by_number_nonexistent_track_returns_404(self, created_order):

        nonexistent_track = 101290

        response = requests.get(f"{BASE_URL}{self.PATH}?t={nonexistent_track}")
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Заказ не найден"