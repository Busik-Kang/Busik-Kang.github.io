from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import os


# 이미지를 저장할 폴더 생성 기능
import os
def createFolder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error: Creating directory: ' + dir)

def crawling_img(name, maxCount):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    # 페이지가 로드되는 동안 기다리는 시간 (인터넷 속도가 느리면 길게 설정)
    SCROLL_PAUSE_TIME = 1
    # 브라우저의 스크롤 높이를 자바스크립트로 찾음
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 브라우저 끝까지 스크롤을 내림
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 페이지 로드를 기다림
        time.sleep(SCROLL_PAUSE_TIME)
        # 다시 브라우저의 스크롤 높이를 자바스크립트로 찾음
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                # 이미지 더보기 버튼을 클릭
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                # 이미지 더보기 버튼이 없다면 (결과 끝) 스크롤 내리기 종료
                break
        last_height = new_height
        print("스크롤 완료")

    # 로드된 전체 페이지에서 이미지 요소들을 모두 찾아냄
    imgs= driver.find_element s(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    print(f'images count : {len(imgs)}')

    # 이미지를 저장할 폴더를 생성
    dir = ".\ships" + "\\" + name
    createFolder(dir)

    count = 1
    for img in imgs:
        try:
            # 이미지 요소 클릭
            img.click()
            # 이미지가 로드되는 동안 기다리는 시간 (인터넷 속도가 느리면 길게 설정)
            time.sleep(3)
            # 이미지를 다운로드할 url 검색, xpath의 경로는 f12를 눌러 개발자 도구를 열고, ctrl+shift+c 를 눌러 해당 요소를 찾아 복사할 수 있다.
            imgUrl = driver.find_element(By.XPATH,
                '//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute(
                "src")
            print(str(count) + "/" + str(len(imgs)) + ": " + imgUrl)
            # 이미지 url로부터 파일을 받아 경로에 저장
            path = dir + "\\"
            imgData = requests.get(imgUrl, timeout=5).content
            with open(path + name + str(count) + ".jpg", 'wb') as handler:
                handler.write(imgData)

            count = count + 1
            if count >= maxCount + 1:
                break
        except Exception as e:
            print(e)

    driver.close()

# 검색어 목록
ships = "tugboat ship"
# 검색어별 이미지 저장 수
maxCount = 2000
crawling_img(ships, maxCount)    
