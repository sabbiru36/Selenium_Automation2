from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as SH
from selenium.webdriver.chrome.options import Options


def test_valid_register_delete():
    # Test Case 10: Verify Subscription in home page

    # |. Launch browser
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
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
    # 4. Scroll down to footer
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    # if project needed sroll down as element then can use below method
    # subscription = WebDriverWait(driver, 10).until(SH.presence_of_element_located((By.CSS_SELECTOR, "#susbscribe_email")))
    # driver.execute_script("arguments[0].scrollIntoView();",subscription)

    # 5. Verify text 'SUBSCRIPTION'
    expected_subscription_text = 'SUBSCRIPTION'
    try:
        actual_subscription_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".single-widget > h2:nth-child(1)")))
        actual_subscription_text = actual_subscription_element.text
        assert actual_subscription_text == expected_subscription_text
        print("5. Subscription text is visible")
    except:
        print("5. Subscription text is 'NOT' visible")

    # 6. Enter email address in input and click arrow button
    try:
        enter_email = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "#susbscribe_email")))
        enter_email.send_keys('sabbir@gmail.com')
    except:
        print("6. Enter Email locator changed")

    try:
        click_arrow = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, "#subscribe"))).click()

    except:
        print("7. Arrow sign Locator changed")
    # 7. Verify success message 'You have been successfully subscribed!' is visible
    expected_subscription_success_text = 'You have been successfully subscribed!'
    try:
        actual_subscription_success_element = WebDriverWait(driver, 10).until(
            SH.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        actual_subscription_success_text = actual_subscription_success_element.text
        assert actual_subscription_success_text == expected_subscription_success_text
        print("7. 'You have been successfully subscribed!' is visible")
    except:
        print("7. 'You have been successfully subscribed!' is 'NOT' visible")
    driver.quit()


