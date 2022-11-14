import time
import clipboard
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from numba import jit
from selenium.webdriver.support.wait import WebDriverWait

from Products import Fields

# @jit(nopython=True)
def Login(driver):
    print("Action : Login")

    loginbutton = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
    loginbutton.click()

    time.sleep(2)

    emailid = driver.find_element(
        By.XPATH, '//*[@id="mui-1"]')
    # emailid.send_keys('ronnyronny1992@gmail.com')
    # emailid.send_keys('shribalajimotersagar@gmail.com')
    # emailid.send_keys('thegiftarea.in@gmail.com')
    # emailid.send_keys('artsmarketing.in@gmail.com')
    emailid.send_keys('PROHRA8@GMAIL.COM')

    password = driver.find_element(
        By.XPATH, '//*[@id="mui-2"]')
    password.send_keys('Yash@12345')

    submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/form/button[2]')
    submit.click()



    # time.sleep(10)
    wait = WebDriverWait(driver, 25, ignored_exceptions=[ElementClickInterceptedException])
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/nav/div/div/div/div[2]/div[2]/div/ul/div/div[6]/li')))
    driver.implicitly_wait(15)

    catlogupload = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/div/div[2]/div[2]/div/ul/div/div[6]/li')
    catlogupload.click()

    # time.sleep(5)
    driver.implicitly_wait(15)







