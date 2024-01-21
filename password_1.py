import requests

login = "super_admin"
response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login" : "abc", "password" : "abcd"})
print("неверный логин response: " + response.text)
print("неверный логин response_code: " + str(response.status_code))

response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"password" : "abcd"})
print("без логина response1: " + response.text)
print("без логина response_code1: " + str(response.status_code))

response2 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login" : f"{login}", "password" : "abcd"})
print("верный логин response2: " + response2.text)
print("верный логин response2: " + str(response2.status_code))

# # c user-agent
#
# us_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# session = requests.get("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", params={"User-Agent": f"{us_agent}"})
#
# print("Get с юзер-агентом" + session.text)
# print(session.status_code)
#
# response3 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login" : f"{login}", "password" : "abcd"})
# print("верный логин после get response3: " + response3.text)
# print("response3: " + str(response3.status_code))

