import clipboard
import time

from argon2 import Type
from selenium.webdriver.common.by import By
from Fields import Sunglass_Fields as Fields
from selenium.webdriver.common import keys




def Sunglass_InventoryDetails(driver,x):
    # ---------------------- Price, Size and Inventory ---------------------------------
    print("Action : Sunglass Inventory Details")
    # Meesho Price
    driver.find_element(By.XPATH, Fields.MeeshoPrice).send_keys('140')



    # Return price
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys(keys.Keys.CONTROL + 'a' + keys.Keys.BACK_SPACE)
    driver.find_element(By.XPATH, Fields.ReturnPrice).send_keys('135')

    # MRP
    driver.find_element(By.XPATH, Fields.MRP).send_keys('999')

    # HSN Code
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.HSNCode).click()

    driver.implicitly_wait(1)
    HSNCodeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in HSNCodeList:
        if '9004' == r.text:
            r.click()
            break


    driver.implicitly_wait(1)

    # GST
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.GST).click()
    GSTList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in GSTList:
        if '18' == r.text:
            r.click()
            break


    # Net Weight
    driver.find_element(By.XPATH, Fields.Weight).send_keys('200')



    # Product Name
    clipboard.copy(x+' Men\'s Combo of Black Color Belt with Black Sunglass {B2+S2}')
    driver.find_element(By.XPATH, Fields.ProductName).send_keys(keys.Keys.CONTROL + 'v')



    driver.execute_script("window.scrollBy(0,500)", "")

    # Size
    driver.find_element(By.XPATH, Fields.Size).click()
    time.sleep(1)
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//ul[@role='menu']/div[2]/div//*[name()='svg']").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, '//div[@role="presentation"]//button[2]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//input[@id="inventory"]').send_keys('1000')



def Sunglass_ProductDetails(driver):

    print("Action : Sunglass Product Details")

    # Frame_Color
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Frame_Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Frame_ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in Frame_ColorList:
        if 'Black' in r.text:
            r.click()
            break

    # Frame_Material
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Frame_Material).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Frame_MaterialList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in Frame_MaterialList:
        if 'Fiber' in r.text:
            r.click()
            break

    # Frame_Type
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Frame_Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Frame_TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in Frame_TypeList:
        if 'Full-rim' in r.text:
            r.click()
            break



    # Lens_Color
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Lens_Color).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Lens_ColorList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in Lens_ColorList:
        if 'Black' in r.text:
            r.click()
            break

    # Lens_Type
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Lens_Type).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Lens_TypeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    # driver.find_element(By.XPATH, Fields.Search).send_keys('4')
    # time.sleep(2)
    for r in Lens_TypeList:
        if 'Polarized' in r.text:
            r.click()
            break


    # NetQuantity
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.NetQuantity).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    NetQuantityList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in NetQuantityList:
        if '2' in r.text:
            r.click()
            break

    # Shape
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Shape).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    ShapeList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in ShapeList:
        if 'Rectangular' in r.text:
            r.click()
            break


    # Country_Of_Origin
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Country_Of_Origin).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    Country_Of_OriginList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in Country_Of_OriginList:
        if 'India' in r.text:
            r.click()
            break


    # Manufacture Details
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Manufacture_Details).send_keys('ASDF')

    # Package Details
    driver.find_element(By.XPATH, Fields.Packer_Details).send_keys('ASDFG')

    driver.execute_script("window.scrollBy(0, 500)", "")



def Sunglass_OtherAttributes(driver):

    print("Action : Sunglass Other Attributes")


    driver.implicitly_wait(1)
    # Occasion
    driver.find_element(By.XPATH, Fields.Occasion).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    OccasionList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in OccasionList:
        if 'Style' in r.text:
            r.click()
            break

    # Warranty
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, Fields.Warranty).click()
    # time.sleep(1)
    driver.implicitly_wait(1)
    WarrantyList = driver.find_elements(By.XPATH, Fields.DropDownList)
    for r in WarrantyList:
        if '12' in r.text:
            r.click()
            break


    # Description
    driver.implicitly_wait(1)
    clipboard.copy("Men's Combo of Black Color Belt with Black Sunglass {B2+S2}")
    driver.find_element(By.XPATH, Fields.Description).send_keys(keys.Keys.CONTROL + 'v')