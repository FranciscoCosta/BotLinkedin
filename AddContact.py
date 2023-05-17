from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.linkedin.com')
time.sleep(2)

email = input("Enter your email: ")
password = input("Enter your password: ")

time.sleep(2)
username = browser.find_element("id", "session_key")
password_field = browser.find_element("id", "session_password")

username.send_keys(email)
password_field.send_keys(password)

time.sleep(2)

submit_button = browser.find_element(
    'css selector', '[data-id="sign-in-form__submit-btn"]')
submit_button.click()

time.sleep(2)

browser.get(
    'https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=(Xq')
time.sleep(4)

next_button = browser.find_element(By.CSS_SELECTOR, '[aria-label="Avançar"]')
print(next_button)
while next:
    all_buttons = browser.find_elements(By.TAG_NAME, "button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]
    print(len(connect_buttons))
    for btn in connect_buttons:

        browser.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        sendbtn = browser.find_element(
            By.CSS_SELECTOR, '[aria-label="Enviar agora"]')
        sendbtn.click()
        time.sleep(2)
    browser.execute_script("window.scrollTo(0, 700)")
    time.sleep(2)
    next_button.click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)
    next_button = browser.find_element(
        By.CSS_SELECTOR, '[aria-label="Avançar"]')

# Keep the script running until interrupted
while True:
    pass
