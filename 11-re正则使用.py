import re

str1 = "I Study Python3.6 Everyday"
print("==============>match()<================")
m1 = re.match(r'I', str1)
m2 = re.match(r'\w', str1)
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'i', str1, re.I)
m6 = re.match(r'\S', str1)
m7 = re.match(r'Study', str1) # 匹配不到，因为match从左开始匹配
print(m4.group())

print("==============>search()<================")
s1 = re.search(r'Study', str1)
s2 = re.search(r'S\w+', str1)
s3 = re.search(r'P\w+.\d', str1)
print(s3.group())

print("==============>findall()<================")
f1 = re.findall(r'y', str1)
print(f1)

print("==============>test<================")
str2 = '<div><a href="https://www.baidu.com">百度一下gg</a></div>'
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)
t2 = re.findall(r'<a href="https://www.baidu.com">(.+)</a>', str2)
t3 = re.findall(r'<a href="(.+)">', str2)
print(t3)

print("==============>sub()<================")
su1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)
print(su1)
