from urllib.request import Request, urlopen
from random import choice

user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
                   "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
                   "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
headers = {
    "User-Agent": choice(user_agents),
    "Cookie": "浏览器登陆后的cookie"
}
url = "https://www.baidu.com"
request = Request(url, headers=headers)
response = urlopen(url)
print(response.read().decode())