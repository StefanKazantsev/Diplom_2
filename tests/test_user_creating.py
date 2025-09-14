import allure
import requests
from test_data import Urls
from helpers import user_data


class TestUserCreating:

    @allure.title("Создание нового пользователя")
    def test_user_registration(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Cоздать зарегистрированного пользователя")
    def test_user_exist_registration(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 200
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert "User already exists" in response.json()["message"]

    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    def test_user_exist_registration(self):
        payload = user_data()
        payload.pop("email")
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert "Email, password and name are required fields" in response.json()["message"]