import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


# Test case for testing the functionality of the button "Alatura-te"
def button():
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    time.sleep(3)

    green_button = browser.find_element(By.XPATH, '//button[@class="join-btn btn--green"]').click()

    time.sleep(10)

    browser.close()
button()



