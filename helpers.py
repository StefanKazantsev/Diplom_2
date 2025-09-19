import random
import string
import requests
from test_data import Urls


def random_email():
    email = f"test_{''.join(random.choices(string.ascii_lowercase, k=6))}@yandex.ru"
    return email


def random_name():
    name = f"Test User {''.join(random.choices(string.ascii_letters, k=4))}"
    return name


def random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return password


def user_data():
    data = {
        "email": random_email(),
        "password": random_password(),
        "name": random_name()
    }
    return data

def delete_user(access_token):
    response = requests.delete(f"{Urls.base_url}{Urls.api_delete_user}", headers={'authorization': access_token})
    assert response.status_code == 202, 'не удалось удалить пользователя'

