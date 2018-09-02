from urllib.request import Request, urlopen
from urllib.error import URLError

url = "http://www.sxt.cn/index/login/login"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
try:
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)
print("访问完成")
