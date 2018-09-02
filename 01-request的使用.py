from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "https://www.baidu.com"

# 不同的user-agent,供随机选择
user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
               "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
               "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]

headers = {
    "User-Agent": choice(user_agents)
}

request = Request(url, headers=headers)
response = urlopen(request)

info = response.read()

print(info.decode())
