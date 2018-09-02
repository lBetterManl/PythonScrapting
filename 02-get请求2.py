from urllib.request import Request, urlopen
from urllib.parse import urlencode

args = {
    "wd": "鄢航程"
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())