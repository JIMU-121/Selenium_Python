import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import BluetoothHeadPhonesAndEarPhonesFields as Fields
from selenium.webdriver.common import keys




def BluetoothHeadPhonesInventoryDetails(driver,x):
    print('Action : BluetoothHeadPhone Inventory Details')
    # ---------------------- Price, Size and Inventory ---------------------------------

    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('190')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('185')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()
    # time.sleep(1)
    driver.implicitly_wait(2)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
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
    clipboard.copy('HBS-730 '+x+' Bluetooth Stereo Sports Headset Bluetooth Headset  + Cable Protector Pack Of 4')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(Fields.alp + str(x) + keys.Keys.CONTROL + 'v')

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    GSTList = driver.find_elements(By.XPATH, Fields.GSTList)
    for r in  GSTList:
        if '18' == r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,200)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)
    driver.implicitly_wait(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//input[@id="length_size"]').click()
    time.sleep(1)
    LengthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in LengthSizeList:
        if '10' == r.text:
            r.click()
            break



def BluetoothHeadPhoneProductDetails(driver):
    print('Action : BluetoothHeadPhone Product Details')

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg3)


    # BatteryChargeTime
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.BatteryChargeTime).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    BatteryChargeTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in BatteryChargeTimeList:
        if '3 Hours' == r.text:
            r.click()
            break

    # Color
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Color).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'Black' == r.text:
            r.click()
            break

    # Compatibility
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Compatibility).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    CompatibilityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CompatibilityList:
        if 'All Smartphone' in r.text:
            r.click()
            break

    # ModelName
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.ModelName).send_keys('2in1')

    # PlayTime
    driver.find_element(By.XPATH, Fields.PlayTime).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    PlayTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PlayTimeList:
        if '8 Hours' == r.text:
            r.click()
            break

    # Type
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Type).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'In The Ear' in r.text:
            driver.implicitly_wait(2)
            r.click()
            break


    # WarrantyPeriod
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WarrantyPeriod).click()
    # time.sleep(1)
    driver.implicitly_wait(2)
    WarrantyPeriodList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyPeriodList:
        if '1 Year' == r.text:
            r.click()
            break

    # WarrentyType
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WarrentyType).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    WarrentyTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrentyTypeList:
        if 'Carry In' in r.text:
            r.click()
            break


    # WaterResistance
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.WaterResistance).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    WaterResistanceList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WaterResistanceList:
        if 'Yes' == r.text:
            r.click()
            break


    # Country
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(2)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break

    # Manufacture Details
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')


def BluetoothHeadPhoneOtherAttributes(driver):
    print('Action : BluetoothHeadPhone Other Details')

    # # Bluetooth Range
    # driver.find_element(By.XPATH, Fields.BluetoothRange).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # BluetoothRangeList = driver.find_elements(By.XPATH, Fields.BluetoothRangeList)
    # for r in BluetoothRangeList:
    #     if '10m' in r.text:
    #         r.click()
    #         break

    # BluetoothVersion
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.BluetoothVersion).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BluetoothVersionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in BluetoothVersionList:
        if '5.1' in r.text:
            r.click()
            break

    # ChargingType
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.ChargingType).click()
    # time.sleep(1)
    driver.implicitly_wait(2)
    ChargingTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ChargingTypeList:
        if 'Micro USB' in r.text:
            r.click()
            break

    # Frequency
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Frequency).click()
    # time.sleep(1)
    driver.implicitly_wait(2)
    FrequencyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in FrequencyList:
        if '10 Hz' in r.text:
            r.click()
            break

    # Material
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Material).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MaterialList:
        if 'ABS Plastic' in r.text:
            r.click()
            break

    # Mic
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.Mic).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    MicList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MicList:
        if 'Yes' in r.text:
            r.click()
            break

    # NetQuantity
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '1' in r.text:
            r.click()
            break

    # NoiceCancelation
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, Fields.NoiceCancelation).click()
    time.sleep(1)
    driver.implicitly_wait(2)
    NoiceCancelationList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NoiceCancelationList:
        if 'Yes' in r.text:
            r.click()
            break

    # Description
    clipboard.copy(r'Bluetooth version: 4.0 + EDR Bluetooth Profile: HFP 1.6, HSP 1.2, AVRCP 1.4, A2DP 1.2 NOISE REDUCTION: CVC6.0 INTELLIGENT Sound Mode: Stereo Operating Distance: 10 meters Charging time: about 1 hours Standby time: about 20 hours Talk/Playing time: 2.5 hours Power Source: Built-in Rechargeable Li-ion Battery Size: 40 x 24 x 32 mm / 1.58 x 0.95 x 1.26 inch Net Weight: 16.4 g HOW TO PAIR WITH: 1.Power on & Enter paring mode: Press the "power on" button for 5 seconds until the Blue LED light and Red LED light quickly flash alternatively (with "paring" voice) (Please don\'t stop pressing the button if you only see the Blue light flashing!!) 2.Use a bluetooth function mobile phone or other bluetooth master device. 3.Try to search the device and connect it(with "connected" voice). 4.Press the "power on" button once while the call is coming / end call. Latest Wireless Bluetooth 4.1 Technology with A2DP stereo music and AptX pure, clear sound, ideal for high quality music while running, jogging, cycling, skating, etc Good noise isolation to create the optimal environment for listening to your favorite tunes, built-in microphone with noise cancellation for clear calling and friends chatting Sweat-proof, light weight and ergonomic design to enhance your comfort; comes with interchangeable earbuds and ear hooks for secure and personal fit when walking or exercising Built-in rechargeable Lithium battery lasts up to 2 hours of talk / play time or 15 hours standby, universally compatible with most Bluetooth-enabled phones. Works with iPhone, iPad, Android and Windows Smartphones tablets and other Bluetooth devices')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')