import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download,default_directory':r'C:\Users\bea99\OneDrive\바탕 화면\나도코딩 업무자동화'})

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# download 링크 클릭
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a/img')
elem.click()

time.sleep(5)
browser.quit()