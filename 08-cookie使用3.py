from urllib.request import Request, HTTPCookieProcessor, build_opener
from urllib.parse import urlencode
from random import choice
from http.cookiejar import MozillaCookieJar

user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
               "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
               "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
headers = {
    "User-Agent": choice(user_agents)
}


def get_cookie():
    # 登录
    # 保存Cookie到文件中
    login_url = "http://www.sxt.cn/index/login/login"
    form_data = {
        "user": "17703181473",
        "password": "123456"
    }
    f_data = urlencode(form_data).encode()
    request = Request(login_url, headers=headers, data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)


def use_cookie():
    info_url = "http://www.sxt.cn/index/user.html"
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load("cookie.txt", ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)
    print(response.read().decode())


if __name__ == '__main__':
    get_cookie()
    use_cookie()
