import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    doc = pq(html)
    all_a = doc('.movie-item > a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrib['href'])
    return ['https://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    doc = pq(html)
    name = doc('h3.name').text()
    types = doc('ul > li.ellipsis').eq(0).text()
    actors = doc('li.celebrity.actor > div.info > a')
    actors = format_actors(actors)
    return {
        "name": name,
        "types": types,
        "actors": actors
    }


def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.text.strip())
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
