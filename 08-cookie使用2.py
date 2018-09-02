from urllib.request import Request, HTTPCookieProcessor, build_opener
from urllib.parse import urlencode
from random import choice

user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
                   "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
                   "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
headers = {
    "User-Agent": choice(user_agents)
}

# 登录
login_url = "http://www.sxt.cn/index/login/login"
form_data = {
    "user": "17703181473",
    "password": "123456"
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=f_data)
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)

# 访问页面
info_url = "http://www.sxt.cn/index/user.html"
request = Request(info_url, headers=headers)
response = opener.open(request)
print(response.read().decode())
