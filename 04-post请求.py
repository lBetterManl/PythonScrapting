from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "https://passport.baidu.com/v2/api/?login"
form_data = {
    "username": "54沦落人",
    "password": "123"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
f_data = urlencode(form_data).encode(encoding='UTF8')
print(f_data)
request = Request(url, data=f_data, headers=headers)
response = urlopen(request)
print(response.read().decode())
