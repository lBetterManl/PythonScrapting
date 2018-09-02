from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
import json

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
names = jsonpath(json.loads(response.text), '$..name')
codes = jsonpath(json.loads(response.text), '$..code')

print(names)
print(codes)


