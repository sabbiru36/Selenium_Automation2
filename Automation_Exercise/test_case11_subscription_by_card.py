from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_valid_register_delete():
    # Test Case 11: Verify Subscription in Cart page
    # 1.  Launch browser
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expected_home_url = 'https://automationexercise.com/'
    try:
        actual_home_url = driver.current_url
        assert actual_home_url == expected_home_url
        print("3. Home page is visible successfully")
    except:
        print("3. Home page is 'NOT' visible successfully")
    # 4. Click 'Cart' button
    try:
        card_button = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".nav > li:nth-child(3) > a:nth-child(1)"))).click()
    except:
        print("4. Click card button locator changed")

    # 5. Scroll down to footer
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    # 6. Verify text 'SUBSCRIPTION'
    expected_subscription_text = 'SUBSCRIPTION'
    try:
        actual_subscription_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".single-widget > h2:nth-child(1)")))
        actual_subscription_text = actual_subscription_element.text
        assert actual_subscription_text == expected_subscription_text
        print("6. Subscriptions text is visible")
    except:
        print("6. Subscription text is 'NOT' visible ")
    # 7. Enter email address in input and click arrow button
    try:
        email = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "#susbscribe_email"))).send_keys('sabbir@gmail.com')
    except:
        print("7. Email locator changed")

    try:
        click_arrow = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "#subscribe"))).click()
    except:
        print("7. Click arrow locator changed")

    # 8. Varify success message 'You have been successfully subscribed!' is visible
    expected_subscription_success_text = 'You have been successfully subscribed!'
    try:
        actual_subscription_success_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        actual_subscription_success_text = actual_subscription_success_element.text
        assert actual_subscription_success_text == expected_subscription_success_text
        print("8. Subscription success text is visible")
    except:
        print("8. Subscription success test is 'NOT' visible")


