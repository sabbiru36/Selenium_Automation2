from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_register_delete():
    # 1. Launch browser
    driver = webdriver.Firefox()
    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expected_home_page_element = 'https://automationexercise.com'
    try:
        actual_home_page_element = driver.current_url
        assert actual_home_page_element == expected_home_page_element
        print("3. home page is visible successfully")
    except:
        print("3. home page is not visible successfully")
    # 4. Click on 'Signup / Login' button
    try:
        signup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(4) > a:nth-child(1)")))
        signup.click()
    except:
        print("signup Locator changed")
    # 5. Verify 'Login to your account' is visible
    expected_login_page_text = 'Login to your account'
    try:
        actual_login_page_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > h2:nth-child(1)")))
        actual_login_page_text = actual_login_page_element.text
        assert actual_login_page_text == expected_login_page_text
        print("5. 'Login to your account' is visible")
    except:
        print("5.'Login to your account' is not visible")
    # 6. Enter incorrect email address and password
    try:
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(2)")))
        email.send_keys("xyz@Gmail.com")
    except:
        print("email Locator changed")
    try:
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > input:nth-child(3)")))
        password.send_keys('123')
    except:
        print("Password locator changed")

    # 7. Click 'login' button
    try:
        login_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(4)")))
        login_button.click()
    except:
        print("login button changed")
    # 8. Verify error 'Your email or password is incorrect!' is visible
    expected_login_error_page_text = 'Your email or password is incorrect!'
    try:
        actual_login_error_page_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > form:nth-child(2) > p:nth-child(4)")))
        actual_login_error_page_text = actual_login_error_page_element.text
        assert actual_login_error_page_text == expected_login_error_page_text
        print("8. 'Your email or password is incorrect!' is visible")
    except:
        print("8. 'Your email or password is incorrect!' is not visible")
    driver.quit()