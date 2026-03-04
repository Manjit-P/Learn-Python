from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('helloworld')
pass_elem =browser.find_element(By.ID,'login_pass')
pass_elem.send_keys("nah")
pass_elem.submit()