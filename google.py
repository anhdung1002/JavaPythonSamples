
from time import perf_counter, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Safari()
driver.get('https://apple.com')
searchField = driver.find_element(By.XPATH,'//*[@id="ac-gn-link-search"]')
# searchField.send_keys('selenium')
searchField.click()

inputField = driver.find_element(By.XPATH,'//*[@id="ac-gn-searchform-input"]')
sleep(3)
inputField.send_keys('macbook  pro')
inputField.send_keys(Keys.ENTER)
driver.close()

driver.get('https://google.com')