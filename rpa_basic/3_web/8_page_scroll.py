from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service



# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager



# 브라우저 꺼짐 방지

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)



# 불필요한 에러 메시지 없애기

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])



service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home')

# 무선 마우스 입력
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input')
elem.send_keys('무선마우스')
elem.send_keys(Keys.ENTER) # 검색 버튼 클릭을 위해 Enter 처리

# 스크롤
# 지정한 위치로 스크롤 내리기
# 모니터 (해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)') # 1920 * 1080 
# browser.execute_script('window.scrollTo(0,2444)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 페이지 로딩 대기 (2초)
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면
        break # 반복문 탈출 (모든 스크롤 동작 완료)

    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script('window.scrollTo(0,0)')


time.sleep(5)



