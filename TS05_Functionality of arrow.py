from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def arrowFunction():
    browser = Firefox()
    browser.get("https://oportunitatisicariere.ro/")
    time.sleep(1)

# TC 01 - The scroll function of the website window is working properly:

    browser.execute_script(
        "document.getElementsByClassName('how-contribute__jobs swiper swiper-initialized swiper-horizontal')[0].scrollIntoView()")
    time.sleep(3)

# TC 02 - The hover effect over the arrow is functional :
    action_chains = ActionChains(browser)
    arrow = browser.find_element(By.XPATH, '/html/body/a/img')
    hover = ActionChains(browser).move_to_element(arrow).perform()
    time.sleep(3)

# TC 03 - The arrow is functional :
    # code to perform the double click on the arrow:
    action_chains.double_click(arrow).perform()
    time.sleep(3)

arrowFunction()