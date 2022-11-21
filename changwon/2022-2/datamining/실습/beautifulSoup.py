from bs4 import BeautifulSoup
import urllib.request
import requests

results = []

def halis() :
  for page in range(1,54) :  
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
    resp = requests.get(url)  # 200으로 응답이 오면 정상적인 url    

    if(resp.reason != 'OK') :
      print("잘못된 url입니다.")
      print('오류코드 : ' + str(resp))
      return
    else :
      print('정상적인 url입니다.')

    suop_hollys = BeautifulSoup(resp.content, 'html.parser')
    tag_tbody = suop_hollys.find('tbody')
    print(tag_tbody.prettify())
    
    for store in tag_tbody.find_all('tr') :
      print("=========================")
      print(store)
      if len(store) < 2 :
        break

      store_td = store.find_all('td')

      store_sido = store_td[0].string
      store_name = store_td[1].string
      store_addr = store_td[3].string
      store_phone = store_td[5].string
      
      results.append([store_sido, store_name, store_addr, store_phone])
      
    print(f"-------------------{page} page conplete-------------------------")
  print(results)
    

def main() :
  halis()

if __name__ == '__main__':
    main()