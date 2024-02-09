import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User authorization cases")
@allure.issue('https://playground.learnqa.ru')
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

    @allure.severity("Critical")
    @allure.title("test_authorization_user_successfully")
    @allure.testcase("SWT-2253")
    def test_auth_user (self):
        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token':self.token},
            cookies={'auth_sid':self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_authmethod,
            "User id from auth method is not equal from user id chek method"
        )

        # assert "user_id" in response2.json() , 'не юзер ид во втором респонсе'
        # user_id_from_check_method = response2.json()["user_id"]
        # print(user_id_from_check_method)
        #
        # assert self.user_id_from_authmethod == user_id_from_check_method, "юзер ид в фактическом результате не соответствует ожидаемому результату"

    @pytest.mark.parametrize('condition', exclude_params)

    @allure.tag("negative")
    @allure.title("test_negative_auth_check")
    def test_negative_auth_check(self, condition):
        if condition == "no cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token":self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is outhorized with condition {condition}"
        )
