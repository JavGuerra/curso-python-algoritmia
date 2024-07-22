from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
browser.implicitly_wait(10)
browser.execute_script("window.open('https://google.com', 'new tab')")
time.sleep(5)
browser.quit()
