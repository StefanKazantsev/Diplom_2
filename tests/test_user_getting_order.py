import allure
import requests
from test_data import Urls, Texts
from helpers import user_data


class TestGettingOrder:

    @allure.title("Получение заказов конкретного авторизованного пользователя")
    def test_get_order_user_auth(self, user_exist_access_token):
        headers = {
            'Authorization': f'{user_exist_access_token}'
        }
        response = requests.get(f"{Urls.base_url}{Urls.api_get_order_user}", headers=headers)
        assert response.status_code == 200
        assert "orders" in response.json()

    @allure.title("Получение заказов не авторизованного пользователя")
    def test_get_order_user_non_auth(self):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(f"{Urls.base_url}{Urls.api_get_order_user}", headers=headers)
        assert response.status_code == 401
        assert response.json()["message"] == Texts.NON_AUTORAZATION_ERROR_MESSAGE