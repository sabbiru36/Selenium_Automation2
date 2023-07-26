from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select
from Automation_Exercise.common import common_functions as CF
# Test Case 14: Place Order: Register while Checkout
# 1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Navigate to url 'http://automationexercise.com'
driver.get("https://automationexercise.com/")

# 3. Verify that home page is visible successfully
expected_home_url = "https://automationexercise.com/"
try:
    actual_home_url = driver.current_url
    assert actual_home_url == expected_home_url
    print("3. Home page is visible successfully")
except :
    print("3. Home page is 'NOT' visible successfully")

# 4. Add products to cart
product = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")))
hover = ActionChains(driver).move_to_element(product)
hover.perform()
time.sleep(5)
product_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)"))).click()
time.sleep(5)
# 5. Click 'Cart' button
click_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-center:nth-child(2) > a:nth-child(1) > u:nth-child(1)")))
click_cart.click()

# 6. Verify that cart page is displayed
expected_cart_url = "https://automationexercise.com/view_cart"
try:
    actual_cart_url = driver.current_url
    assert actual_cart_url == expected_cart_url
    print("6. Cart page is visible successfully")
except :
    print("6. Cart page is 'NOT' visible successfully")
# 7. Click Proceed To Checkout
click_checkout = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn"))).click()

# 8. Click 'Register / Login' button
click_process_to_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-body > p:nth-child(2) > a:nth-child(1) > u:nth-child(1)"))).click()

# 9. Fill all details in Signup and create account
user_credentials = [CF.random_email(), CF.random_number(), CF.random_string()]
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
except :
    print("Email Locator Changed")

# 7. Click 'Signup' button
signup_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn:nth-child(5)")))
signup_button.click()


# 8. Fill details: Title, Name, Email, Password, Date of birth
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

# 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
expected_account_create_text = "ACCOUNT CREATED!"
try:
    actual_account_create_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
    actual_account_create_text = actual_account_create_element.text

    assert actual_account_create_text == expected_account_create_text
    print("9. ACCOUNT CREATED!' is visible")

except:
    print("9. ACCOUNT CREATED!' is not visible")

# 10--. Click 'Continue' button
continue_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
continue_button.click()
# 11. Verify ' Logged in as username' at
expected_text_logged = "Logged in as " + user_credentials[2]
try:
    actual_logged_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
    actual_text_logged = actual_logged_element.text

    assert actual_text_logged == expected_text_logged
    print("11. Logged in as " + user_credentials[2] + " is visible")

except:
    print("11. Logged in as' is not visible")

# 12.Click 'Cart' button
click_cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".nav > li:nth-child(3) > a:nth-child(1)"))).click()

# 13. Click 'Proceed To Checkout' button
click_checkout = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn"))).click()

# 14. Verify Address Details and Review Your Order
expected_address_url = "https://automationexercise.com/checkout"
try:
    actual_address_url = driver.current_url
    assert actual_address_url == expected_address_url
    print("14. Address details  Home page is visible successfully")
except :
    print("14. Address datails page is 'NOT' visible successfully")
# 15. Enter description in comment text area and click 'Place Order'
comment = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control")))
driver.execute_script("arguments[0].scrollIntoView();", comment)
time.sleep(5)
comment = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control"))).send_keys("Hi")
place_order = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn"))).click()
# 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.form-row:nth-child(2) > div:nth-child(1) > input:nth-child(2)"))).send_keys("sabbir")

card = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".card-number"))).send_keys("12345")

cvc = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".card-cvc"))).send_keys("12345")

expramonth = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".card-expiry-month"))).send_keys("March")

exprayear = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".card-expiry-year"))).send_keys("2025")

# 17. Click 'Pay and Confirm Order' button
order_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#submit"))).click()
# 18. Verify success message 'Your order has been placed successfully!'
expected_order_success_text = "Your order has been placed successfully!"
try:
    actual_order_success_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#success_message > div:nth-child(1)")))
    actual_order_success_text = actual_order_success_element.text

    assert actual_order_success_text == expected_order_success_text
    print("18. Your order has been placed successfully has verified ")

except:
    print("18. Your order has been placed successfully has 'NOT' verified ")

# 19. Click 'Delete Account' button
account_delete_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Delete Account")))
account_delete_button.click()

# 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
expected_delete_text = "ACCOUNT DELETED!"
try:
    actual_delete_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
    actual_delete_text = actual_delete_element.text

    assert expected_delete_text == actual_delete_text
    print("20. ACCOUNT DELETED!' is visible")

except :
    print("20. ACCOUNT DELETED!' is not visible")

continue_button2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
continue_button2.click()

driver.quit()
