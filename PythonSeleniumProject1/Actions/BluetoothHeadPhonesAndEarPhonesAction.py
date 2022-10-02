import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import BluetoothHeadPhonesAndEarPhonesFields as Fields
from selenium.webdriver.common import keys




def BluetoothHeadPhonesInventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------

    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('450')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('445')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.HSNCodeList)
    for r in HSNCodeList:
        if '8518' == r.text:
            r.click()
            break

    # time.sleep(1)
    driver.implicitly_wait(1)


    # Net Weight
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg2)


    # Product Name
    clipboard.copy(' TRUE WIRELESS EARBUDS AIRPODS V5.1 WITH 1500 MAH POWER BANK Bluetooth Headset  (Black, True Wireless) + Cable Protector Pack Of 4')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(Fields.alp + str(x) + keys.Keys.CONTROL + 'v')

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    GSTList = driver.find_elements(By.XPATH, Fields.GSTList)
    for r in  GSTList:
        if '18' == r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    #driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)
    # driver.implicitly_wait(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.find_element(By.XPATH, '//input[@id="length_size"]').click()
    time.sleep(1)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//li[1]').click()


def BluetoothHeadPhoneProductDetails(driver):

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg3)


    # BatteryChargeTime
    driver.find_element(By.XPATH, Fields.BatteryChargeTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BatteryChargeTimeList = driver.find_elements(By.XPATH, Fields.BatteryChargeTimeList)
    for r in BatteryChargeTimeList:
        if '3 Hours' == r.text:
            r.click()
            break

    # Compatibility
    driver.find_element(By.XPATH, Fields.Compatibility).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CompatibilityList = driver.find_elements(By.XPATH, Fields.CompatibilityList)
    for r in CompatibilityList:
        if 'All Smartphones' == r.text:
            r.click()
            break

    # PlayTime
    driver.find_element(By.XPATH, Fields.PlayTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PlayTimeList = driver.find_elements(By.XPATH, Fields.PlayTimeList)
    for r in PlayTimeList:
        if '10 Hours' == r.text:
            r.click()
            break

    # WarrantyPeriod
    driver.find_element(By.XPATH, Fields.WarrantyPeriod).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyPeriodList = driver.find_elements(By.XPATH, Fields.WarrantyPeriodList)
    for r in WarrantyPeriodList:
        if '1 Year' == r.text:
            r.click()
            break

    # WaterResistance
    driver.find_element(By.XPATH, Fields.WaterResistance).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WaterResistanceList = driver.find_elements(By.XPATH, Fields.WaterResistanceList)
    for r in WaterResistanceList:
        if 'Yes' == r.text:
            r.click()
            break

    # Color
    driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ColorList = driver.find_elements(By.XPATH, Fields.ColorList)
    for r in ColorList:
        if 'Black' == r.text:
            r.click()
            break

    # ModelName
    driver.find_element(By.XPATH, Fields.ModelName).send_keys('2in1')


    # Type
    driver.find_element(By.XPATH, Fields.Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TypeList = driver.find_elements(By.XPATH, Fields.TypeList)
    for r in TypeList:
        if 'In The Ear' in r.text:
            r.click()
            break

    # WarrentyType
    driver.find_element(By.XPATH, Fields.WarrentyType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrentyTypeList = driver.find_elements(By.XPATH, Fields.WarrentyTypeList)
    for r in WarrentyTypeList:
        if 'Carry In' in r.text:
            r.click()
            break

    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CountryList = driver.find_elements(By.XPATH, Fields.CountryList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break

    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')


def BluetoothHeadPhoneOtherAttributes(driver):
    # Bluetooth Range
    driver.find_element(By.XPATH, Fields.BluetoothRange).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BluetoothRangeList = driver.find_elements(By.XPATH, Fields.BluetoothRangeList)
    for r in BluetoothRangeList:
        if '10m' in r.text:
            r.click()
            break

    # BluetoothVersion
    driver.find_element(By.XPATH, Fields.BluetoothVersion).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BluetoothVersionList = driver.find_elements(By.XPATH, Fields.BluetoothVersionList)
    for r in BluetoothVersionList:
        if '5.1' in r.text:
            r.click()
            break

    # ChargingType
    driver.find_element(By.XPATH, Fields.ChargingType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ChargingTypeList = driver.find_elements(By.XPATH, Fields.ChargingTypeList)
    for r in ChargingTypeList:
        if 'Micro USB' in r.text:
            r.click()
            break

    # NetQuantity
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.NetQuantityList)
    for r in NetQuantityList:
        if '2' in r.text:
            r.click()
            break

    # Frequency
    driver.find_element(By.XPATH, Fields.Frequency).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    FrequencyList = driver.find_elements(By.XPATH, Fields.FrequencyList)
    for r in FrequencyList:
        if '100 Hz' in r.text:
            r.click()
            break

    # Mic
    driver.find_element(By.XPATH, Fields.Mic).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    MicList = driver.find_elements(By.XPATH, Fields.MicList)
    for r in MicList:
        if 'Yes' in r.text:
            r.click()
            break

    # NoiceCancelation
    driver.find_element(By.XPATH, Fields.NoiceCancelation).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NoiceCancelationList = driver.find_elements(By.XPATH, Fields.NoiceCancelationList)
    for r in NoiceCancelationList:
        if 'Yes' in r.text:
            r.click()
            break

    # Description
    clipboard.copy('M10 TWS Wireless Bluetooth v5.1Headset.It’s time to take your music-listening experience with high-capability 1500mAh rechargeable lithium polymer battery with 1hours of charging time that will allow you to listen to your music up to 48 hours straight. High-Quality Material with Styles & lightweight design. Perfect fit & comfortable in your ear, for all-day wearing with no distractions. fast pairing,  & listening to music on the go takes a turn for the better. Easy to Carry & secure, stay firm in place even when you are working out or running. DEAMFLUM Advanced Bluetooth technology ensures a steady wireless connection without  and music.')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')