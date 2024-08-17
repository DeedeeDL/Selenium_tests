from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# TC 01 - Testing the functionality of the search bar by typing inside it
def searching_bar():
    # Initialize the browser
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.maximize_window()
    time.sleep(1)

    # Locate and interact with "Cum poti ajuta tu" section
    link = browser.find_element(By.LINK_TEXT, 'Cum poți ajuta tu?')
    link.click()
    time.sleep(2)


    # Scroll to the job section
    browser.execute_script(
        "document.getElementsByClassName('how-contribute__jobs swiper swiper-initialized swiper-horizontal')[0].scrollIntoView()")
    time.sleep(3)

# TC 02 - Left arrow is functional:
    arrowL = browser.find_element(By.ID, "arrow-left")
    arrowL.click()
    time.sleep(2)
    arrowL.click()
    time.sleep(2)
    arrowL.click()
    time.sleep(2)

# TC 03 - Right arrow is functional:
    arrowR = browser.find_element(By.ID, "arrow-right")
    action_chains = ActionChains(browser)
    action_chains.double_click(arrowR).perform()
    time.sleep(2)
    action_chains.double_click(arrowR).perform()
    time.sleep(2)
    action_chains.double_click(arrowR).perform()
    time.sleep(3)

    # Locate the search bar
    search = browser.find_element(By.XPATH, '//input[@class="search-input"]')

# TC 04 - List of words to write in the searching bar:
    words = ['tester', 'hr', 'marketing', 'UX', 'Developer', "Assistant manager", "not found", "Onboarding project"]

    for word in words:
        search.clear()  # Clear the input field before entering a new word
        search.send_keys(word)
        time.sleep(2)  # Wait for the results to load
        search.send_keys(Keys.ENTER)  # Press Enter after typing the word
        time.sleep(3)  # Wait to see the cleared state before the next iteration

# TC05 -On page of "Onboarding project volunteer" the button "detalii" is functional:

    detalii_button = browser.find_element(By.XPATH, '//a[@class = "detail-btn"]')
    detalii_button.click()
    time.sleep(3)


    # Switch to the new window that opened
    original_window = browser.current_window_handle
    all_windows = browser.window_handles

    # Assume the new window is the last one opened
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break


    #Interract with the new window:
    prev_height = -1
    max_scrolls = 100
    scroll_count = 0

    #Scrolling down and up  the new window
    while scroll_count < max_scrolls:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # give some time for new results to load
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)

# TC 06  - "Aplica" button is functional

    apply_button = browser.find_element(By.CLASS_NAME, "applyBtn")
    action_chains = ActionChains(browser)
    action_chains.double_click(apply_button).perform()


    # Switch to the new window that opened
    original_window = browser.current_window_handle
    all_windows = browser.window_handles

    # Assume the new window is the last one opened
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break
    time.sleep(6)
    browser.close()
    browser.switch_to.window(original_window)
    time.sleep(2)

#TC 07 - verifying the functionality of the link "Inapoi la locurile de munca":

    link_up = browser.find_element(By.CLASS_NAME,"backTxt")
    link_up.click()
    time.sleep(2)


    # Close the browser
    browser.quit()

searching_bar()