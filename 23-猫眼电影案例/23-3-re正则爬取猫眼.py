import requests
from fake_useragent import UserAgent
import re
from random import randint
from time import sleep

def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    # 随机睡眠模拟人
    # sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_index(html):
    all_url = re.findall(r'<a href="(/films/\d+)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">', html)
    return ['https://maoyan.com{}'.format(url) for url in all_url]

def parse_info(html):
    name = re.findall(r'<h3 class="name">(.+)</h3>', html)[0]
    types = re.findall(r'<li class="ellipsis">(.+)</li>', html)[0]
    actors = re.findall(r'<a href="/films/celebrity/\d+" target="_blank" class="name">\s+(.*)\s+</a>', html)
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }

def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set

def main():
    index_url = 'https://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)

if __name__ == '__main__':
    main()