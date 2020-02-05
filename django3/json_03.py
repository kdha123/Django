# 네이버 Papago NMT API 예제
import json
# import os
# import sys
# import urllib.request
# client_id = "CZlk4f8gLxTpIHG9wM4F"
# client_secret = "Wyg9qcMMIn"
# encText = urllib.parse.quote("오늘 너무 건조하다")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# tojson = json.loads(result)
# print(tojson['message']['result']['translatedText'])

# ------------------------------let it be 가사 해석하기
text = open('data\\song.txt').read()
# print(text)
import os
import sys
import urllib.request
client_id = "CZlk4f8gLxTpIHG9wM4F"
client_secret = "Wyg9qcMMIn"
encText = urllib.parse.quote(text)
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
tojson = json.loads(result)
print(tojson['message']['result']['translatedText'])
