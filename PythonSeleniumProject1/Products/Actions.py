import time
import clipboard
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from Products import Fields


def Login(driver):
    loginbutton = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
    loginbutton.click()

    time.sleep(2)

    emailid = driver.find_element(
        By.XPATH, '//*[@id="mui-1"]')
    # emailid.send_keys('ronnyronny1992@gmail.com')
    # emailid.send_keys('shribalajimotersagar@gmail.com')
    # emailid.send_keys('artsmarketing.in@gmail.com')
    emailid.send_keys('thegiftarea.in@gmail.com')


    password = driver.find_element(
        By.XPATH, '//*[@id="mui-2"]')
    password.send_keys('Yash@12345')

    submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/form/button[2]')
    submit.click()

    # time.sleep(10)
    driver.implicitly_wait(10)

    catlogupload = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/div/div[2]/div[2]/div/ul/li[6]')
    catlogupload.click()

    # time.sleep(5)
    driver.implicitly_wait(15)







