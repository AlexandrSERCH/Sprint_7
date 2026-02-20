import allure
import requests

from setting import BASE_URL


@allure.epic("Курьер")
@allure.feature("Удаление курьера")
class TestDeleteCourier:

    PATH = "/api/v1/courier/"

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_returns_200(self):
        courier_id = 123

        response = requests.delete(f"{BASE_URL}{self.PATH}/{courier_id}")
        print(response.status_code)
        print(response.json())

        #
        #  ПРОДОЛЖИТЬ РЕАЛИЗОВЫВАТЬ ТЕСТ
        #