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
import re
import os

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

sql = sqlite3.connect('TMEHK.db')
cursor = sql.cursor()
cursor.execute("SELECT value FROM used_values WHERE parameter='email';")
email_value = cursor.fetchone()[0]
cursor.execute(f"UPDATE used_values SET value = {email_value + 1}")
sql.commit()


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


def get_hyperlinks_from_first_email(username, password, server, mailbox="INBOX"):
    try:
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)

        mail.select(mailbox)

        _, data = mail.search(None, '(SUBJECT "Welcome to TME")')
        email_ids = data[0].split()

        if not email_ids:
            print("No emails found in the mailbox.")
            return []

        first_email_id = email_ids[-1]
        _, msg_data = mail.fetch(first_email_id, "(RFC822)")
        raw_email = msg_data[0][1]

        msg = email.message_from_bytes(raw_email)

        hyperlinks = []

        for part in msg.walk():
            if part.get_content_type() == "text/html":
                email_content = part.get_payload(decode=True).decode("utf-8")

                links = re.findall(r"\b(https?://\S+)\b", email_content)
                hyperlinks.extend(links)

        return hyperlinks

    except Exception as e:
        print("Error:", e)

    finally:
        mail.logout()


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
radiobutton_1 = 'app_company_user_agreements_159_approved_0'

company_name = get_random_value(8, "string")
company_email = f'chinacustomertme+{email_value}@gmail.com'
company_phone = get_random_value(12, "number")
company_city = get_random_value(8, "string")
company_street = get_random_value(12, "string")
company_zip = get_random_value(6,"number")
customer_job = "director"
customer_email = f'chinacustomertme+{email_value}@gmail.com'
customer_phone = get_random_value(13, "number")
customer_name = get_random_value(6, "string")
customer_surname = get_random_value(7, "string")

driver.get('https://www.tme.hk/en/register')
time.sleep(1)

driver.find_element(By.ID, 'cookies-consent-close-icon').click()
time.sleep(1)

driver.find_element(By.ID, field_1).send_keys(company_name)
driver.find_element(By.ID, field_2).send_keys(company_email)
driver.find_element(By.ID, field_3).send_keys(company_phone)
driver.find_element(By.ID, field_4).send_keys(company_city)
driver.find_element(By.ID, field_5).send_keys(company_street)
driver.find_element(By.ID, field_6).send_keys(company_zip)
driver.find_element(By.ID, field_7).send_keys(customer_job)
driver.find_element(By.ID, field_8).send_keys(customer_email)
driver.find_element(By.ID, field_9).send_keys(customer_phone)
driver.find_element(By.ID, field_10).send_keys(customer_name)
driver.find_element(By.ID, field_11).send_keys(customer_surname)
driver.find_element(By.ID, radiobutton_1).click()
time.sleep(10)
driver.find_element(By.ID, field_11).send_keys(Keys.ENTER)
time.sleep(1)

thank_you_page = driver.current_url
assert thank_you_page == 'https://www.tme.hk/en/register/welcome'

insert_query = "INSERT INTO customers (company_name, company_email, company_phone, company_city, company_street, " \
               "company_zip, customer_job, customer_email, customer_phone, customer_name, customer_surname) VALUES (" \
               "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
cursor.execute(insert_query, (company_name, company_email, company_phone, company_city, company_street, company_zip,
                              customer_job, customer_email, customer_phone, customer_name, customer_surname))
sql.commit()
sql.close()

for i in range(1, 13):
    globals()[f"xpath_{i}"] = f"/html/body/div[1]/div[4]/section/div[{i}]/span[2]"

thank_you_check = [driver.find_element(By.XPATH, xpath_1).text == company_name,
        driver.find_element(By.XPATH, xpath_2).text == company_email,
        driver.find_element(By.XPATH, xpath_3).text == company_phone,
        driver.find_element(By.XPATH, xpath_4).text == "China",
        driver.find_element(By.XPATH, xpath_5).text == company_city,
        driver.find_element(By.XPATH, xpath_6).text == company_street,
        driver.find_element(By.XPATH, xpath_7).text == company_zip,
        driver.find_element(By.XPATH, xpath_8).text == customer_job,
        driver.find_element(By.XPATH, xpath_9).text == customer_email,
        driver.find_element(By.XPATH, xpath_10).text == customer_phone,
        driver.find_element(By.XPATH, xpath_11).text == customer_name,
        driver.find_element(By.XPATH, xpath_12).text == customer_surname]

