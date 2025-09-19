import pytest
import requests
from helpers import user_data, delete_user
from test_data import Urls

@pytest.fixture
def prepared_user():
    payload = user_data()
    response= requests.post(f"{Urls.base_url}{Urls.api_create_user}", json=payload)
    assert response.status_code == 200
    access_token = response.json()["accessToken"]
    data = {
        "access_token": access_token,
        "login_payload": {'email':payload["email"], 'password': payload["password"]}
    }
    yield data
    delete_user(access_token)

@pytest.fixture
def user_exist_login(prepared_user):
    yield prepared_user['login_payload']

@pytest.fixture
def user_exist_access_token(prepared_user):
    yield prepared_user['access_token']