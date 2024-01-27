import requests
class TestCookies:
    def test_cookie(some):

        response =requests.get("https://playground.learnqa.ru/api/homework_cookie")
        # print(response.cookies) #<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqa.ru/>]>
        assert 'HomeWork' in response.cookies, 'wrong cookies'
