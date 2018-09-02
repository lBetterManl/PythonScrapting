from bs4 import BeautifulSoup, Comment

str = '''
<title id="title">样例</title>
<div class="info" float="left">Hello World</div>
<div class="info" float="right">
    <span>好好学习天天向上</span>
    <a href="www.baidu.com">百度一下，你就知道</a>
    <strong><!-- 没用 --></strong>
</div>
'''

# 使用lxml解析方式(建议不用html.parser使用lxml)
soup = BeautifulSoup(str, 'lxml')

print(soup.title)
print(soup.div)

print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a['href'])

print(soup.div.string)
print(soup.div.text)

if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())
else:
    print(soup.strong.text)

print("-------------------find_all()-----------------")
print(soup.find_all('title'))
print(soup.find_all(id='title'))
print(soup.find_all(class_='info'))
print(soup.find_all('div', attrs={'float': 'left'}))

print("--------------------CSS选择器-------------------")
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('.info'))
print(soup.select('div span'))
print(soup.select('div > span'))
print(soup.select('div')[1].select('a'))


