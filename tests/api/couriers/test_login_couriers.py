import allure
import pytest
import requests

from setting import BASE_URL


@allure.epic("Курьер")
@allure.feature("Авторизация курьера")
class TestLoginCouriers:

    PATH = "/api/v1/courier/login"

    @allure.title("Успешая авторизация курьера")
    def test_login_courier_returns_200_and_id(self, registered_courier):

        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 200
        assert body.get("id") is not None

    @allure.title("Ошибка валидации при отсутствии поля 'login'")
    def test_login_courier_without_login_returns_400(self):

        payload = {
            "password" : "123"
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка валидации при отсутствии поля 'password'")
    def test_login_courier_without_password_returns_400(self):

        payload = {
            "login" : "user"
        }

        try:
            response = requests.post(f"{BASE_URL}{self.PATH}", data=payload, timeout=5)
            body = response.json()
        except:
            pytest.fail("Превышено время ожидания: 5 секунд")

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка валидации при невалидном логине")
    def test_login_courier_invalid_login_returns_404(self):

        payload = {
            "login": "inval1d_l0g1n",
            "password": "123"
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка валидации при невалидном пароле")
    def test_login_courier_invalid_login_returns_404(self):

        payload = {
            "login": "alex_29",
            "password": "123zxc098"
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 404
        assert body["message"] == "Учетная запись не найдена"