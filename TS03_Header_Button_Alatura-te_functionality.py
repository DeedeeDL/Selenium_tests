import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By


def button():
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.maximize_window()
    time.sleep(3)

#TC01 - The hover effect is visible over the button "Alatura-te":

    buttonhover = browser.find_elements(By.XPATH, '//button[@class="join-btn btn--green"]')
    actions = ActionChains(browser)
    for link in buttonhover:
        actions.move_to_element(link).perform()  # Perform hover action
        time.sleep(3)  # Wait for 3 seconds

# TC02  -  Verify the functionality of the button "Alatura-te"
    green_button = browser.find_element(By.XPATH, '//button[@class="join-btn btn--green"]').click()

    time.sleep(10)

    browser.close()
button()



