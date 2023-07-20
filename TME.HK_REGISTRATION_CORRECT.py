from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import string
import sqlite3
import imaplib
import email

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

sql = sqlite3.connect('TMEHK.db')
cursor = sql.cursor()
cursor.execute("SELECT value FROM used_values WHERE parameter='email';")
email_value = cursor.fetchone()[0]
cursor.execute(f"UPDATE used_values SET value = {chosen_value + 1}")
sql.commit()
sql.close()

def get_random_value(length, type="string"):
    if type == "string":
        letters = string.ascii_letters
        result_value = ''.join(random.choice(letters) for _ in range(length))
    elif type == "number":
        digits = string.digits
        result_value = ''.join(random.choice(digits) for _ in range(length))
    else:
        raise ValueError("Invalid type. Use 'string' or 'number'.")

    return result_value


#driver.get('https://www.tme.hk/en/register')
#time.sleep(1)

#driver.find_element(By.ID, 'cookies-consent-close-icon').click()
#time.sleep(1)

field_1 = 'app_company_user_company_name'
field_2 = 'app_company_user_company_email'
field_3 = 'app_company_user_company_phoneNumber'
field_4 = 'app_company_user_company_city'
field_5 = 'app_company_user_company_street'
field_6 = 'app_company_user_company_postcode'
field_7 = 'app_company_user_jobTitle'
field_8 = 'app_company_user_customer_email'
field_9 = 'app_company_user_customer_phoneNumber'
field_10 = 'app_company_user_customer_firstName'
field_11 = 'app_company_user_customer_lastName'

company_name = get_random_value(5, "string")
company_email = f'chinacustomertme+{email_value}@gmail.com'
company_phone =