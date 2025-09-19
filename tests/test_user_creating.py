import allure
import requests
import pytest
from test_data import Urls, Texts
from helpers import user_data, random_name, delete_user


class TestUserCreating:

    @allure.title("Создание нового пользователя")
    def test_user_registration(self):
        payload = user_data()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()
        delete_user(response.json()['accessToken'])

    @allure.title("Cоздать зарегистрированного пользователя")
    def test_user_exist_registration(self, user_exist_login):
        payload = user_exist_login
        payload['name'] = random_name()
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert response.json()["message"] == Texts.USER_ALREADY_EXISTS_ERROR_MESSAGE


    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    @pytest.mark.parametrize("missing_field_name", ["name", "email", "password"])
    def test_user_exist_registration_without_one_field(self, missing_field_name):
        payload = user_data()
        payload.pop(missing_field_name)
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert response.json()["message"] == Texts.MISSING_FIELD_ERROR_MESSAGE