import requests
from fake_useragent import UserAgent

session = requests.session()

headers = {
    "User-Agent": UserAgent().chrome
}

# 使用ip代理
proxies = {
    "http": "118.190.95.35:9001"
}

# 关闭警告
requests.packages.urllib3.disable_warnings()

login_url = "http://www.sxt.cn/index/login/login"
params = {
    "user": "17703181473",
    "password": "123456"
}

response = session.post(login_url, headers=headers, data=params, proxies=proxies)
# print(response.content.decode())
info_url = "http://www.sxt.cn/index/user.html"
response = session.get(info_url, headers=headers)
response.encoding = "utf-8"
print(response.text)
