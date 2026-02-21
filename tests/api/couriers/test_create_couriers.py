import allure
import requests

from helpers.generate_data import get_login, get_password, get_firstname
from setting import BASE_URL


@allure.epic("Курьер")
@allure.feature("Cоздание курьера")
class TestCreateCouriers:

    PATH = '/api/v1/courier'

    @allure.title("Успешное создание курьера")
    def test_create_courier_return_201(self):

        payload = {
            "login": get_login(),
            "password": get_password(),
            "firstName": get_firstname()
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)

        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title("Запрет на создание дубпиката курьера")
    def test_create_duplicate_couriers_returns_409(self, registered_courier):

        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 409
        assert "Этот логин уже используется" in body["message"]
        # 'in' использовал, т.к. ошибка в ТЗ.
        # ФР = Этот логин уже используется
        # а ОР из доки = Недостаточно данных для создания учетной записи

    @allure.title("Ошибка валидации при отсутствии обязательно поля 'login'")
    def test_create_couriers_without_login_returns_400(self):

        payload = {
            "password": get_password(),
            "firstName": get_firstname()
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка валидации при отсутствии обязательно поля 'password'")
    def test_create_couriers_without_password_returns_400(self):

        payload = {
            "login": get_login(),
            "firstName": get_firstname()
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка валидации при отсутствии обязательно поля 'firstname'")
    def test_create_couriers_without_firstname_returns_400(self):

        payload = {
            "login": get_login(),
            "password": get_password()
        }

        response = requests.post(f"{BASE_URL}{self.PATH}", data=payload)
        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для создания учетной записи"
        # в ТЗ для поля "firstName" нет отметки "необязательный" как в других полях
