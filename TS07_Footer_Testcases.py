from selenium.webdriver import Chrome,ActionChains
import time
from selenium.webdriver.common.by import By




# Test case for testing the functionality of the search bar by typing inside it
def searching_bar():
    # Initialize the browser
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.maximize_window()  # Use maximize_window() instead of fullscreen
    time.sleep(2)

    #scroll to the bottom of the page to see the footer
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


    # TC01 - Verify the LInkedin button :

    linkedin = browser.find_element(By.XPATH, '//footer//a[contains(@href,"linkedin.com")]')
    linkedin.click()
    time.sleep(3)

    # Switch to the new window that opened
    original_window = browser.current_window_handle
    all_windows = browser.window_handles

    # Assume the new window is the last one opened
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break
    time.sleep(2)
    browser.close()
    browser.switch_to.window(original_window)
    time.sleep(2)

    # TC02 - Verify the Instagram button :

    instagramIcon = browser.find_element(By.XPATH, '//footer//a[contains(@href,"https://www.instagram.com/")]')
    instagramIcon.click()
    time.sleep(3)

    # Switch to the new window that opened
    original_window = browser.current_window_handle
    all_windows = browser.window_handles

    # Assume the new window is the last one opened
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break
    time.sleep(2)
    browser.close()
    browser.switch_to.window(original_window)
    time.sleep(2)


    # TC03 - Verify the functionality of "Asociatia Oportunitati si cariere" link

    asociationLink = browser.find_element(By.XPATH,'//footer//h4[contains(text(),"ASOCIAȚIA OPORTUNITĂȚI ȘI CARIERE")]')
    asociationLink.click()
    time.sleep(2)


searching_bar()

