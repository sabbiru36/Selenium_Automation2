from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.common.by import By

# Test Case 9: Search Product

# 1. Launch browser
driver = webdriver.Chrome()

# 2. Navigate to url 'http://automationexercise.com'
driver.get('http://automationexercise.com')
# 3. Verify that home page is visible successfully
expected_home_url = 'https://automationexercise.com/'
try:
    actual_home_url = driver.current_url
    assert actual_home_url == expected_home_url
    print("3. Home page visible successfully")
except :
    print("3. Home page is 'NOT' visible successfully")

# 4. Click on 'Products' button
try:
    product_button = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(2) > a:nth-child(1)"))).click()
except :
    print("Product not found or product locator changed")

# 5. Verify user is navigated to ALL PRODUCTS page successfully
expected_product_page_url = 'https://automationexercise.com/products'
try:
    actual_product_page_url = driver.current_url
    assert actual_product_page_url == expected_product_page_url
    print("5. Product page visible successfully")
except :
    print("5. Product page is 'NOT' visible successfully")

# 6. Enter product name in search input and click search button
try:
    search_button = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#search_product")))
    search_button.send_keys('Tshirt')
except :
    print("Search button not found or locator changed")

try:
    search_click = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#submit_search"))).click()
except :
    print("Search button not found or Locator changed")

# 7. Verify 'SEARCHED PRODUCTS' is visible
expected_searched_products_page_text = 'SEARCHED PRODUCTS'
try:
    actual_searched_products_page_element = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, ".title")))
    actual_searched_products_page_text = actual_searched_products_page_element.text
    assert actual_searched_products_page_text == expected_searched_products_page_text
    print("7. Searched products is visible")
except :
    print("7. Searched products is 'NOT' visible")
# 8. Verify all the products related to search are visible


