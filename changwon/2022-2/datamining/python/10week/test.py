import os
import sys
import urllib.request
import urllib
import json
import datetime

keyworld = urllib.parse.quote("고양이")
client_id = 'OU_qFlZy2JG7si3EC_Bz'
client_sec = 'Yks3HKaGP1'

url = 'https://openapi.naver.com/v1/search/news.json?query=' + keyworld
print(url)

req = urllib.request.Request(url)
req.add_header('X-Naver-Client-Id', client_id)
req.add_header('X-Naver-Client-Secret', client_sec)

response = urllib.request.urlopen(req)
ret = response.getcode()

if ret == 200:
  print(response.read().decode('utf-8'))
else:
  print("에러")