import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get('https://www.tme.hk/en/register')
time.sleep(2)

driver.find_element(By.ID, 'cookies-consent-close-icon').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[15]/button').click()
time.sleep(2)

xpath_1 = '/html/body/div[1]/section[2]/div/form/div[1]/div'
xpath_2 = '/html/body/div[1]/section[2]/div/form/div[2]/div'
xpath_3 = '/html/body/div[1]/section[2]/div/form/div[3]/div'
xpath_4 = '/html/body/div[1]/section[2]/div/form/div[5]/div/div'
xpath_5 = '/html/body/div[1]/section[2]/div/form/div[6]/div'
xpath_6 = '/html/body/div[1]/section[2]/div/form/div[7]/div/div'
xpath_7 = '/html/body/div[1]/section[2]/div/form/div[9]/div'
xpath_8 = '/html/body/div[1]/section[2]/div/form/div[10]/div'
xpath_9 = '/html/body/div[1]/section[2]/div/form/div[11]/div'
xpath_10 = '/html/body/div[1]/section[2]/div/form/div[12]/div'

obligatory_validation_1 = driver.find_element(By.XPATH, xpath_1)
obligatory_validation_2 = driver.find_element(By.XPATH, xpath_2)
obligatory_validation_3 = driver.find_element(By.XPATH, xpath_3)
obligatory_validation_4 = driver.find_element(By.XPATH, xpath_4)
obligatory_validation_5 = driver.find_element(By.XPATH, xpath_5)
obligatory_validation_6 = driver.find_element(By.XPATH, xpath_6)
obligatory_validation_7 = driver.find_element(By.XPATH, xpath_7)
obligatory_validation_8 = driver.find_element(By.XPATH, xpath_8)
obligatory_validation_9 = driver.find_element(By.XPATH, xpath_9)
obligatory_validation_10 = driver.find_element(By.XPATH, xpath_10)

for i in range(1, 11):
    variable_name = 'obligatory_validation_' + str(i)
    if globals().get(variable_name).is_displayed and globals().get(variable_name).text == 'This field is obligatory':
        print(f"OBLIGATORY VALIDATION {i} OK")
    else:
        print(f"OBLIGATORY VALIDATION {i} NOK")

company_name = driver.find_element(By.ID, "app_company_user_company_name")
company_name.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
company_name.send_keys(Keys.ENTER)
time.sleep(2)
length_validation_company = driver.find_element(By.XPATH, xpath_1)

if length_validation_company.is_displayed() and length_validation_company.text == 'The maximum length for the "Company" field is 120 characters.':
    print("COMPANY MAX LENGTH OK")
else:
    print("COMPANY MAX LENGTH NOK")

driver.refresh()
time.sleep(2)

company_name = driver.find_element(By.ID, "app_company_user_company_name")
company_name.send_keys("數產生ZHZH")
company_name.send_keys(Keys.ENTER)
time.sleep(2)
length_validation_company = driver.find_element(By.XPATH, xpath_1)

if length_validation_company.is_displayed() and length_validation_company.text == 'Please use only latin characters.':
    print("COMPANY LATIN ONLY OK")
else:
    print("COMPANY LATIN ONLY NOK")

