import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User registration cases")
@allure.issue('https://playground.learnqa.ru')
class TestUserRegister(BaseCase):

    @allure.severity("Critical")
    @allure.title("test_create_user_successfully")
    @allure.testcase("SWT-5694")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post('https://playground.learnqa.ru/api/user', data = data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')


    @allure.tag("negative")
    @allure.title("test_create_user_with_existing_email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)


        response = requests.post('https://playground.learnqa.ru/api/user', data = data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",  f"Unexpected response content {response.content}"

    @allure.tag("negative")
    @allure.title("test_create_user_with_invalid_format_email")
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

    @allure.tag("negative")
    @allure.title("test_create_user_with_existing_params")
    def test_create_user_with_existing_params(self, data):
        response = requests.post('https://playground.learnqa.ru/api/user', data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert "The following required params are missed" in response.content.decode(
            "utf-8"), f"Wrong response content {response.content}"

    @allure.tag("negative")
    @allure.title("test_create_user_with_short_name")
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

    @allure.tag("negative")
    @allure.title("test_create_user_with_long_name")
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
