
import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
resp = response.json()

for k, v in resp.items():
    if k == "token":
        tok = v
        # print(tok)
    else:
        sec = v
        # print(sec)


response_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': f"{tok}"})
assert response_1.text == '{"status":"Job is NOT ready"}'
# print(response_2.text)

time.sleep(v)

response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token':f"{tok}"})

assert response_2.text.__contains__('result')
assert response_2.text.__contains__(str('"status":"Job is ready"'))

print("Кейс пройден успешно")