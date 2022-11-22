from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests

MAX_COUNT = 2000

def createFolder(dir):
  try:
    if not os.path.exists(dir):
      os.makedirs(dir)
  except OSError:
    print('Error: Creating directory: ' + dir)

# @bref : 현재 자기 Chrome에 맞는 Chrome Driver를 자동으로 설치함
def chromDriverInit() :
  options = Options()
  options.add_experimental_option("excludeSwitches", ["enable-logging"])  #크롬 드라이버의 usb 오류 메세지 삭제
  options.add_experimental_option("detach", True)                         #브라우저 바로 닫힘 방지
  service = Service(ChromeDriverManager(path="ChomeDriver").install())    #path = "설치할 폴더"  
  driver = webdriver.Chrome(service=service, options=options)  

  url = "https://www.google.co.kr/imghp?hl=ko"                            # 구글 이미지 사이트 주소로 설정
  driver.get(url)                                                         # 구글 이미지 사이트로 이동
  
  searchData = input("검색할 단어를 입력하세요 :")                        # 검색할 정보 입력

  element = driver.find_element(By.NAME, "q")                              # 속성이름(name)과 속성값"q"를 찾음
  element.send_keys(searchData)                                           # 검색 데이터를 검색 창에 넣음
  element.send_keys(Keys.ENTER)                                           # 엔터키를 누름

  #페이지 로드 대기 시간
  SCROLL_PAUSE_TIME = 2
  #이미지 클릭 후 로딩이 완료 될 때까지 시간
  IMG_CLICK_TIME = 3
  # 브라우저의 스크롤 높이를 자바스크립트로 찾음
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
    # 브라우저 끝까지 스크롤을 내림
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 페이지 로드를 기다림
    time.sleep(SCROLL_PAUSE_TIME)
    # 다시 브라우저의 스크롤 높이를 자바스크립트로 찾음
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height :
      try :
        # 이미지 더보기 버튼을 클릭
        driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
      except :
        # 이미지 더보기 버튼이 없다면 (결과 끝) 스크롤 내리기 종료
        break
    last_height = new_height

  # 브라우저에서 CSS_SELECTOR의 속성값이 .rg_i.Q4LuWd인 것이 이미지임
  imgs= driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
  
  # 총 몇개를 찾았는지를 표시
  print(f'images count : {len(imgs)}')

  # 이미지를 저장할 폴더를 생성 (검색한 키워드로 생성)
  dir = searchData
  createFolder(dir)

  count = 1  
  for img in imgs:
    try :
      #이미지 클릭
      img.click()
      # 이미지가 로드되는 동안 기다리는 시간 (인터넷 속도가 느리면 길게 설정)
      time.sleep(IMG_CLICK_TIME)
      imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute('src')
      print(str(count) + "/" + str(len(imgs)) + ": " + imgUrl)
      # 이미지 url로부터 파일을 받아 경로에 저장
      path = dir + "\\"
      imgData = requests.get(imgUrl, timeout=5).content

      with open(path + searchData + str(count) + ".jpg", 'wb') as handler:
        handler.write(imgData)

      count = count + 1
      if count >= MAX_COUNT + 1:
        break

    except Exception as e:
      print(e)
  driver.close()


  
"""
  url = "https://www.google.co.kr/imghp?hl=ko"
  driver.get(url)
  time.sleep(1)

  ele = driver.find_element(By.NAME, "q")
  ele.send_keys("파란하늘")
  ele.send_keys(Keys.ENTER)
  time.sleep(1)
"""

def main() :
  chromDriverInit()


if __name__ == '__main__':
    main()