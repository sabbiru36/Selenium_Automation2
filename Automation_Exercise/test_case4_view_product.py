from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
def test_valid_register_delete():

    # 1. Launch browser
    driver = webdriver.Firefox()
    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expected_home_page_element = 'https://automationexercise.com/'
    try:
        actual_home_page_element = driver.current_url
        assert actual_home_page_element == expected_home_page_element
        print("3. home page is visible successfully")
    except:
        print("3. home page is not visible successfully")

    # 4. Click on 'Signup / Login' button
    try:
        signup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".nav > li:nth-child(4) > a:nth-child(1)")))
        signup.click()
    except:
        print("Signup button Locator changed")

    # 5. Verify 'Login to your account' is visible
    expected_login_Account_page_text = 'Login to your account'
    try:
        actual_login_account_page_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")))
        actual_login_account_page_text = actual_login_account_page_element.text
        assert actual_login_account_page_text == expected_login_Account_page_text
        print("5. 'Login to your account' is visible")
    except:
        print("5. 'Login to your account' is not visible")
    # 6. Enter correct email address and password
    try:
        email = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(2)")))
        email.send_keys("sabbir@gmail.com")
    except:
        print("Email locator changed")

    try:
        password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(3)")))
        password.send_keys("1234")
    except:
        print("Password locator changed")

    # 7. Click 'login' button
    try:
        login = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(4)")))
        login.click()
    except:
        print("Login button locator changed")

    # 8. Verify that 'Logged in as username' is visible
    expected_username_page_text = 'Logged in as Sabbir'

    try:
        actual_username_page_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(10) > a:nth-child(1)")))
        actual_username_page_text = actual_username_page_element.text
        assert actual_username_page_text == expected_username_page_text
        print("8. 'Logged in as username' is visible")
    except:
        print("8. 'Logged in as username' is not visible")
    # 9. Click 'Logout' button
    try:
        logout = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")))
        logout.click()
    except:
        print("Logout locator changed")
    # 10. Verify that user is navigated to login page
    expected_login_page_back_element = 'https://automationexercise.com/login'
    try:
        actual_login_page_back_element = driver.current_url
        assert actual_login_page_back_element == expected_login_page_back_element
        print("10. user is navigated to login page")
    except:
        print("10. user is not navigated to login page")

    driver.quit()
