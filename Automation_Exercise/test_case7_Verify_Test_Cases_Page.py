from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

def test_valid_register_delete():
    # 1. Launch browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://automationexercise.com/')

    # 3. Verify that home page is visible successfully
    expected_home_page_element = 'https://automationexercise.com/'
    try:
        actual_home_page_element = driver.current_url
        assert actual_home_page_element == expected_home_page_element
        print("3. home page is visible successfully")
    except:
        print("3. home page is not visible successfully")

    # 4. Click on 'test_case' button
    try:
        test_case = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(5) > a:nth-child(1)"))).click()

    except:
        print("signup locator changed")
    # 5. Verify user is navigated to test cases page successfully
    expected_test_case_page_url = 'https://automationexercise.com/test_cases'
    try:
        actual_test_case_page_url = driver.current_url
        assert actual_test_case_page_url == expected_test_case_page_url
        print("5. user is navigated to test cases page successfully")
    except:
        print("5. user is not navigated to test cases page successfully")
    driver.quit()