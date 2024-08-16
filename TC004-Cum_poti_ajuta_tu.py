from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Test case for testing the functionality of the search bar by typing inside it
def searching_bar():
    # Initialize the browser
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.maximize_window()  # Use maximize_window() instead of fullscreen
    time.sleep(1)

    # Locate and interact with "Misiunea noastra" section
    link = browser.find_element(By.LINK_TEXT, 'Cum poți ajuta tu?')
    link.click()
    time.sleep(2)


    # Scroll to the job section
    browser.execute_script(
        "document.getElementsByClassName('how-contribute__jobs swiper swiper-initialized swiper-horizontal')[0].scrollIntoView()")
    time.sleep(3)

    #Interract with the left arrow:
    arrowl = browser.find_element(By.ID, "arrow-left")
    arrowl.click()
    time.sleep(2)
    arrowl.click()
    time.sleep(2)
    arrowl.click()
    time.sleep(2)

    #Interact with te right arrow:
    arrowr = browser.find_element(By.ID, "arrow-right")
    action_chains = ActionChains(browser)
    action_chains.double_click(arrowr).perform()
    time.sleep(2)
    action_chains.double_click(arrowr).perform()
    time.sleep(2)
    action_chains.double_click(arrowr).perform()
    time.sleep(3)

    # Locate the search bar
    search = browser.find_element(By.XPATH, '//input[@class="search-input"]')

    # List of words to search
    words = ['tester', 'hr', 'marketing', 'UX', 'Developer', "Assistant manager", "not found", "Onboarding project"]

    for word in words:
        search.clear()  # Clear the input field before entering a new word
        search.send_keys(word)
        time.sleep(2)  # Wait for the results to load or any animation
        search.send_keys(Keys.ENTER)  # Press Enter after typing the word
        time.sleep(3)  # Wait to see the cleared state before the next iteration

    # Interact with the page of "Onboarding project volunteer"

    detalii_button = browser.find_element(By.XPATH, '//a[@class = "detail-btn"]')
    detalii_button.click()
    time.sleep(3)
    # Close the browser
    browser.quit()


# Run the search bar test
searching_bar()