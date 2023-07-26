import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
# Test Case 12: Add Products in Cart
# 1. Launch browser
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# 2. Navigate to url 'http://automationexercise.com'
driver.maximize_window()
driver.get('http://automationexercise.com')
# 3. Verify that home page is visible successfully
expected_home_url = "https://automationexercise.com/"
try:
    actual_home_url = driver.current_url
    assert actual_home_url == expected_home_url
    print("3. Home page is visible successfully")
except :
    print("3. Home is 'NOT' visible successfully")

# 4. Click 'Products' button
click_product = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(2) > a:nth-child(1)"))).click()

# 5. Hover over first product and click 'Add to cart'
first_product = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(4) > div > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay")))
hover = ActionChains(driver).move_to_element(first_product)
hover.perform()
time.sleep(5)
click_cart = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(4) > div > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.product-overlay > div > a"))).click()
time.sleep(5)

# 6. Click 'Continue Shopping' button
continue_click = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "#cartModal > div > div > div.modal-footer > button"))).click()

# 7. Hover over second product and click 'Add to cart'
second_product = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(4) > div > div > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.product-overlay")))
hover = ActionChains(driver).move_to_element(second_product)
hover.perform()
time.sleep(5)
click_cart2 = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(4) > div > div > div.col-sm-9.padding-right > div > div:nth-child(4) > div > div.single-products > div.product-overlay > div > a"))).click()
time.sleep(5)

# 8. Click 'View Cart' button
view_cart = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "p.text-center:nth-child(2) > a:nth-child(1) > u:nth-child(1)"))).click()

# 9. Verify both products are added to Cart
expected_first_product_text = 'Blue Top'
try:
    actual_first_product_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")))
    actual_first_product_text = actual_first_product_element.text
    assert actual_first_product_text == expected_first_product_text
    print("9. First Product add to cart successfully")
except :
    print("9. First product add to cart is 'NOT'  successfully")
expected_second_product_text = 'Men Tshirt'
try:
    actual_second_product_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-2 > td:nth-child(2) > h4:nth-child(1) > a:nth-child(1)")))
    actual_second_product_text = actual_second_product_element.text
    assert actual_second_product_text == expected_second_product_text

    print("9. Second product add to cart  successfully")
except :
    print("9. Second product add to cart 'NOT' successfully")

# 10. Verify their prices, quantity and total price
expected_first_product_prices_text = 'Rs. 500'
expected_first_product_quantity_text = '1'
expected_first_product_total_price_text = 'Rs. 500'
try:
    actual_first_product_prices_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td:nth-child(3) > p:nth-child(1)")))
    actual_first_product_prices_text = actual_first_product_prices_element.text

    actual_first_product_quantity_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td:nth-child(4) > button:nth-child(1)")))
    actual_first_product_quantity_text = actual_first_product_quantity_element.text

    actual_first_product_total_prices_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td:nth-child(5) > p:nth-child(1)")))
    actual_first_product_total_prices_text = actual_first_product_total_prices_element.text

    assert actual_first_product_prices_text == actual_first_product_prices_text
    assert actual_first_product_quantity_text == expected_first_product_quantity_text
    assert actual_first_product_total_prices_text == expected_first_product_total_price_text
    print("10. First product prices,quantity,total price is verified as expected ")
except :
    print("10. First product prices,quantity,total price is 'NOT' verified as expected")

expected_second_product_prices_text = 'Rs. 400'
expected_second_product_quantity_text = '1'
expected_second_product_total_price_text = 'Rs. 400'
try:
    actual_second_product_prices_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-2 > td:nth-child(3) > p:nth-child(1)")))
    actual_second_product_prices_text = actual_second_product_prices_element.text

    actual_second_product_quantity_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-2 > td:nth-child(4) > button:nth-child(1)")))
    actual_second_product_quantity_text = actual_second_product_quantity_element.text

    actual_second_product_total_prices_element = WebDriverWait(driver, 10).until(
        SH.presence_of_element_located((By.CSS_SELECTOR, "#product-2 > td:nth-child(5) > p:nth-child(1)")))
    actual_second_product_total_prices_text = actual_second_product_total_prices_element.text

    assert actual_second_product_prices_text == actual_second_product_prices_text
    assert actual_second_product_quantity_text == expected_second_product_quantity_text
    assert actual_second_product_total_prices_text == expected_second_product_total_price_text
    print("10. Second product prices,quantity,total price is verified as expected ")
except :
    print("10. Second product prices,quantity,total price is 'NOT' verified as expected")
