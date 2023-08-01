from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

sku_1 = input('Enter the SKU of first product: ')
sku_2 = input('Enter the SKU of second product: ')

driver_service = Service(executable_path="C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get(f'https://www.tme.hk/en/product/{sku_1}')
driver.find_element(By.ID, 'cookies-consent-close-icon').click()
driver.find_element(By.XPATH, '//*[@id="sylius-product-adding-to-cart"]/button[1]').click()
time.sleep(3)
driver.get(f'https://www.tme.hk/en/product/{sku_2}')
driver.find_element(By.XPATH, '//*[@id="sylius-product-adding-to-cart"]/button[1]').click()
time.sleep(3)


def generate_product_variables(item, variable_type):
    if item == 1:
        field = driver.find_element(By.XPATH, f'/html/body/div[1]/div[5]/main/div/div/section[1]/div[2]/div').text
    else:
        field = driver.find_element(By.XPATH, f'/html/body/div[1]/div[5]/main/div/div/section[1]/div[2]/div[{item}]').text
    values_list = field.split('\n')
    local_variables = {}
    for idx, value in enumerate(values_list):
        var_name = f"variable_{idx + 1}"
        local_variables[var_name] = value

    if variable_type == 7 or variable_type == 8:
        mult_qty = int(local_variables[f'variable_{variable_type}'].split(': ')[1])
        return mult_qty

    elif variable_type == 10:
        weight = float(local_variables[f'variable_{variable_type}'].split(' ')[0])
        return weight

    elif variable_type == 12 or variable_type == 14:
        price_total = float(local_variables[f'variable_{variable_type}'].split(' ')[1])
        return price_total

    else:
        print('INCORRECT FUNCTION VALUES')


def generate_summary_variables(variable_type):
    if variable_type == 1:
        field = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/section[2]/div/div[2]/div/div[2]').text
        weight = float(field.split(' ')[0])
        return weight

    elif variable_type == 2:
        field = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/section[2]/div/div[3]/div/div/div/div[2]/div[2]').text
        transport = float(field.split(' ')[1])
        return transport

    elif variable_type == 3:
        field = driver.find_element(By. XPATH, '/html/body/div[1]/div[5]/main/div/div/section[2]/div/div[4]/div[2]').text
        subtotal = float(field.split(' ')[1])
        return subtotal

    elif variable_type == 4:
        field = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/section[2]/div/div[5]').text
        order_total = float(field.split(' ')[2])
        return order_total

    else:
        print('INCORRECT FUNCTION VALUES')


cart_button_1 = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/div/div[2]')
cart_button_2 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div[2]/a[2]')
driver.fullscreen_window()
time.sleep(20)
add_button = driver.find_element(By.XPATH, '//*[@id="sylius_cart_item"]/table/tbody/tr/td[2]/div[2]/div[1]/div/div/div[3]')
subtract_button = driver.find_element(By.XPATH, '//*[@id="sylius_cart_item"]/table/tbody/tr/td[2]/div[2]/div[1]/div/div/div[1]')
delete_item_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/section[1]/div[2]/div[2]/div[1]/form/button')
qty_field = driver.find_element(By.ID, 'sylius_cart_item_quantity')
item_multiplicity_1 = generate_product_variables(1, 7)
item_min_amount_1 = generate_product_variables(1, 8)
item_weight_1 = generate_product_variables(1, 10)
item_unit_prc_1 = generate_product_variables(1, 12)
item_subtotal_1 = generate_product_variables(1, 14)
item_multiplicity_2 = generate_product_variables(2, 7)
item_min_amount_2 = generate_product_variables(2, 8)
item_weight_2 = generate_product_variables(2, 10)
item_unit_prc_2 = generate_product_variables(2, 12)
item_subtotal_2 = generate_product_variables(2, 14)
order_weight = generate_summary_variables(1)
order_transport = generate_summary_variables(2)
order_subtotal = generate_summary_variables(3)
order_total = generate_summary_variables(4)

assert round(item_min_amount_1 * item_unit_prc_1, 2) == item_subtotal_1
assert round(item_min_amount_2 * item_unit_prc_2, 2) == item_subtotal_2
assert round(item_subtotal_1 + item_subtotal_2, 2) == order_subtotal
assert round(order_subtotal + order_transport, 2) == order_total
assert round(item_weight_1 + item_weight_2, 2) == order_weight

new_amount_1 = item_min_amount_1 + 2 * item_multiplicity_1
add_button.click()
time.sleep(1)
add_button.click()
time.sleep(8)
item_weight_1 = generate_product_variables(1, 10)
item_subtotal_1 = generate_product_variables(1, 14)
order_weight = generate_summary_variables(1)
order_transport = generate_summary_variables(2)
order_subtotal = generate_summary_variables(3)
order_total = generate_summary_variables(4)

assert round(new_amount_1 * item_unit_prc_1, 2) == item_subtotal_1
assert round(item_min_amount_2 * item_unit_prc_2, 2) == item_subtotal_2
assert round(item_subtotal_1 + item_subtotal_2, 2) == order_subtotal
assert round(order_subtotal + order_transport, 2) == order_total
assert round(item_weight_1 + item_weight_2, 2) == order_weight

new_amount_2 = new_amount_1 - item_multiplicity_1
subtract_button.click()
time.sleep(5)
item_weight_1 = generate_product_variables(1, 10)
item_subtotal_1 = generate_product_variables(1, 14)
order_weight = generate_summary_variables(1)
order_transport = generate_summary_variables(2)
order_subtotal = generate_summary_variables(3)
order_total = generate_summary_variables(4)

assert round(new_amount_2 * item_unit_prc_1, 2) == item_subtotal_1
assert round(item_min_amount_2 * item_unit_prc_2, 2) == item_subtotal_2
assert round(item_subtotal_1 + item_subtotal_2, 2) == order_subtotal
assert round(order_subtotal + order_transport, 2) == order_total
assert round(item_weight_1 + item_weight_2, 2) == order_weight

new_amount_3 = item_multiplicity_1 * 10
qty_field.clear()
qty_field.send_keys(new_amount_3)
time.sleep(5)
item_weight_1 = generate_product_variables(1, 10)
item_subtotal_1 = generate_product_variables(1, 14)
order_weight = generate_summary_variables(1)
order_transport = generate_summary_variables(2)
order_subtotal = generate_summary_variables(3)
order_total = generate_summary_variables(4)

assert round(new_amount_3 * item_unit_prc_1, 2) == item_subtotal_1
assert round(item_min_amount_2 * item_unit_prc_2, 2) == item_subtotal_2
assert round(item_subtotal_1 + item_subtotal_2, 2) == order_subtotal
assert round(order_subtotal + order_transport, 2) == order_total
assert round(item_weight_1 + item_weight_2, 2) == order_weight

delete_item_button.click()
time.sleep(8)
order_weight = generate_summary_variables(1)
order_transport = generate_summary_variables(2)
order_subtotal = generate_summary_variables(3)
order_total = generate_summary_variables(4)

assert item_subtotal_1 == order_subtotal
assert item_weight_1 == order_weight
assert order_subtotal + order_transport == order_total

qty_field.clear()
qty_field.send_keys('xc')
time.sleep(2)
background = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/main/div/div/section[1]/div[2]/div[1]')
validation_error = driver.find_element(By.XPATH, '//*[@id="sylius_cart_item"]/table/tbody/tr/td[2]/p[1]')
assert background.value_of_css_property('background-color') == 'rgba(250, 232, 231, 1)'
assert validation_error.text == 'Required only positive digit numbers.'
assert validation_error.value_of_css_property('color') == 'rgba(175, 9, 9, 1)'
assert validation_error.value_of_css_property('font-size') == '14px'

driver.find_element(By.ID, 'cart-items-all-checkbox').click()
driver.find_element(By.ID, 'cart-items-bulk-delete').click()
time.sleep(2)
items_in_cart = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div/h1')
background = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div')

assert items_in_cart.text == '0 items in your shopping cart'
assert items_in_cart.value_of_css_property('font-size') == '26px'
assert background.value_of_css_property('background-color') == 'rgba(99, 151, 212, 1)'

print('CART TEST OK')
