# 安装browsercookie和pypiwin32
import browsercookie
import requests
from jsonpath import jsonpath
import json
import re

# 消除 warning   InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


base_url = "https://m.weibo.cn/api/container/getIndex?containerid=2304131671973710_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page="

# 获取cookie，前提是需要浏览器登陆过
cj = browsercookie.chrome()

with open("blogs.txt", 'a+', encoding="utf-8") as f:
    for page in range(1, 6000):
        print(base_url+str(page))
        response = requests.get(base_url+str(page), cookies=cj)
        dates = jsonpath(json.loads(response.text), '$..created_at')
        blogs = jsonpath(json.loads(response.text), '$..text')
        for i in range(len(dates)):
            content = dates[i]+'\t'+blogs[i]+'\r\n\n\n'
            dr = re.compile(r'<[^>]+>', re.S)
            f.write(dr.sub('', content))
            f.flush()





