import  clipboard
import time
from selenium.webdriver.common.by import By
from Fields import TrimmerFields as Fields
from selenium.webdriver.common import keys





def TrimmerInventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------

    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('850')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('845')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('1999')

    # HSN Code
    driver.find_element(By.XPATH, Fields.HSNCode).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '8510' == r.text:
            r.click()
            break

    # time.sleep(1)
    driver.implicitly_wait(1)


    # Net Weight
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')

    # UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')
    # UploadSlideImages.send_keys(Fields.SlideImg2)


    # Product Name
    clipboard.copy('A Professional Rechargeable and Cordless Hair Clipper Trimmer 120 min Runtime 5 Length Settings & Cable Protector Pack Of 4')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(Fields.alp+str(x) + keys.Keys.CONTROL + 'v')

    # GST
    driver.find_element(By.XPATH, Fields.GST).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    GSTList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in  GSTList:
        if '18' == r.text:
            r.click()
            break

    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@class="MuiBox-root css-759u60"]//*[name()="svg"]').click()
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')
    driver.find_element(By.XPATH, Fields.LengthSize).click()
    time.sleep(1)
    LengthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in LengthSizeList:
        if '10' == r.text:
            r.click()
            break

    driver.find_element(By.XPATH, Fields.WidthSize).click()
    time.sleep(1)
    WidthSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WidthSizeList:
        if '1' == r.text:
            r.click()
            break





def TrimmerProductDetails(driver):


    # Country
    driver.find_element(By.XPATH, Fields.Country).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    CountryList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in CountryList:
        if 'India' in r.text:
            r.click()
            break


    # BatteryRunTime
    driver.find_element(By.XPATH, Fields.BatteryRunTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    BatteryRunTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in BatteryRunTimeList:
        if '100 Mins' in r.text:
            r.click()
            break




    # Manufacture Details
    driver.find_element(By.XPATH, Fields.Manufacture).send_keys('ASD')

    # Package Details
    driver.find_element(By.XPATH, Fields.PackageDetail).send_keys('ASD')
    driver.execute_script("window.scrollBy(0,200)", "")


def TrimmerOtherAttributes(driver):


    # AdjustableTrimmingRange
    driver.find_element(By.XPATH, Fields.AdjustableTrimmingRange).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    AdjustableTrimmingRangeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in AdjustableTrimmingRangeList:
        if '12 mm' in r.text:
            r.click()
            break

    # ChargingTime
    driver.find_element(By.XPATH, Fields.ChargingTime).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ChargingTimeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ChargingTimeList:
        if '9 Hours' in r.text:
            r.click()
            break

    # ClipSize
    driver.find_element(By.XPATH, Fields.ClipSize).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ClipSizeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ClipSizeList:
        if '12 mm' in r.text:
            r.click()
            break

    # Color
    driver.find_element(By.XPATH, Fields.Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ColorList:
        if 'White' in r.text:
            r.click()
            break

    # Frequency
    driver.find_element(By.XPATH, Fields.Frequency).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    FrequencyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in FrequencyList:
        if '100 Hz' in r.text:
            r.click()
            break

    # Material
    driver.find_element(By.XPATH, Fields.Material).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in MaterialList:
        if 'ABS Plastic' in r.text:
            r.click()
            break


    # # CordLength
    # driver.find_element(By.XPATH, Fields.CordLength).click()
    # # time.sleep(1)
    # driver.implicitly_wait(1)
    # CordLengthList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # for r in CordLengthList:
    #     if '1 Mtr' in r.text:
    #         r.click()
    #         break

    # IdealFor
    driver.find_element(By.XPATH, Fields.IdealFor).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    IdealForList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in IdealForList:
        if 'Unisex' in r.text:
            r.click()
            break

    # NetQuantity
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '1' in r.text:
            r.click()
            break

    # PowerConsumption
    driver.find_element(By.XPATH, Fields.PowerConsumption).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    PowerConsumptionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in PowerConsumptionList:
        if '100 Watts' in r.text:
            r.click()
            break

    # Type
    driver.find_element(By.XPATH, Fields.Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in TypeList:
        if 'Cordless' in r.text:
            r.click()
            break
    time.sleep(1)

    # Warranty
    driver.find_element(By.XPATH, Fields.Warranty).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyList:
        if '1 Year' in r.text:
            r.click()
            break

    # OperatingVoltage
    driver.find_element(By.XPATH, Fields.OperatingVoltage).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    OperatingVoltageList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in OperatingVoltageList:
        if '100 Volts' in r.text:
            r.click()
            break

    # Rechargeable
    driver.find_element(By.XPATH, Fields.Rechargeable).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    RechargeableList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in RechargeableList:
        if 'Yes' in r.text:
            r.click()
            break

    # UseableWhileCharging
    driver.find_element(By.XPATH, Fields.UseableWhileCharging).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    UseableWhileChargingList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in UseableWhileChargingList:
        if 'Yes' in r.text:
            r.click()
            break

    # WarrantyType
    driver.find_element(By.XPATH, Fields.WarrantyType).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyTypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyTypeList:
        if 'Repair' in r.text:
            r.click()
            break


    # Description
    clipboard.copy(r'Professional Rechargeable Hair Trimmer Electric Hair Clipper, Razor Trimmer 120 min Runtime 4 Length Settings Hair Trimmer, Clipper, Grooming Set For Men, Women. Whether You Need To Trim, Fade Or Manscape Your Facial Hair, The Ideal Way To Go About It By Using A CLIPPER. You Can Take A Look At This CLIPPER As It Allows You To Neatly And Precisely Trim Your Beard Just The Way You Want. Skin-Friendly High Performance This Cordless clipper Comes With Blades That Have Rounded Tips For A Smooth Contact Against Your Skin, reducing/Preventing Any Irritation. Also, These Blades Stay Extra-Sharp At All Times, Making It Easy For You To Trim The Hair Neatly And Effectively. Effortless Trimming To Get Your Desired Beard Look - 3-Day Shadow Look Of 1Mm Or Semi/Full Beard Of 3Mm. You Can Even Remove The Comb And Get A Zero Trim Look Of 0.5Mm As Well.')
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')