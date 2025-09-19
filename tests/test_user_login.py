import allure
import requests
from test_data import Urls, ResponseBodies, Texts


class TestUserLogin:

    @allure.title("Авторизация под существующим пользователем")
    def test_user_exist_login(self, user_exist_login):
            response = requests.post(f"{Urls.base_url}{Urls.api_auth_user}", json=user_exist_login)
            assert response.status_code == 200
            assert "accessToken" in response.json()

    @allure.title("Авторизация с неверным логином и паролем")
    def test_user_fail_login(self):
        payload = ResponseBodies.wrong_data
        response = requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
        assert response.status_code == 403
        assert response.json()["message"] == Texts.MISSING_FIELD_ERROR_MESSAGE