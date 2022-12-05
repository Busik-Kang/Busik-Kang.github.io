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

  url = "https://www.changwon.ac.kr/portal/main.do"
  driver.get(url)
  time.sleep(1)
  
  element = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[3]/div/div/div[1]/a/i')
  element.click()  
  time.sleep(1)
  
  for page in range(1,5) :
    driver.execute_script("goPaging(%d)" %page)
    time.sleep(1)
    bs = BeautifulSoup(driver.page_source, 'html.parser')

  
    results = []
    
    for idx in range(3,13) :  
      title = bs.select('tr')[idx].select('td')[1].text
      title = title.strip()
      date = bs.select('tr')[idx].select('td')[2].text
      numClick = bs.select('tr')[idx].select('td')[3].text      
      results.append([title, date, numClick])    
      print(results[idx - 3])    
  
  
def main() :
  chromDriverInit()


if __name__ == '__main__':
  main()