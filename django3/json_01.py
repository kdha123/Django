import os
import sys
import json
import urllib.request
client_id = "9eYRtkGNmEzbrUhDYxym"
client_secret = "QFU3tG14u2"
encText = urllib.parse.quote("신종")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
tojson = json.loads(result)
# print(tojson, type(json))
# print(tojson['items'])
for dic in tojson['items']:
    # print(dic['title'])
    # print(dic['description'])
    title = dic['title']
    description = dic['description']
    title = title.replace('<b>신종</b>', '신종')
    title = title.replace(',', ' ')
    description = description.replace('<b>신종</b>', '신종')
    description = description.replace(',', ' ')
    print(title)
    print(description)
    print('-'*30)
