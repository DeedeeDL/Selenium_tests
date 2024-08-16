from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# webdriver wait

def arrow_buttons():
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    time.sleep(1)

    browser.execute_script(
        "document.getElementsByClassName('how-contribute__jobs swiper swiper-initialized swiper-horizontal')[0].scrollIntoView()")
    time.sleep(3)

    right_arrow = browser.find_element(By.ID, 'arrow-right')
    left_arrow = browser.find_element(By.ID, 'arrow-left')

    for i in range(5):
        action_chains = ActionChains(browser)
        action_chains.double_click(right_arrow).perform()
        time.sleep(1)
    for i in range(5):
        action_chains = ActionChains(browser)
        action_chains.double_click(left_arrow).perform()
        time.sleep(1)
    browser.quit()  # Close the browser when done


# Call the function
arrow_buttons()