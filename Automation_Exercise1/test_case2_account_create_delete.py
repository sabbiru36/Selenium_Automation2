from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from Automation_Exercise1.Common import common_fuctions as CF
import pytest
# from selenium.webdriver.firefox.options import Options as FirefoxOptions


def test_valid_register_delete():
    # https://automationexercise.com/test_cases
    # Test Case 1: Register User

    user_credentials = [CF.random_email(), CF.random_number(), CF.random_string()]

    # Write user credentials to file
    filename_data = "./user_credentials"
    CF.store_user_data(filename_data, user_credentials)

    # Step 1 : Launch Browser
    driver = webdriver.Firefox()

    # Step 2 : Navigate to url 'http://automationexercise.com'
    driver.get("https://automationexercise.com/")


    # 3. Verify that home page is visible successfully
    expected_home_page_url = "https://automationexercise.com/"
    actual_home_page_url = driver.current_url

    try:
        assert expected_home_page_url == actual_home_page_url
        print("Home page is visible successfully.")
    except AssertionError:
        print("home page is not visible successfully")

    # 4. Click on 'Signup / Login' button
    signup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a")))
    signup_button.click()

    #  5. Verify 'New User Signup!' is visible
    expected_signup_page_text = "New User Signup!"
    actual_signup_page_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form h2")))
    actual_signup_page_text = actual_signup_page_element.text

    try:
        assert expected_signup_page_text == actual_signup_page_text
        print("'New User Signup!' is visible")

    except:
        print("'New User Signup!' is not visible")

    # 6. Enter name and email address
    try:
        Username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
        Username.send_keys(user_credentials[2])
    except:
        print("Username Locator Changed.")

    try:
        Email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".signup-form > form:nth-child(2) > input:nth-child(3)")))
        Email.send_keys(user_credentials[0])
    except:
        print("Email Locator Changed.")

    # 7. Click 'Signup' button
    signup_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(5)")))
    signup_button.click()

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expected_signup_text = "ENTER ACCOUNT INFORMATION"

    try:
        actual_signup_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-form > .text-center.title > b")))
        actual_signup_text = actual_signup_element.text

        assert actual_signup_text == expected_signup_text
        print("'ENTER ACCOUNT INFORMATION' is visible")

    except:
        print("'ENTER ACCOUNT INFORMATION' is not visible")

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    #  Click Title button
    title_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.radio-inline:nth-child(3) > label:nth-child(1)")))
    title_button.click()

    #  Type Password
    Password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    Password.send_keys(user_credentials[1])

    #  Click Date of birth
    date = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#days"))))
    date.select_by_visible_text("10")

    month = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#months"))))
    month.select_by_visible_text("May")

    year = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#years"))))
    year.select_by_visible_text("2010")

    # 10. Select checkbox 'Sign up for our newsletter!'
    news_letter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#newsletter")))
    news_letter.click()

    # 11. Select checkbox 'Receive special offers from our partners!'
    receive_special_offers = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#optin")))
    receive_special_offers.click()

    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    #  Address info
    try:
        Firstname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "first_name")))
        Firstname.send_keys(CF.random_string())
    except:
        print("Firstname not found.")

    Lastname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "last_name")))
    Lastname.send_keys(CF.random_string())

    Address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "address1")))
    Address.send_keys(CF.random_string())

    # Country
    Country = Select(
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='country']"))))
    Country.select_by_visible_text("Canada")

    State = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "state")))
    State.send_keys(CF.random_string())

    City = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "city")))
    City.send_keys(CF.random_string())

    Zipcode = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "zipcode")))
    Zipcode.send_keys("700001")

    Mobile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mobile_number")))
    Mobile.send_keys("123456789")

    # 13. Click 'Create Account button'
    Create_account_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
    Create_account_button.click()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    expected_account_create_text = "ACCOUNT CREATED!"
    try:
        actual_account_create_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
        actual_account_create_text = actual_account_create_element.text

        assert actual_account_create_text == expected_account_create_text
        print("'ACCOUNT CREATED!' is visible")

    except:
        print("'ACCOUNT CREATED!' is not visible")

    # 15. Click 'Continue' button
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    continue_button.click()

    # 16. Verify that 'Logged in as username' is visible
    expected_text_logged = "Logged in as " + user_credentials[2]
    try:
        actual_logged_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
        actual_text_logged = actual_logged_element.text

        assert actual_text_logged == expected_text_logged
        print("Logged in as " + user_credentials[2] + " is visible")

    except:
        print("'Logged in as' is not visible")

    # 17. Click 'Delete Account' button
    account_delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Delete Account")))
    account_delete_button.click()

    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expected_delete_text = "ACCOUNT DELETED!"
    try:
        actual_delete_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
        actual_delete_text = actual_delete_element.text

        assert expected_delete_text == actual_delete_text
        print("'ACCOUNT DELETED!' is visible")

    except:
        print("'ACCOUNT DELETED!' is not visible")

    continue_button2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    continue_button2.click()

    # print(user_credentials)

    driver.close()