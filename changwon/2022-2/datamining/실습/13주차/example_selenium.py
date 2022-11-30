from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests
from bs4 import BeautifulSoup


def chromDriverInit() :
  options = Options()
  options.add_experimental_option("excludeSwitches", ["enable-logging"])  #크롬 드라이버의 usb 오류 메세지 삭제
  options.add_experimental_option("detach", True)                         #브라우저 바로 닫힘 방지
  service = Service(ChromeDriverManager(path="ChomeDriver").install())    #path = "설치할 폴더"  
  driver = webdriver.Chrome(service=service, options=options)
  
  url = "https://www.coffeebeankorea.com/store/store.asp"

  driver.get(url)
  time.sleep(3)

  ele = driver.find_element(By.ID, 'region_srh')   # 지역 검색 선택
  ele.click()                                      # 지역 검색 클릭

  ele = driver.find_element(By.ID, 'localTitle')   # 시/도를 선택
  ele.click()

  
  driver.execute_script("stroeLocal2('서울')")


def main() :
  chromDriverInit()


if __name__ == '__main__':
    main()