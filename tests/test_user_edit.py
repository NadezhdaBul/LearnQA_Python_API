
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    #REGISTER
    # def test_edit_just_created_user(self):
    #     register_data = self.prepare_registration_data()
    #     response1_1 = requests.post('https://playground.learnqa.ru/api/user', data=register_data)
    #     Assertions.assert_code_status(response1_1, 200)
    #     Assertions.assert_json_has_key(response1_1, 'id')
    #
    #     password = register_data['password']
    #     firstName = register_data['firstName']
    #     email= register_data['email']
    #     user_id = self.get_json_value(response1_1, 'id')
    #
    # #LOGIN
    #     login_data = {
    #         'email' : email,
    #        'password' : password
    #     }
    #     response1_2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
    #     auth_sid = self.get_cookie(response1_2, 'auth_sid')
    #     token = self.get_header(response1_2, 'x-csrf-token')
    #     # print(f"sid {auth_sid}")
    #     # print(token)
    #     # print(email)
    #     # print(password)
    #
    #
    # #EDIT
    #     new_name = 'Changed Name'
    #     response1_3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
    #                              headers={'x-csrf-token': token},
    #                              cookies={'auth_sid': auth_sid},
    #                              data={'firstName': new_name}
    #                              )
    #     Assertions.assert_code_status(response1_3, 200)
    #
    # #GET
    #     response1_4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
    #                  headers={'x-csrf-token': token},
    #                  cookies={'auth_sid': auth_sid}
    #                  )
    #     Assertions.assert_json_value_by_name(response1_4, 'firstName', new_name, "Wrong name of the user after edit")
    #

    def test_edit_not_authorized_user_negative(self):
        email = 'learnqa02072024210315@example.com'
        password = '123'

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2_1 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response2_1, 'auth_sid')
        token = self.get_header(response2_1, 'x-csrf-token')
        user_id = self.get_json_value(response2_1, 'user_id')

        # EDIT
        new_name = 'Changed Wrong Name'
        response2_2 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 data={'firstName': new_name})

        Assertions.assert_code_status(response2_2, 400)
        assert response2_2.content.decode('utf-8') == "Auth token not supplied", f"Unexpected response content {response2_2.content}"


        # GET
        response2_3 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})

        Assertions.assert_json_value_not_expected_name(response2_3, 'firstName', new_name, "Attention! The name has been changed")

#
    def test_edit_email_invalid_format(self):
        email = 'learnqa02072024210315@example.com'
        password = '123'

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3_1 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response3_1, 'auth_sid')
        token = self.get_header(response3_1, 'x-csrf-token')
        user_id = self.get_json_value(response3_1, 'user_id')
        Assertions.assert_code_status(response3_1, 200)

        # EDIT
        new_email = 'ChangedEmailyandexru'
        response3_2 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                   data={'email': new_email})

        Assertions.assert_code_status(response3_2, 400)
        assert response3_2.content.decode(
            'utf-8') == "Auth token not supplied", f"Unexpected response content {response3_2.content}"

        # GET
        response3_3 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid})

        Assertions.assert_code_status(response3_3, 200)
        assert "email" in response3_3.json(), f"No 'email' in response3_3"
        assert response3_3.json()["email"] != new_email, "Attention! The name has been changed"



