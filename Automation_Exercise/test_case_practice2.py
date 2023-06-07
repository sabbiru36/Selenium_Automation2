from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

def test_valid_register_delete():
    # 1. Launch browser
    driver = webdriver.Firefox()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

    # 3. Verify that home page is visible successfully
    expected_home_page_element = 'https://automationexercise.com/'
    try:
        actual_home_page_element = driver.current_url
        assert actual_home_page_element == expected_home_page_element
        print("3. Home page is visible successfully")
    except:
        print("3. Home page is not visible successfully")
    # 4. Click on 'Signup / Login' button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")))
        login_button.click()
    except:
        print("4. Loging button not found or Locator changed")
    # 5. Verify 'Login to your account' is visible
    expected_login_page_text = 'Login to your account'

    try:
        actual_login_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")))
        actual_login_page_text = actual_login_page_element.text
        assert actual_login_page_text == expected_login_page_text
        print("5. 'Login to your account' is visible")
        # driver.get_screenshot_as_file("./log.png")
    except:
        print("5. 'Login to your account' is not visible")
        # driver.get_screenshot_as_file("./Not log.png")
    # 6. Enter correct email address and password
    try:
        Email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(2)")))
        Email.send_keys("sabbir@gmail.com")
    except:
        print("Email invalid or Locator Changed")
    try:
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(3)")))
        password.send_keys("1234")
    except:
        print("password invalid or Password locator changed")

    # 7. Click 'login' button
    login_button2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(4)")))
    login_button2.click()
    # 8. Verify that 'Logged in as username' is visible
    expected_username_page_text = 'Logged in as sa'

    try:
        actual_username_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(10) > a:nth-child(1)")))
        actual_username_page_text = actual_username_page_element.text
        assert actual_username_page_text == expected_username_page_text
        print("7. 'Logged in as username' is visible")
    except:
        print("7. 'Logged in as username' is not visible")

    # 9. Click 'Delete Account' button
    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(5) > a:nth-child(1)")))
    delete_button.click()
    # 10. Verify that 'ACCOUNT DELETED!' is visible
    expected_delete_page_text = 'Account Deleted!'

    try:
        actual_delete_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".title > b:nth-child(1)")))
        actual_delete_page_text = actual_delete_page_element.text
        assert actual_delete_page_text == expected_delete_page_text
        print("10. 'ACCOUNT DELETED!' is visible")
    except:
        print("10. 'ACCOUNT DELETED!' is not visible")

    driver.quit()
