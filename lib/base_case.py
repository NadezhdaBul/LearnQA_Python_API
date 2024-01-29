import json.decoder

from requests import Response
class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"не найдены куки с именем {cookie_name} в последнем респонсе"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"не найден заголовок с именем {headers_name} в последнем респонсе"
        return  response.headers[headers_name]

    def get_json_value (self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Респонс не в формате json. Текст респонса '{response.text}'"
        assert name in response_as_dict, f"В респонсе нет ключа '{name}'"

        return response_as_dict[name]