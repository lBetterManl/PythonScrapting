# 下载Selenium.exe
# 利用驱动操作浏览器
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('http://www.baidu.com')
chrome.save_screenshot('jietu.png')
html = chrome.page_source
print(html)

chrome.quit()