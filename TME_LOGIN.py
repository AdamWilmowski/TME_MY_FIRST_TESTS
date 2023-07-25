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
    if (pop_up.text == 'Login or password is incorrect' and
       pop_up.value_of_css_property("background-color") == 'rgba(175, 9, 9, 1)'):
        print("POP-UP INFO PRESENT, CORRECT TEXT AND COLOR")
    else:
        print('POP-UP NOT CORRECT')

except NoSuchElementException:
    print("JOB NOT OBLIGATORY OK")

driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)
driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)

#try:
    #captcha = driver.find_element(By.ID, r'captcha_\S+')

#except NoSuchElementException:
    #print('NO CAPTCHA FOUND')

