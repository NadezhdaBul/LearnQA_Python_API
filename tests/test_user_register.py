import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'leanqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post('https://playground.learnqa.ru/api/user', data = data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",  f"Unexpected response content {response.content}"

    def test_create_user_with_invalid_format_email(self):
        email = 'vinkotovexample.com'
        data = {
            'password': '123',
            'username': 'leanqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post('https://playground.learnqa.ru/api/user', data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == 'Invalid email format', f"The email {email} format is correct"


    @pytest.mark.parametrize('data', [
        ({'username': 'leanqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'qwerty@example.com'}),
        ({'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'qwerty@example.com'}),
        ({'password': '123', 'username': 'learnqa','lastName': 'learnqa', 'email': 'qwerty@example.com'}),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'qwerty@example.com'}),
        ({'password': '123','username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'})
    ])
    def test_create_user_with_existing_params(self, data):
        response = requests.post('https://playground.learnqa.ru/api/user', data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The following required params are missed" in response.content.decode(
            "utf-8"), f"Wrong response content {response.content}"

    def test_create_user_with_short_name(self):
        username = "u"
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'Vjivinkotov@example.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user', data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The value of 'username' field is too short" in response.content.decode('utf-8'), f"Unexpected user registration result for username {username}"

    def test_create_user_with_long_name(self):
        username = "Asdfghjklqwertyuiopzxcvbnm1234567890987654321qwedcxAsdfghjklqwertyuiopzxcvbnm1234567890987654321qwedcxAsdfghjklqwertyuiopzxcvbnm1234567890987654321qwedcxAsdfghjklqwertyuiopzxcvbnm1234567890987654321qwedcxAsdfghjklqwertyuiopzxcvbnm1234567890987654321qwedcx"
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'Vrjivinkotov@example.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user', data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The value of 'username' field is too long" in response.content.decode('utf-8'), f"Unexpected user registration result for username {username}"
