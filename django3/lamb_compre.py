# 컴프리헨션 - 컬렉션을 만드는 한줄짜리 반복문
# a = [1, 2, 3, 4, 5]
# print(a)
a = []
for n in range(1,11):
    # print(n)
    a.append(n)
# print(a)
a = [n for n in range(1, 11)]
# print(a)

# [7,7,.....,7]
a = []
for i in range(100):
    a.append(7)
# print(a)
b = [7 for i in range(100)]
# print(b)
a = []
for n in range(1,101):
    if n % 2 == 1:
        a.append(n)
# print(a)
b = [n for n in range(1, 101)if n % 2 == 1]
# print(b)

a = 'tensorflow'
# for c in a:
    # print(c)
b = [c for c in a]
# print(b)
d = {c:0 for c in a}
# print(d)

# for c in enumerate(a):
#     print(c)
# for i, c in enumerate(a):
#     print(i, c)
d = {i:c for i,c in enumerate(a)}
# print(d)
# -----------------------------

import json_01
j1='{"ip": "8.8.8.8"}'
# print(j1)
# loads = 문자열일때 , load = 파일일때
d1 = json_01.loads(j1)
# print(d1, type(d1))
# print(d1['ip'])


j2 = '''{
   "Accept-Language": "en-US,en;q=0.8",
   "Host": "headers.jsontest.com",
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}'''
print(j2, type(j2))
d2 = json_01.loads(j2)
print(d2, type(d2))
print('-'*30)
jj2 = json_01.dumps(d2)
print(jj2, type(jj2))
