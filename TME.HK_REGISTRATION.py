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

field_1 = 'app_company_user_company_name'
field_2 = 'app_company_user_company_email'
field_3 = 'app_company_user_company_email'
field_4 = 'app_company_user_company_city'
field_5 = 'app_company_user_company_street'
field_6 = 'app_company_user_company_postcode'
field_7 = 'app_company_user_jobTitle'
field_8 = 'app_company_user_customer_email'
field_9 = 'app_company_user_customer_phoneNumber'
field_10 = 'app_company_user_customer_firstName'
field_11 = 'app_company_user_customer_lastName'

for i in range(1, 11):
    xpath = globals()["xpath_" + str(i)]
    obligatory_validation = driver.find_element(By.XPATH, xpath)
    if obligatory_validation.is_displayed() and obligatory_validation.text == 'This field is obligatory':
        print(f"OBLIGATORY VALIDATION {i} OK")
    else:
        print(f"OBLIGATORY VALIDATION {i} NOK")

company_name = driver.find_element(By.ID, "app_company_user_company_name")
company_name.clear()
company_name.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "
                       "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
company_name.send_keys(Keys.ENTER)
time.sleep(2)
length_validation_company = driver.find_element(By.XPATH, xpath_1)

if length_validation_company.is_displayed() and length_validation_company.text == 'The maximum length for the ' \
                                                                                  '"Company" field is 120 characters.':
    print("COMPANY MAX LENGTH OK")
else:
    print("COMPANY MAX LENGTH NOK")

driver.refresh()
time.sleep(2)

company_name = driver.find_element(By.ID, field_1)
company_name.clear()
company_name.send_keys("數產生ZHZH")
company_name.send_keys(Keys.ENTER)
time.sleep(2)
length_validation_company = driver.find_element(By.XPATH, xpath_1)

if length_validation_company.is_displayed() and length_validation_company.text == 'Please use only latin characters.':
    print("COMPANY LATIN ONLY OK")
else:
    print("COMPANY LATIN ONLY NOK")

driver.refresh()
time.sleep(2)

company_email = driver.find_element(By.ID, field_2)
company_email.clear()
company_email.send_keys("xx.cc")
company_email.send_keys(Keys.ENTER)
time.sleep(2)
format_email_validation = driver.find_element(By.XPATH, xpath_2)

if format_email_validation.is_displayed() and format_email_validation.text == "Invalid format. Please enter a " \
                                                                                  "valid e-mail address, for example " \
                                                                                  "smith@domain.cn":
    print("COMPANY EMAIL FORMAT ONLY OK")
else:
    print("COMPANY EMAIL FORMAT NOK")

driver.refresh()
time.sleep(2)

company_email = driver.find_element(By.ID, field_2)
company_email.clear()
company_email.send_keys("數產生")
company_email.send_keys(Keys.ENTER)
time.sleep(2)
latin_email_validation = driver.find_element(By.XPATH, xpath_2)

if latin_email_validation.is_displayed() and latin_email_validation.text == "Please use only latin characters.":
    print("COMPANY EMAIL LATIN ONLY OK")
else:
    print("COMPANY EMAIL LATIN ONLY NOK")

driver.refresh()
time.sleep(2)

company_email = driver.find_element(By.ID, field_2)
company_email.clear()
company_email.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX "
                       "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@XX.com")
company_email.send_keys(Keys.ENTER)
time.sleep(2)
email_max_length_validation = driver.find_element(By.XPATH, xpath_2)

if email_max_length_validation.is_displayed() and email_max_length_validation.text == 'The maximum length for the ' \
                                                                                      '"E-mail" ' \
                                                                            'field is 64 characters.':
    print("COMPANY EMAIL MAX LENGTH OK")
else:
    print("COMPANY EMAIL MAX LENGTH NOK")

driver.refresh()
time.sleep(2)

company_phone_number = driver.find_element(By.ID, field_3)
company_phone_number.clear()
company_phone_number.send_keys("1234567")
company_phone_number.send_keys(Keys.ENTER)
time.sleep(2)
company_phone_min_validation = driver.find_element(By.XPATH, xpath_3)

if company_phone_min_validation.is_displayed() and company_phone_min_validation.text == 'The field must contain a ' \
                                                                                        'minimum of 11 digits.':
    print("COMPANY PHONE NUMBER MIN LENGTH OK")
else:
    print("COMPANY PHONE NUMBER MIN LENGTH NOK")

driver.refresh()
time.sleep(2)

company_phone_number = driver.find_element(By.ID, field_3)
company_phone_number.clear()
company_phone_number.send_keys("1234567891011121314")
company_phone_number.send_keys(Keys.ENTER)
time.sleep(2)
company_phone_max_validation = driver.find_element(By.XPATH, xpath_3)

if company_phone_max_validation.is_displayed() and company_phone_max_validation.text == 'The maximum length for the ' \
                                                                                        '"Phone Number" field is 15 ' \
                                                                                        'digits"':
    print("COMPANY PHONE NUMBER MAX LENGTH OK")
else:
    print("COMPANY PHONE NUMBER MAX LENGTH NOK")

driver.refresh()
time.sleep(2)

company_city = driver.find_element(By.ID, field_4)
company_city.clear()
company_city.send_keys("1234567891011121314")
company_city.send_keys(Keys.ENTER)
time.sleep(2)
company_phone_max_validation = driver.find_element(By.XPATH, xpath_3)

if company_phone_max_validation.is_displayed() and company_phone_max_validation.text == 'The maximum length for the ' \
                                                                                        '"Phone Number" field is 15 ' \
                                                                                        'digits"':
    print("COMPANY PHONE NUMBER MAX LENGTH OK")
else:
    print("COMPANY PHONE NUMBER MAX LENGTH NOK")