if all(thank_you_check):
    print('THANK YOU PAGE OK')
else:
    print('THANK YOU PAGE NOK')

time.sleep(15)

username = "adam.wilmowski@zohomail.eu"
password = os.environ.get("password_1")
imap_server = "imap.zoho.eu"

hyperlinks = get_hyperlinks_from_first_email(username, password, imap_server)
hyperlink = hyperlinks[7]

driver.get(hyperlink)
time.sleep(1)

driver.find_element(By.ID, 'app_user_set_password_password_first').send_keys(os.environ.get("password_2"))
driver.find_element(By.ID, 'app_user_set_password_password_second').send_keys(os.environ.get("password_2"))
driver.find_element(By.XPATH, '//button[text()="Save"]').send_keys(Keys.ENTER)
time.sleep(1)

assert driver.current_url == 'https://www.tme.hk/en/login'
driver.find_element(By.ID, '_username').send_keys(customer_email)
driver.find_element(By.ID, '_password').send_keys(os.environ.get("password_2"))
driver.find_element(By.ID, '_password').send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//button[text()="Login"]').send_keys(Keys.ENTER)
time.sleep(1)

assert driver.current_url == 'https://www.tme.hk/en/account/agreements'
driver.get('https://www.tme.hk/en/account/dashboard')

for i in range(1, 4):
    globals()[f"company_xpath_{i}"] = f'//*[@id="customer-information"]/div[2]/table/tbody/tr[{i}]/td[2]'

if driver.find_element(By.XPATH, company_xpath_1).text == company_name:
    print("COMPANY NAME CORRECT")
else:
    print("COMPANY NAME INCORRECT")

if driver.find_element(By.XPATH, company_xpath_2).text == company_email:
    print('COMPANY EMAIL CORRECT')
else:
    print('COMPANY EMAIL INCORRECT')

if driver.find_element(By.XPATH, company_xpath_3).text == company_phone:
    print('COMPANY PHONE CORRECT')
else:
    print('COMPANY PHONE INCORRECT')

for i in range(1, 5):
    globals()[f"customer_xpath_{i}"] = f'//*[@id="customer-information"]/div[3]/table/tbody/tr[{i}]/td[2]'

if driver.find_element(By.XPATH, customer_xpath_1).text == customer_name:
    print('CUSTOMER NAME CORRECT')
else:
    print('CUSTOMER NAME INCORRECT')

if driver.find_element(By.XPATH, customer_xpath_2).text == customer_surname:
    print('CUSTOMER SURNAME CORRECT')
else:
    print('CUSTOMER SURNAME INCORRECT')

if driver.find_element(By.XPATH, customer_xpath_3).text == customer_email:
    print('CUSTOMER EMAIL CORRECT')
else:
    print('CUSTOMER EMAIL INCORRECT')

if driver.find_element(By.XPATH, customer_xpath_4).text == customer_phone:
    print('CUSTOMER PHONE CORRECT')
else:
    print('CUSTOMER PHONE INCORRECT')

driver.get('https://www.tme.hk/en/account/address-book')
time.sleep(1)

if driver.find_element(By.XPATH, '//*[@id="sylius-default-address"]/div/p[1]').text == company_name:
    print('ADDRESS BOOK COMPANY CORRECT')
else:
    print('ADDRESS BOOK COMPANY INCORRECT')

if driver.find_element(By.XPATH, '//*[@id="sylius-default-address"]/div/p[3]').text == company_street:
    print('ADDRESS BOOK STREET CORRECT')
else:
    print('ADDRESS BOOK STREET INCORRECT')

if driver.find_element(By.XPATH, '//*[@id="sylius-default-address"]/div/p[4]').text == f'T: {company_phone}':
    print('ADDRESS BOOK PHONE CORRECT')
else:
    print('ADDRESS BOOK PHONE INCORRECT')
