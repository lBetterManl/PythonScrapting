import requests

url = "http://www.sxt.cn/index/login/login"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

url = "https://www.baidu.com/s"
params = {
    "word": "湖北工业大学"
}

response = requests.get(url, headers=headers, params=params, verify=False)
print(response.content.decode())
