import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

obligatory_validation_1 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[1]/div')
obligatory_validation_2 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[2]/div')
obligatory_validation_3 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[3]/div')
obligatory_validation_4 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[5]/div/div')
obligatory_validation_5 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[6]/div')
obligatory_validation_6 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[7]/div/div')
obligatory_validation_7 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[9]/div')
obligatory_validation_8 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[10]/div')
obligatory_validation_9 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[11]/div')
obligatory_validation_10 = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[12]/div')

if obligatory_validation_1.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 1 OK")
else:
    print("Field 1 NOK")

if obligatory_validation_2.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 2 OK")
else:
    print("Field 2 NOK")

if obligatory_validation_3.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 3 OK")
else:
    print("Field 3 NOK")

if obligatory_validation_4.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 4 OK")
else:
    print("Field 4 NOK")

if obligatory_validation_5.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 5 OK")
else:
    print("Field 5 NOK")

if obligatory_validation_6.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 6 OK")
else:
    print("Field 6 NOK")

if obligatory_validation_7.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 7 OK")
else:
    print("Field 7 NOK")

if obligatory_validation_8.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 8 OK")
else:
    print("Field 8 NOK")

if obligatory_validation_9.is_displayed() and obligatory_validation_1.text == 'This field is obligatory':
    print("Field 9 OK")
else:
    print("Field 9 NOK")

if obligatory_validation_10.is_displayed() and obligatory_validation_10.text == 'This field is obligatory':
    print("Field 10 OK")
else:
    print("Field 10 NOK")