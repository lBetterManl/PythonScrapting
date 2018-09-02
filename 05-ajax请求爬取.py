from urllib.request import Request, urlopen


def save_file(filename, content):
    with open(filename, "wb") as f:
        f.write(content)


base_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
i = 0
while True:
    url = base_url.format(i * 20)
    request = Request(url)
    response = urlopen(request)
    info = response.read().decode()
    if info == "" or info is None:
        break
    filename = "第"+str(i+1)+"页数据.json"
    save_file(filename, info.encode())
    i += 1
