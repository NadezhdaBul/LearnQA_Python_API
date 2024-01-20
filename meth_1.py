import requests

response_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("если метод не указан: " + response_1.text)  #Wrong method provided

response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print("если тип запроса не из списка: " + response_2.text)

response_3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print("тип запроса и метод совпадают: " + response_3.text) #{"success":"!"}


method = ['GET', 'PUT', 'POST', 'DELETE']
for v in method:

    response_4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": f"{v}"})
    print(f"Для get запроса если метод указан  {v}, то результат - " + response_4.text)


    response_5 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{v}"})
    print(f"Для put запроса если метод указан  {v}, то результат - " + response_5.text)

    response_6 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{v}"})
    print(f"Для post запроса если метод указан  {v}, то результат - " + response_6.text)

    response_7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": f"{v}"})
    print(f"Для delete запроса если метод указан  {v}, то результат - " + response_7.text)    #Для delete запроса если метод указан  get, то результат - {"success":"!"}

