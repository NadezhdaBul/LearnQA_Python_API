import requests
import pytest
from lib.base_case import BaseCase
class TestUserAuth (BaseCase):
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    def setup(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data = data)
        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_authmethod = self.get_json_value(response1, 'user_id')

    def test_auth_user (self):
        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token':self.token},
            cookies={'auth_sid':self.auth_sid}
        )

        assert "user_id" in response2.json() , 'не юзер ид во втором респонсе'
        user_id_from_check_method = response2.json()["user_id"]
        print(user_id_from_check_method)

        assert self.user_id_from_authmethod == user_id_from_check_method, "юзер ид в фактическом результате не соответствует ожидаемому результату"