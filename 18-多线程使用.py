from threading import Thread
from  queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree


# 爬虫类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().random
        }
        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)


# 解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            with open("duanzi.txt", 'a', encoding='utf-8') as f:
                for span in span_contents:
                    info = span.xpath('string(.)')  # 格式化当前节点
                    f.write(info + '\n')


if __name__ == '__main__':
    # 存储url的容器
    url_queue = Queue()
    # 存储内容的容器
    html_queue = Queue()
    base_url = "https://www.qiushibaike.com/text/page/{}"
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    # 创建一个爬虫
    craw1_list = []
    for i in range(0, 3):
        craw11 = CrawlInfo(url_queue, html_queue)
        craw1_list.append(craw11)
        craw11.start()
    # 等待所有craw1线程结束
    for craw1 in craw1_list:
        craw1.join()
    parse_list = []
    for i in range(0, 3):
        parse1 = ParseInfo(html_queue)
        parse_list.append(parse1)
        parse1.start()
    # 等待所有parse线程结束
    for parse in parse_list:
        parse.join()
