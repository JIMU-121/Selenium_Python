import time
import os
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from ExtractImages import FetchingImages
from Products import Fields, Actions, Categories
from Actions import TrimmerAction as Action
from openpyxl import Workbook, load_workbook





# Files Path
ProImgDir = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\809 + cp\\images'
SlideImagesPath = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\809 + cp\\slide'
path = 'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\809 + cp'
# SlideImg1 = 'C:/Users/bhatt/Downloads/Telegram Desktop/folder 8/slide/img1.jpg'
# SlideImg2 = 'C:/Users/bhatt/Downloads/Telegram Desktop/folder 8/slide/img2.jpg'
# SlideImg3 = 'C:/Users/bhatt/Downloads/Telegram Desktop/folder 8/slide/OIP.jpeg'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('https://supplier.meesho.com/')
driver.maximize_window()


wb = load_workbook('Products.xlsx')
ws = wb.active
row = 1
col = 1
n = 880
ibtn = 1
# 810
if __name__ == '__main__':
    Actions.Login(driver)
    images = FetchingImages.ProductImages(ProImgDir)
    for x in images:

        SlideImages = FetchingImages.SlideImages(SlideImagesPath)
        print(type(SlideImages))




        AddSingleCatlog = driver.find_element(By.XPATH, '//*[@id="mainWrapper"]/div/div[1]/div[2]/div[1]/div[1]/div/button[2]')
        AddSingleCatlog.click()

        # time.sleep(7)
        driver.implicitly_wait(7)

        Categories.Trimmer(driver)

        # Upload Product Front Image
        UploadProdImage = driver.find_element(By.XPATH, '//*[@id="addImages"]').send_keys(x)


        # time.sleep(5)
        driver.implicitly_wait(15)

        # Clicking to Continue button
        AfterSelectingPhoto = driver.find_element(By.XPATH,
                                                              '//button[@class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root css-1n1ggul"]')
        AfterSelectingPhoto.click()

        # time.sleep(8)
        driver.implicitly_wait(15)

        # i Button
        if ibtn <= 4:
            driver.find_element(By.XPATH, '//p[normalize-space()="Wrong/Defective Returns Price"]//parent::div//parent::div/div[2]/div/div/div/div').click()

        time.sleep(2)

        print(str(x)+' '+str(n))

        driver.execute_script("window.scrollBy(0,500)", "")
        UploadSlideImages = driver.find_element(By.XPATH, '//input[@id="addMoreImagesInput"]')

        # Upload Product Slide Image
        for s in SlideImages:
            UploadSlideImages.send_keys(s)
            time.sleep(2)

        # UploadSlideImages.send_keys(SlideImg2)
        # UploadSlideImages.send_keys(SlideImg3)





        Action.TrimmerInventoryDetails(driver, n)

        # driver.execute_script("arguments[0].scrollIntoView();", Fields.PackageDetail)
        driver.execute_script("window.scrollBy(0,500)", "")

        Action.TrimmerProductDetails(driver)



        # driver.execute_script("arguments[0].scrollIntoView();", Fields.Description)

        Action.TrimmerOtherAttributes(driver)

        ws.cell(row=row, column=col).value = str(x) + ' ' + str(n)
        row += 1
        n += 1
        ibtn += 1

        SubmitButton = '//button[@class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root css-16z39kb"]'
        driver.find_element(By.XPATH, SubmitButton).click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[@class="MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButtonBase-root css-1bc15yu"]').click()
        # os.replace(x, destination)
        # time.sleep(10)
        driver.implicitly_wait(15)
        print('Done')
        destination = path+'\\'+os.path.basename(x)
        os.replace(x, destination)
        print('File'+os.path.basename(x)+'has been moved to destination '+destination)
        wb.save('Products.xlsx')
