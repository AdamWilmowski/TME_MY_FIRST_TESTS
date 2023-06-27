from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

list_of_products = input('Please provide last part of link tme.cn/tme.hk category: ')


# generating list of xpaths for prices on tme.cn
def generate_xpath_list():
    xpath_list = []
    for i in range(1, 21):
        new_xpath = input_xpath.replace('X', str(i))
        xpath_list.append(new_xpath)
    return xpath_list


# xpath for price
input_xpath = '//*[@id="products-list-container"]/div[2]/table/tbody/tr[X]/td[2]/div/table/tbody/tr[1]/td[3]'
result = generate_xpath_list()

# change each element from xpath list into variable
for i, element in enumerate(result):
    xpath_name = f"xpath{i + 1}"
    exec(f"{xpath_name} = '{element}'")

# setting up chrome webdriver
driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# first action, opening tme.cn page, accepting cookies, showing only instock objects
driver.maximize_window()
driver.get(f'https://www.tme.cn/catalog/{list_of_products}')
close_cookies = driver.find_element(By.ID, "cookies-consent-close-icon")
close_cookies.click()
in_stock = driver.find_element(By.ID, "in_stock_filter")
in_stock.click()
# waiting for page to load
time.sleep(3)

# running test for each consecutive price
price1 = driver.find_element(By.XPATH, xpath1).text
price2 = driver.find_element(By.XPATH, xpath2).text
assert price1 > price2
price3 = driver.find_element(By.XPATH, xpath3).text
assert price2 > price3
price4 = driver.find_element(By.XPATH, xpath4).text
assert price3 > price4
price5 = driver.find_element(By.XPATH, xpath5).text
assert price4 > price5
price6 = driver.find_element(By.XPATH, xpath6).text
assert price5 > price6
price7 = driver.find_element(By.XPATH, xpath7).text
assert price6 > price7
price8 = driver.find_element(By.XPATH, xpath8).text
assert price7 > price8
price9 = driver.find_element(By.XPATH, xpath9).text
assert price8 > price9
price10 = driver.find_element(By.XPATH, xpath10).text
assert price9 > price10
price11 = driver.find_element(By.XPATH, xpath11).text
assert price10 > price11
price12 = driver.find_element(By.XPATH, xpath12).text
assert price11 > price12
price13 = driver.find_element(By.XPATH, xpath13).text
assert price12 > price13
price14 = driver.find_element(By.XPATH, xpath14).text
assert price13 > price14
price15 = driver.find_element(By.XPATH, xpath15).text
assert price14 > price15
price16 = driver.find_element(By.XPATH, xpath16).text
assert price15 > price16
price17 = driver.find_element(By.XPATH, xpath17).text
assert price16 > price17
price18 = driver.find_element(By.XPATH, xpath18).text
assert price17 > price18
price19 = driver.find_element(By.XPATH, xpath19).text
assert price18 > price19
price20 = driver.find_element(By.XPATH, xpath20).text
assert price19 > price20
