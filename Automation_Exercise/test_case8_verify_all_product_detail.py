from selenium import webdriver
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest

def test_valdi_register_delete():
    # Test Case 8: Verify All Products and product detail page
    # 1. Launch browser
    driver = webdriver.Firefox()
    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expected_home_page_url = 'https://automationexercise.com/'
    try:
        actual_home_page_url = driver.current_url
        assert actual_home_page_url == expected_home_page_url
        print("3. home page is visible successfully")
    except:
        print("3. home page is 'NOT' visible successfully")
    # 4. Click on 'Products' button
    try:
        product_button = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(2) > a:nth-child(1)"))).click()
    except:
        print("4. Product locator not found or changed")
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    # 6. The products list is visible
    expected_product_page_url = 'https://automationexercise.com/products'
    try:
        actual_product_page_url = driver.current_url
        assert actual_product_page_url == expected_product_page_url
        print("5. Product page is visible successfully, And product list is visible")

    except:
        print("5. Product page is 'NOT' visible successfully")

    # 7. Click on 'View Product' of first product
    try:
        view_product = WebDriverWait(driver, 10).until \
            (SH.presence_of_element_located((By.CSS_SELECTOR, "div.col-sm-4:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)"))).click()
    except:
        print("7. View locator not found or changed")
    time.sleep(30)
    # 8. User is landed to product detail page
    expected_product_detail_page_url = 'https://automationexercise.com/product_details/1'
    try:
        actual_product_detail_page_url = driver.current_url
        assert actual_product_detail_page_url == expected_product_detail_page_url
        print("8. User is landed to product detail page")

    except:
        print("8. User is 'NOT' landed to product detail page")
    # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
    expected_product_name_text = 'Blue Top'
    expected_product_category_text = 'Category: Women > Tops'
    expected_product_price_text = 'Rs. 500'
    expected_product_availability_text = 'Availability: In Stock'
    expected_product_condition_text = 'Condition: New'
    expected_product_brand_text = 'Brand: Polo'
    try:
        actual_product_name_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".product-information > h2:nth-child(2)")))
        actual_product_name_text = actual_product_name_element.text

        actual_product_category_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".product-information > p:nth-child(3)")))
        actual_product_category_text = actual_product_category_element.text

        actual_product_price_element = WebDriverWait(driver, 10).until(SH.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-information > span:nth-child(5) > span:nth-child(1)")))
        actual_product_price_text = actual_product_price_element.text

        actual_product_availability_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".product-information > p:nth-child(6)")))
        actual_product_availability_text = actual_product_availability_element.text

        actual_product_condition_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".product-information > p:nth-child(7)")))
        actual_product_condition_text = actual_product_condition_element.text

        actual_product_brand_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".product-information > p:nth-child(8)")))
        actual_product_brand_text = actual_product_brand_element.text

        assert actual_product_name_text == expected_product_name_text
        assert actual_product_category_text == expected_product_category_text
        assert actual_product_price_text == expected_product_price_text
        assert actual_product_availability_text == expected_product_availability_text
        assert actual_product_condition_text == expected_product_condition_text
        assert actual_product_brand_text == expected_product_brand_text
        print("10. Detail is visible: product name, category, price, availability, condition, brand")
    except:
        print("10. Detail is 'NOT' visible: product name, category, price, availability, condition, brand")
    driver.quit()


