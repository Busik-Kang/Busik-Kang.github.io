from bs4 import BeautifulSoup
import requests

def example() :
  print("-----------------------코드 시작----------------------")
  print(" ")
  print(" ")
  print(" ")
  #코드 시작 부분
  
  results = []
  
  
  for page in range(1,10) :
  
    #page = 1
    url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
    
    resp = requests.get(url)
    
    hollys_soup = BeautifulSoup(resp.content, 'html.parser')
    print_data = hollys_soup.select('tr')
    
    for tr_tag in print_data :
      if (len(tr_tag.select('td')) != 0) : #tr태그가 빈것인지 알아내는 방법
        sido = tr_tag.select('td')[0].text
        name = tr_tag.select('td')[1].text
        addr = tr_tag.select('td')[3].text
        phone = tr_tag.select('td')[5].text
        
        results.append([sido, name, addr, phone])
    print("=================================%d page end=====================================================" %page)
  print(results)
  
  
  
  
  #코드 끝 부분  
  print(" ")
  print(" ")
  print(" ")
  print("-----------------------코드 끝-----------------------")
  
  
  
  
def main() :
  example()


if __name__ == '__main__':
    main()