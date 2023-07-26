from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
import time
from selenium.webdriver.chrome.options import Options
# Test Case 13: Verify Product quantity in Cart
# 1. Launch browser
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.maximize_window()

# 2. Navigate to url 'http://automationexercise.com'
driver.get("https://www.automationexercise.com/")

# 3. Verify that home page is visible successfully
expected_home_url = "https://www.automationexercise.com/"
try:
    actual_home_url = driver.current_url
    assert actual_home_url == expected_home_url
    print("3. Home page is visible successfully")
except :
    print("3. Home page is 'NOT' visible successfully")

# 4. Click 'View Product' for any product on home page
view_product = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(3) > div > div.choose > ul > li > a"))).click()

# 5. Verify product detail is opened
expected_product_detail = "https://www.automationexercise.com/product_details/1"
try:
    actual_product_detail = driver.current_url
    assert actual_product_detail == expected_product_detail
    print("5. Product detail is visible")
except :
    print("5. Product detail is 'NOT' visible")

# 6. Increase quantity to 4
quantity_increase = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "#quantity")))
quantity_increase.clear()
quantity_increase.send_keys("4")

# 7. Click 'Add to cart' button
add_cart = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.CSS_SELECTOR, "body > section > div > div > div.col-sm-9.padding-right > div.product-details > div.col-sm-7 > div > span > button"))).click()
time.sleep(5)
# 8. Click 'View Cart' button
view_cart = WebDriverWait(driver, 10).until(
    SH.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a/u"))).click()

# 9. Verify that product is displayed in cart page with exact quantity
expected_product_name_text = "Blue Top"
expected_product_quantity_text = "4"
try:
    actual_product_name_element = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td.cart_description > h4 > a")))
    actual_product_name_text = actual_product_name_element.text
    actual_product_quantity_element = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#product-1 > td.cart_quantity > button")))
    actual_product_quantity_text = actual_product_quantity_element.text
    assert actual_product_name_text == expected_product_name_text
    assert actual_product_quantity_text == expected_product_quantity_text
    print("9. Product is displayed exactly")
except :
    print("9.product is 'NOT' displayed exactly")
driver.quit()