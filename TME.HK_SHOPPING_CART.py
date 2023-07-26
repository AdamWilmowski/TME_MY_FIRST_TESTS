from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re
import random
import sqlite3

#sku_1 = input('Enter the SKU of first product: ')
#sku_2 = input('Enter the SKU of second product: ')

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get(f'https://www.tme.hk/en/product/BZX585-C15.115')
driver.find_element(By.ID, 'cookies-consent-close-icon').click()
price_raw_1 = float(driver.find_element(By.XPATH, '//*[@id="sylius-product-selecting-variant"]/div/div[1]/table/tbody/tr[1]/td[3]').text)
  time.sleep(1)
driver.get(f'https://www.tme.hk/en/product/TGL41-6.8A-DIO')
price_raw_2 = float(driver.find_element(By.XPATH, '//*[@id="sylius-product-selecting-variant"]/div/div[1]/table/tbody/tr[1]/td[3]').text)
driver.find_element(By.XPATH, '//*[@id="sylius-product-adding-to-cart"]/button[1]').click()
time.sleep(1)


def generate_cart_variables(number):
    field = driver.find_element(By.XPATH, f'/html/body/div[1]/div[4]/main/div/div/section[1]/div[2]/div[{number}]').text
    values_list = field.split('\n')
    for idx, value in enumerate(values_list):
        var_name = f"variable_{idx+1}"
        globals()[var_name] = value


driver.get('https://www.tme.hk/en/cart')
generate_cart_variables(1)

