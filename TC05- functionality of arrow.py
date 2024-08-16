from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def arrowFunction():
    browser = Firefox()
    browser.get("https://oportunitatisicariere.ro/")
    time.sleep(1)

   # code for using the scroll :

    browser.execute_script(
        "document.getElementsByClassName('how-contribute__jobs swiper swiper-initialized swiper-horizontal')[0].scrollIntoView()")
    time.sleep(3)

    # code for doing the hover on the arrow
    action_chains = ActionChains(browser)
    arrow = browser.find_element(By.XPATH, '/html/body/a/img')
    hover = ActionChains(browser).move_to_element(arrow).perform()
    time.sleep(3)

    # code yo perform the double click on the arrow:
    action_chains.double_click(arrow).perform()
    time.sleep(3)

arrowFunction()