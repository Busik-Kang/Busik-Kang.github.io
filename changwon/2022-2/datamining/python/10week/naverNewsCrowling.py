import os
import sys
import urllib.request
import urllib
import json
import datetime

def getNaverSearch(node, srcText, page_start, display) :
  base = "https://openapi.naver.com/v1/search"
  node = "/%s.json" % node
  parameters = "?query=%s&start=%sdisplay=%s"% (urllib.parse.quote(srcText), page_start, display)
  url = base + node + parameters
  print(url)

  client_id = 'OU_qFlZy2JG7si3EC_Bz'    # 네이버에서 발급 받은 id를 넣음
  client_sec = 'Yks3HKaGP1'             # 네이버에서 발급 받은 secret code를 넣음

  req = urllib.request.Request(url)
  req.add_header('X-Naver-Client-Id', client_id)
  req.add_header('X-Naver-Client-Secret', client_sec)

  response = urllib.request.urlopen(req)
  ret = response.getcode()

  if ret == 200:
    return json.loads(response.read().decode('utf-8'))  
  else:
    print("에러")
    return None

def getPostData(post, jsonResult, cnt) :
  title     = post['title']
  desc      = post['description']
  org_link  = post['originallink']
  link      = post['link']
  jsonResult.append({'cnt' : cnt, 'title' : title,
                    'org_link' : org_link, 'link' : link, 'desc' : desc})

def main() :
  jsonResult = []

  cnt = 0
  ret = getNaverSearch('news', '고양이',1,10)

  for post in ret['items'] :
      getPostData(post, jsonResult, cnt)
      cnt += 1
  print(jsonResult)
  with open('%s_naver_%s.json' % ('고양이', 'news'), 'w', encoding='utf8') as out :
      jsonFile = json.dumps(jsonResult, ensure_ascii = False, indent = 4)
      out.write(jsonFile)
      
if __name__ == '__main__':
    main()