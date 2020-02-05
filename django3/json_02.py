import json
# import os
# import sys
# import urllib.request
# client_id = "9eYRtkGNmEzbrUhDYxym"
# client_secret = "QFU3tG14u2"
# encText = urllib.parse.quote("코로나")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result=response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# with open('data\\corona.csv', 'w', encoding='utf-8') as f:
#     tojson=json.loads(result)
#     print(tojson['items'])  #[{},{},...{}]
#     for dic in tojson['items']:
#         title=dic['title']
#         description=dic['description']
#         title=title.replace('<b>코로나</b>','코로나')
#         title=title.replace(',',' ')
#         description=description.replace('<b>코로나</b>','코로나')
#         description=description.replace(',',' ')
#         str = title + ',' + description + '\n'
#         print(title)
#         print(description)
#         print('-'*30)
#         f.write(str)
# ---------------------------
import os
import sys
import urllib.request
client_id = "9eYRtkGNmEzbrUhDYxym"
client_secret = "QFU3tG14u2"
encText = urllib.parse.quote("증상")
url = "https://openapi.naver.com/v1/search/book.json?display=100&query=" + encText # json 결과
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
# 책 제목, 저자, 출판사, 가격 ==> data\\book.csv
with open("data\\book.csv", 'w', encoding='utf-8')as f:
    tojson = json.loads(result)
    print(tojson)
    for dic in tojson['items']:
        title = dic['title']
        title = title.replace('<b>증상</b>', '코로나')
        image = dic['image']
        author = dic['author']
        publisher = dic['publisher']
        price = dic['price']
        str = '{},{},{},{},{}\n'.format(title, image, author, publisher, price)
        f.write(str)
        # print(str)

#  '{},{},{},{},{}'.format(), 이미지 저장


