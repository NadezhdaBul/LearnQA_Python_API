import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User deleting cases")
@allure.issue('https://playground.learnqa.ru')
class TestUserDelete(BaseCase):

    @allure.severity("normal")
    @allure.title("test_delete_user_number_2")
    @allure.testcase("SWT-9001")
    def test_delete_user_number_2(self):
        #LOGIN
        login_data = {
            'email' : 'vinkotov@example.com',
            'password' : '1234'
        }
        response1_1 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response1_1, 'auth_sid')
        token = self.get_header(response1_1, 'x-csrf-token')
        Assertions.assert_code_status(response1_1, 200)


        #DELETE
        user_id = 2
        response1_2 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                             headers={'x-csrf-token': token},
                             cookies={'auth_sid': auth_sid}
                             )

        Assertions.assert_code_status(response1_2, 400)
        assert 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.' in response1_2.content.decode('utf-8'), f"Deleting user {user_id} is not correct"

        # #GET
        response1_3 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                 headers={'x-csrf-token': token},
                 cookies={'auth_sid': auth_sid}
                 )
        Assertions.assert_code_status(response1_3, 200)
        expected_fields = ["id", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response1_3, expected_fields)
        assert response1_3.json()['id'] == '2', "Wrong user id info"

    @allure.severity("normal")
    @allure.title("test_delete_just_created_user")
    @allure.testcase("SWT-9002")
    def test_delete_just_created_user(self):
        #REGISTER

        register_data = self.prepare_registration_data()
        response2_1 = requests.post('https://playground.learnqa.ru/api/user', data=register_data)
        Assertions.assert_code_status(response2_1, 200)
        Assertions.assert_json_has_key(response2_1, 'id')

        password = register_data['password']
        email= register_data['email']
        user_id = self.get_json_value(response2_1, 'id')

        #LOGIN
        login_data = {
            'email' : email,
            'password' : password
        }
        response2_2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response2_2, 'auth_sid')
        token = self.get_header(response2_2, 'x-csrf-token')


        # DELETE
        response1_2 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                                  headers={'x-csrf-token': token},
                                  cookies={'auth_sid': auth_sid}
                                  )

        Assertions.assert_code_status(response1_2, 200)

        assert response2_2.json()["user_id"] == int(user_id), f"The wrong user {user_id} was deleted"


        #GET
        response2_3 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                               headers={'x-csrf-token': token},
                               cookies={'auth_sid': auth_sid}
                               )
        Assertions.assert_code_status(response2_3, 404)
        assert response2_3.content.decode('utf-8') == 'User not found', f"The user {user_id} has not been deleted"

    @allure.severity("normal")
    @allure.epic("FLACKY test")
    @allure.title("test_delete_other_user")
    @allure.testcase("SWT-9004")
    def test_delete_other_user(self):
        # REGISTER

        register_data = self.prepare_registration_data()
        response2_1 = requests.post('https://playground.learnqa.ru/api/user', data=register_data)
        Assertions.assert_code_status(response2_1, 200)
        Assertions.assert_json_has_key(response2_1, 'id')

        password = register_data['password']
        email = register_data['email']
        user_id = self.get_json_value(response2_1, 'id')


        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response3_1 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response3_1, 'auth_sid')
        token = self.get_header(response3_1, 'x-csrf-token')
        # user_id = self.get_json_value(response3_1, 'id')

        Assertions.assert_code_status(response3_1, 200)

        # REGISTER ANOTHER USER

        register_data2 = self.prepare_registration_data()
        response3_2 = requests.post('https://playground.learnqa.ru/api/user', data=register_data2)
        Assertions.assert_code_status(response3_2, 200)
        Assertions.assert_json_has_key(response3_2, 'id')

        another_user_id = self.get_json_value(response3_2, 'id')


        #DELETE

        # print(f"id залогированного:  {user_id}")
        # print(f"id удаляемого:  {another_user_id}")
        response3_3 = requests.delete(f"https://playground.learnqa.ru/api/user/{another_user_id}",
                                      headers={'x-csrf-token': token},
                                      cookies={'auth_sid': auth_sid}
                                      )

        Assertions.assert_code_status(response3_3, 400)
        # print(f"респонс контент: {response3_3.content}") # b''
        #
        # print(f"респонс код: {response3_3.status_code}") # 200


        # Если авторизовываться под id = 2, то получаем ошибку  'Please, do not delete test users with ID 1, 2, 3, 4 or 5.' in response1_2.content.decode(
        #     'utf-8'), как если бы указанный в делит запросе id не обрабатывался, а удаление происходило на основании указанного
        #     токена и куков - то есть удаление самого авторизованного пользователя, игнорируя указанный id


         #GET проверка авторизованного пользователя (на предмет удаления)

        response3_4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                   headers={'x-csrf-token': token},
                                   cookies={'auth_sid': auth_sid}
                                   )
        # print(response3_4.content) # b'User not found'   Залогированный пользователь удален, указанный delete
        # ид другого пользователя проигнорирован

        # Дальнейшие ассерты теряют смысл
        Assertions.assert_code_status(response3_4, 200)
        expected_fields = ["id", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response3_4, expected_fields)
        assert response3_4.json()['id'] == str(user_id), "Wrong user id info"
