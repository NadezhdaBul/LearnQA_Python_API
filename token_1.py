
import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
resp = response.json()

for k, v in resp.items():
    if k == "token":
        tok = v

    else:
        sec = v


response_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': f"{tok}"})
assert response_1.text == '{"status":"Job is NOT ready"}'


time.sleep(v)

response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token':f"{tok}"})

assert response_2.text.__contains__('result') == True
assert response_2.text.__contains__(str('"status":"Job is ready"')) == True

print("Кейс пройден успешно")