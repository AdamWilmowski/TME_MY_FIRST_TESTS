from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re
import random
import sqlite3

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

sql = sqlite3.connect('TMEHK.db')
cursor = sql.cursor()
cursor.execute("SELECT COUNT(*) FROM customers;")
number_of_customers = cursor.fetchone()[0]
selected_customer = random.randint(1, number_of_customers)
customer_email = f'chinacustomertme+{selected_customer}@gmail.com'
sql.close()

driver.get('https://www.tme.hk/en/login')
driver.find_element(By.ID, 'cookies-consent-close-icon').click()
driver.find_element(By.ID, '_username').send_keys('xxxx')
driver.find_element(By.ID, '_password').send_keys('xxxx')
driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)

try:
    pop_up = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[1]')
    if (pop_up.is_displayed() and pop_up.text == 'Login or password is incorrect' and
            pop_up.value_of_css_property("background-color") == 'rgba(175, 9, 9, 1)'):
        print("POP-UP INFO PRESENT, CORRECT TEXT AND COLOR")
    else:
        print('POP-UP NOT CORRECT')

except NoSuchElementException:
    print("POP-UP NOT FOUND")

driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)
driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)

try:
    captcha = driver.find_element(By.CLASS_NAME, 'captcha_image')
    if (captcha.is_displayed() and captcha.value_of_css_property('width') == '200px'
            and captcha.value_of_css_property('height') == '60px'):
        print("CAPTCHA DISPLAYED CORRECTLY")
    else:
        print('CAPTCHA NOT DISPLAYED CORRECTLY')

except NoSuchElementException:
    print('NO CAPTCHA FOUND')

driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)
captcha_input = driver.find_element(By.ID, 'captcha')
captcha_validation = driver.find_element(By.XPATH, '/html/body/div[1]/section[2]/div/form/div[3]/span')

if (captcha_input.value_of_css_property('color') == 'rgba(159, 58, 56, 1)' and
        captcha_validation.value_of_css_property('color') == 'rgba(175, 9, 9, 1)' and
        captcha_validation.text == 'The signs do not match' and
        captcha_validation.value_of_css_property('font-size') == '14px'):
    print('CAPTCHA VALIDATION CORRECT')
else:
    print('CAPTCHA VALIDATION INCORRECT')

driver.find_element(By.ID, '_username').send_keys(customer_email)
driver.find_element(By.ID, '_password').send_keys('1qaz@WSX')
time.sleep(10)
driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)

driver.get('tme.hk/en/account/dashboard')
assert driver.current_url == 'tme.hk/en/account/dashboard'
driver.close()
