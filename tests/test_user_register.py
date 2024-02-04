import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    emails = [
        ('vinkotov@example.com'),
        ('vinkotovexample.com')
    ]

    @pytest.mark.parametrize('email', emails)
    def test_create_user_with_existing_email(self, email):

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


    datas = [
        ({"'password': '123','username': 'leanqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'qwerty@example.com'"}),
        ({"'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'qwerty@example.com'"}),
        ("'password': '123', 'username': 'leanqa','lastName': 'learnqa', 'email': 'qwerty@example.com'"),
        ("'password': '123', 'username': 'leanqa', 'firstName': 'learnqa', 'email': 'qwerty@example.com'"),
        ("'password': '123','username': 'leanqa', 'firstName': 'learnqa', 'lastName': 'learnqa'")
    ]
    #
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
