import allure
import requests
import pytest
from test_data import Urls, Texts
from helpers import random_name, random_email, random_password


class TestUserDataUpdating:

    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("field_name, field_new_value", [
        ("name", random_name()),
        ("email", random_email()),
    ])
    def test_user_data_update_auth(self, user_exist_access_token, field_name, field_new_value):
        headers = {
            'Authorization': f'{user_exist_access_token}'
        }
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={field_name: field_new_value}, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"][field_name] == field_new_value


    @allure.title("Изменение пароля пользователя с авторизацией")
    def test_user_data_password_update_auth(self, user_exist_access_token):
        headers = {
            'Authorization': f'{user_exist_access_token}'
        }
        new_password = random_password()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"password": new_password}, headers=headers)
        assert response.status_code == 200

    @allure.title("Изменение имени пользователя без авторизацией")
    def test_user_data_name_update_non_auth(self):
        headers = {
            "Content-Type": "application/json"
        }
        new_name = random_name()
        response = requests.patch(f"{Urls.base_url}{Urls.api_update_data_user}", json={"name": new_name}, headers=headers)
        assert response.status_code == 401
        assert response.json()["message"] == Texts.NON_AUTORAZATION_ERROR_MESSAGE