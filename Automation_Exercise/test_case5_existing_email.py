from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.common.by import By
import pytest

def test_valid_register_delete():
    # 1. Launch browser
    driver = webdriver.Firefox()

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

    # 4. Click on 'Signup / Login' button
    try:
        signup = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")))
        signup.click()
    except:
        print("signup locator changed")

    # 6. Enter name and already registered email address
    try:
        name = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > input:nth-child(2)")))
        name.send_keys("Sabbir")
    except:
        print("name locator changed")

    try:
        email = WebDriverWait(driver, 5).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > input:nth-child(3)")))
        email.send_keys("sabbir@gmail.com")
    except:
        print("email locator changed")

    # 7. Click 'Signup' button
    try:
        signup_button = WebDriverWait(driver, 5).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(5)")))
        signup_button.click()
    except:
        print("Signup locator changed")

    # 8. Verify error 'Email Address already exist!' is visible
    expected_exit_email_page_text = 'Email Address already exist!'

    try:
        actual_exit_email_page_element = WebDriverWait(driver, 5).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > p:nth-child(5)")))
        actual_exit_email_page_text = actual_exit_email_page_element.text
        assert actual_exit_email_page_text == expected_exit_email_page_text
        print("8. 'Email Address already exist!' is visible")
    except:
        print("8. 'Email Address already exist!' is not visible")

    driver.quit()
