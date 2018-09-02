# www.yundama.com收费

import requests
from fake_useragent import UserAgent
# from my_util import get_code 调用云打码的工具

headers = {
    "User-Agent": UserAgent().random
}

def get_image():
    img_url = "http://www.yundama.com/index/captcha"
    response = session.get(img_url, headers = headers)
    with open('yzm.jpg', 'wb') as f:
        f.write(response.content)
    code = get_code('yzm.jpg')
    return code

def do_login():
    login_url = "http://www.yundama.com/login?"
    f_data = {
        "username": "398707160_pt",
        "password": "123456abc",
        "utype": "1",
        "vcode": code
    }
    response = session.get(login_url, headers=headers, params=f_data)

if __name__ == '__main__':
    index_url = "http://www.yundama.com"
    session = requests.session()
    code = get_image()
    do_login(code)
    response = session.get(index_url, headers=headers)
