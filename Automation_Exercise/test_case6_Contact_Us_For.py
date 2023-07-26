from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
import time
from selenium.webdriver.common.alert import Alert

def test_valid_register_delete():
    # 1. Launch browser
    driver = webdriver.Chrome()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')

    # 3. Verify that home page is visible successfully
    expected_home_page_url = "https://automationexercise.com/"

    try:
        actual_home_page_url = driver.current_url
        assert expected_home_page_url == actual_home_page_url
        print("Home page is visible successfully.")
    except AssertionError:
        print("home page is not visible successfully")
    # 4. Click on 'Contact Us' button
    try:
        contract_botton = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".navbar-nav > li:nth-child(8) > a:nth-child(1)")))
        contract_botton.click()
    except:
        print("Contract us Button locator changed")

    # 5 . Verify 'GET IN TOUCH' is visible
    expected_get_in_page_text = 'GET IN TOUCH'

    try:
        actual_get_in_page_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "h2.title:nth-child(2)")))
        actual_get_in_page_text = actual_get_in_page_element.text
        assert actual_get_in_page_text == expected_get_in_page_text
        print("5. 'GET IN TOUCH' is visible")
    except:
        print("5. 'GET IN TOUCH' is not visible")

    # 6. Enter name, email, subject and message
    try:
        name = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "div.form-group:nth-child(2) > input:nth-child(1)")))
        name.send_keys('Sabbir')
    except:
        print("Name locator changed")

    try:
        gmail = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "div.form-group:nth-child(3) > input:nth-child(1)")))
        gmail.send_keys("Sabbir@gmail.com")
    except:
        print("Email locator changed")

    try:
        subject = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "div.form-group:nth-child(4) > input:nth-child(1)")))
        subject.send_keys("practice your test cases")
    except:
        print("Subject locator changed")

    try:
        message = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#message")))
        message.send_keys(
            "I'm the fresher student in SQA field.If i complete your 23 test cases then 'can i proudly say i'm an automation engineer'")
    except:
        print("Message locator changed")

    # 7. Upload file
    try:
        file_select = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "div.form-group:nth-child(6) > input:nth-child(1)")))
        # file_path = "C:/Users/xyz/Downloads/download.jpg"
        file_select.send_keys('C://Users/xyz/Desktop/Demo/Demo.jpg')

    except:
        print("Choose option not pound")
    # driver.close()
    # C:\Users\xyz\Desktop\Demo\Demo.jpg
    try:
        submit = WebDriverWait(driver, 5).until \
            (SH.presence_of_element_located((By.CSS_SELECTOR, "#contact-us-form > div:nth-child(7) > input"))).click()
    except:
        print("Submit button not found")
    # 9. Click OK button
    alert = Alert(driver)
    alert.accept()

    # try:
    #   ok_button = WebDriverWait(driver, 10).until(SH.presence_of_element_located(By.CSS_SELECTOR, "")).click()
    # except :
    # print("Ok button locator changed")
    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    expected_success_page_text = 'Success! Your details have been submitted successfully.'
    try:
        actual_success_page_element = WebDriverWait(driver, 10).until(SH.presence_of_element_located(
            (By.CSS_SELECTOR, "#contact-page > div.row > div.col-sm-8 > div > div.status.alert.alert-success")))
        actual_success_page_text = actual_success_page_element.text
        assert actual_success_page_text == expected_success_page_text
        print("9. 'Success! Your details have been submitted successfully.")

    except:
        print("9. 'Success! Your details have not been submitted successfully.")
    time.sleep(8)
    # 11. Click 'Home' button and verify that landed to home page successfully
    try:
        home_button = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "a.btn > span:nth-child(1)")))
        home_button.click()
    except:
        print("Home button locator changed")

    expected_home2_page_url = "https://automationexercise.com/"
    try:
        actual_home_page2_url = driver.current_url
        assert expected_home2_page_url == actual_home_page2_url
        print("11. Back home page is visible successfully.")
    except:
        print("11. Back home page is not  visible successfully")
        driver.get_screenshot_as_file('error.png')