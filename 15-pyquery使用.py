from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

url = "http://www.xicidaili.com/nn"
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url, headers=headers)
doc = pq(response.text)
trs = doc('#ip_list tr')
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    type = trs.eq(num).find('td').eq(5).text()
    print(type, "://", ip, ":", port)
