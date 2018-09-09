# 安装browsercookie和pypiwin32
import browsercookie
import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath
import json
import os.path

# 消除 warning   InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

cj = browsercookie.chrome()

headers = {
    "User-Agent": UserAgent().random
}


def get_res(mid, pid):
    base_url = 'https://weibo.com/aj/photo/popview'
    params = {
        "mid": mid,
        "pid": pid,
        "uid": "1671973710"
    }
    response = requests.get(base_url, params=params, headers=headers, cookies=cj)
    clear_pics = jsonpath(json.loads(response.text), '$..pic_list[*].clear_picSrc')
    for clear_pic in clear_pics:
        get_img(clear_pic, os.path.basename(clear_pic))
    next_mid = jsonpath(json.loads(response.text), '$..pic_next.mid')
    next_pid = jsonpath(json.loads(response.text), '$..pic_next.pid')
    return get_res(next_mid, next_pid)


def get_img(clear_pic, img_name):
    response = requests.get('https:' + clear_pic)
    with open('blogImg/' + img_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    response_text = get_res('4281850556165152', '63a84b4egy1fv1ossr8oyj22c02c0b29')
