import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# cars 에 해당하는 element 를 찾고ㅡ 드롭다운 내부에 있는 4번쨰 옵션을 선택
# elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[3]')
# option[1] : 첫번째 항목
# option[1] : 두번째 항목
# option[1] : 세번째 항목
# ...
# elem.click()


# 텍스트 값을 통해서 선택하는 방법
# 옵션 중에서 텍스트가 Audi인 항목을 선택
# elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[text() = "Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(5)