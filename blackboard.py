from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def waitForElement(xpath, dur):
    try:
        userName = WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
        sleep(dur)
    except TimeoutException:
        print('Did not wait long enough for page to load')



# driver = webdriver.Chrome('/Users/andynguyen/Downloads/chromedriver')
driver = webdriver.Safari()
driver.maximize_window()
driver.get('https://blackboard.jhu.edu/webapps/login/')
jhButton = driver.find_element(By.XPATH,'//*[@id="JHU-logo"]')
jhButton.click()

