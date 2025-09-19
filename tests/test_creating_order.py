import allure
import requests
from test_data import Urls, ResponseBodies,Texts


class TestCreatingOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_auth(self, user_exist_access_token):
        headers = {
            'Authorization': f'{user_exist_access_token}'
        }
        payload = ResponseBodies.test_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload, headers=headers)
        assert response.status_code == 200
        assert "name" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_non_auth(self):
        payload = ResponseBodies.test_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == Texts.NON_AUTORAZATION_ERROR_MESSAGE

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_non_ingredient(self):
        payload = ResponseBodies.non_ingredients
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == Texts.NON_INGRIDIENTS_ERROR_MESSAGE

    @allure.title("Создание заказа c неверным хэшом")
    def test_create_order_fake_hash(self):
        payload = ResponseBodies.non_hash_ingredient
        response = requests.post(f"{Urls.base_url}{Urls.api_make_order}", json=payload)
        assert response.status_code == 500