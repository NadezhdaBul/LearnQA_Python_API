import requests

class TestHeader:
    def test_header(some):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        # print(response.headers) #'x-secret-homework-header': 'Some secret value'
        assert 'x-secret-homework-header' in response.headers, "wrong header"
