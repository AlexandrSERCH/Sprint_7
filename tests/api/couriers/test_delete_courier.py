import allure
import requests

from setting import BASE_URL


@allure.epic("Курьер")
@allure.feature("Удаление курьера")
class TestDeleteCourier:

    PATH = "/api/v1/courier/"

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_returns_200(self, auth_courier):

        response = requests.delete(f"{BASE_URL}{self.PATH}{auth_courier}")
        body = response.json()

        assert response.status_code == 200
        assert body == {'ok': True}

    @allure.title("Ошибка валидации при удалении курьера без id")
    def test_delete_courier_without_id_returns_400(self):

        response = requests.delete(f"{BASE_URL}{self.PATH}")
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для удаления курьера"

    @allure.title("Ошибка валидации при удалении курьера c невалидным id")
    def test_delete_courier_with_invalid_id_retutns_404(self):

        invalid_id = 123987

        response = requests.delete(f"{BASE_URL}{self.PATH}{invalid_id}")
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Курьера с таким id нет."
