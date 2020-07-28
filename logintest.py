from selenium import webdriver
from selenium.webdriver.common.keys import Keys#
import time

def checkloginstatus():
    try:
        assert ("Successfully logged in!") in driver.page_source
    except AssertionError:
        assert("Error Message")in driver.page_source
        print("Login failed")
    else:
        print("Login success")
        
driver = webdriver.Chrome()
driver.get(" https://login.dev.qa-experience.com")
elem1 = driver.find_element_by_name('loginUsername')
elem2 = driver.find_element_by_name('loginPassword')
elem1.send_keys("test@qa-experience.com")
elem2.send_keys("Password1")
driver.find_element_by_xpath("/html/body/app-root/div/app-login/form/button").click()
checkloginstatus()
time.sleep(5)

driver.get(" https://login.dev.qa-experience.com")
elem1 = driver.find_element_by_name('loginUsername')
elem2 = driver.find_element_by_name('loginPassword')
elem1.send_keys("test123qaexperience")
elem2.send_keys("Password123")
driver.find_element_by_xpath("/html/body/app-root/div/app-login/form/button").click()
checkloginstatus()

