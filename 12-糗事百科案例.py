import requests
from fake_useragent import UserAgent
import re

url = "https://www.qiushibaike.com/text/page/1/"
headers = {
    "User-Agent": UserAgent().random
}
# 关闭警告
requests.packages.urllib3.disable_warnings()
# 构造请求
response = requests.get(url, headers=headers, verify=False)
info = response.text
# print(info)
infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', info)
# print(infos)
with open("duanzi.txt", 'a', encoding="utf-8") as f:
    for duanzi in infos:
        f.write(re.sub(r'<.+.>', "\n", duanzi)+"\n\n\n")
