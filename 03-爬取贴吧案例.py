from urllib.request import Request, urlopen
from urllib.parse import urlencode
from random import choice


def get_html(url):
    user_agents = ["Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
                   "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
                   "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"]
    headers = {
        "User-Agent": choice(user_agents)
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def save_html(filename, html_bytes):
    with open(filename, "wb") as f:
        f.write(html_bytes)


def main():
    content = input("请输入要下载的内容：")
    num = input("请输入要下载的页数：")
    base_url = "http://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        filename = "第" + str(pn+1) + "页.html"
        args = urlencode(args)
        print("正在下载"+filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename, html_bytes)


if __name__ == '__main__':
    main()
