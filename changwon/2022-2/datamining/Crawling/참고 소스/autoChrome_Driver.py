from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)                         #브라우저 바로 닫힘 방지
service = Service(ChromeDriverManager(path="CHROM DRIVER").install())   #크롬 드라이버 자동 설치

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.google.co.kr/imghp?hl=ko"
driver.get(url)
time.sleep(1)

ele = driver.find_element(By.NAME, "q")
ele.send_keys("파란하늘")
ele.send_keys(Keys.ENTER)
time.sleep(1)



"""
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" 
type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" 
autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" 
title="검색" value="" aria-label="검색" data-ved="0ahUKEwj9yNilz7L7AhVHRd4KHb7xBkAQ39UDCAM">  
"""