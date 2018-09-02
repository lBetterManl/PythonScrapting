import requests
from fake_useragent import UserAgent
from lxml import etree

headers = {
    "User-Agent": UserAgent().random
}
url = "https://www.qiushibaike.com/article/120925356"

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
content = e.xpath('//div[@class="content"]')
for c in content:
    print(c.xpath('string(.)'))
image_urls = e.xpath('//div[@class="thumb"]/img/@src')
for img in image_urls:
    response = requests.get('https:'+img, headers=headers)
    with open("qiushi.jpg", 'wb') as f:
        f.write(response.content)

