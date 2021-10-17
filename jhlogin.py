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
driver.get('https://my.jh.edu')
logInButton = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[1]/a')
logInButton.click()

waitForElement('//*[@id="i0116"]',1.2)
userName = driver.find_element(By.XPATH,'//*[@id="i0116"]')
userName.send_keys('anguye79@jh.edu')
nextButton = driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
nextButton.click()

waitForElement('//*[@id="i0118"]',3)
passInput = driver.find_element(By.XPATH,'//*[@id="i0118"]')
passInput.send_keys('Nextstep2021!')
waitForElement('//*[@id="idSIButton9"]',1.2)
signInButton = driver.find_element(By.XPATH,'//*[@id="idSIButton9"]')
signInButton.click()

waitForElement('//*[@id="appImage36"]',1.2)
blackBoard = driver.find_element(By.XPATH,'//*[@id="appImage36"]')
blackBoard.click()

sleep(3)
searchElement = driver.find_element(By.XPATH,'/html')
# searchElement.click()

print(searchElement)
sleep(3)
driver.find_elements(By.XPATH,'//*[@id="toggle_other_FA21"]/tbody/tr[1]/td[2]/span/a')[0].click()
# iframeList.click()