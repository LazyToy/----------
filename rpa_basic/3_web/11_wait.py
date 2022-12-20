import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/')

# 가는 날 클릭
browser.find_element(By.LINK_TEXT,'가는 날').click()  
browser.find_elements(By.LINK_TEXT,'21')[0].click()

# 오는 날
browser.find_elements(By.LINK_TEXT,'25')[0].click()

# 오사카 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div/ul/li[1]/button/figure/img').click()

# 항공원 검색 클릭
browser.find_element(By.LINK_TEXT,'항공권 검색').click()


time.sleep(5)
browser.quit()
