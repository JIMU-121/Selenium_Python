from selenium.webdriver.common.by import By




def BluetoothHeadPhonesAndEarPhones(driver):

    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div/div[1]/div/p[7]').click()  # Consumer electronics
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[2]/div/div[2]/p[9]').click()  # Audio & Video
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[3]/div/div[2]/p[2]').click()  # Headphones & Earphones
    driver.find_element(By.XPATH,
                        '//*[@id="mainWrapper"]/div/div[5]/div[1]/div[4]/div/div[2]/p[1]').click()  # Bluetooth Headphones & Earphones


def HairDryer(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Hair Dryer"]').click() # Hair Dryer


def Trimmer(driver):

    driver.find_element(By.XPATH, '//p[normalize-space()="Appliances"]').click()  # Appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Small appliances"]').click()  # Small appliances
    driver.find_element(By.XPATH, '//p[normalize-space()="Personal Grooming"]').click() # Personal Grooming
    driver.find_element(By.XPATH, '//p[normalize-space()="Trimmers"]').click() # Trimmer
