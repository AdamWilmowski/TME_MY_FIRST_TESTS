from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

# sku_1 = input('Enter the SKU of first product: ')
# sku_2 = input('Enter the SKU of second product: ')

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get(f'https://www.tme.hk/en/product/TGL41-6.8A-DIO')
driver.find_element(By.ID, 'cookies-consent-close-icon').click()
price_raw_2 = float(driver.find_element(By.XPATH,
                                        '//*[@id="sylius-product-selecting-variant"]/div/div[1]/table/tbody/tr[1]/td[3]').text)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="sylius-product-adding-to-cart"]/button[1]').click()
time.sleep(2)


def generate_product_variables(item, value):
    field = driver.find_element(By.XPATH, f'/html/body/div[1]/div[4]/main/div/div/section[1]/div[2]/div[{item}]').text
    values_list = field.split('\n')
    local_variables = {}
    for idx, value in enumerate(values_list):
        var_name = f"variable_{idx + 1}"
        local_variables[var_name] = value

    if value == 7 or value == 8:
        mult_qty = int(local_variables[f'variable_{value}'].split(': ')[1])
        return mult_qty

    elif value == 12 or value == 13:
        price = float(local_variables[f'variable_{value}'].split(' ')[1])
        return price

    elif value == 10:
        weight = float(local_variables[f'variable_{value}'].split(' ')[0])
        return weight

    else:
        print('INCORRECT FUNCTION VALUES')


def generate_summary_variables(value):
    if value in range(3, 6):
        field = driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/div[4]/main/div/div/section[2]/div/div[{value}]/div[2]').text
        if value == 3 or 4:
            transport_subtotal = float(field.split(' ')[1])
            return transport_subtotal
        elif value == 5:
            weight = float(field.split(' ')[0])
            return weight
    elif value == 6:
        field = driver.find_element(By.ID, 'sylius-cart-grand-total').text
        order_total = float(field.split(' ')[1])
        return order_total


driver.get('https://www.tme.hk/en/cart')
item_multiplicity = generate_product_variables(1, 7)
min_amount = generate_product_variables(1, 8)
unit_price = generate_product_variables(1, 12)
item_total = generate_product_variables(1, 13)
item_weight = generate_product_variables(1, 10)
order_total = generate_summary_variables(6)
order_transport = generate_summary_variables(4)
order_weight = generate_summary_variables(5)
order_subtotal = generate_summary_variables(3)

assert item_weight == order_weight
assert unit_price * item_multiplicity == round(item_total, 2)
assert item_total == order_subtotal
assert order_subtotal + order_transport == order_total

