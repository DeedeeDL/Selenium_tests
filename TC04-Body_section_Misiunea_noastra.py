from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Test cases for "Misiunea noastra" section :
def searching_bar():
    # Initialize the browser
    browser = Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.maximize_window()  # Use maximize_window() instead of fullscreen
    time.sleep(1)

    # Locate and interact with "Misiunea noastra" section
    link = browser.find_element(By.LINK_TEXT, 'Misiunea noastră')
    link.click()
    time.sleep(2)

    #Locate and interact with "peviitor" link from "Misiunea noastra" section
    vlink = browser.find_element(By.XPATH, '//a[contains(@href,"https://peviitor.ro/")]')
    vlink.click()
    time.sleep(3)

    # Switch to the new window that opened
    original_window = browser.current_window_handle
    all_windows = browser.window_handles

    # Assume the new window is the last one opened
    for window in all_windows:
        if window != original_window:
            browser.switch_to.window(window)
            break

    # You can close the new window after performing actions
    browser.close()

    # Switch back to the original window
    browser.switch_to.window(original_window)

    # A little scroll on the section "Misiunea noastra":
    browser.execute_script("window.scrollTo(0, 800)")

    # Locate and interact with the iframe part in the "Misiunea noastra" section:
    frame = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(frame)
    time.sleep(2)

    # A little scroll into the child window :
    browser.execute_script("window.scrollTo(100, 200)")
    time.sleep(2)


    # Testing the searching field from iframe:
    searching = browser.find_element(By.XPATH, '//input')
    time.sleep(2)
    searching.send_keys("tester")
    time.sleep(3)
    searching.send_keys(Keys.ENTER)
    time.sleep(5)

    # Scrolling down through the jobs incrementally
    scroll_steps = [300, 400, 600, 800, 1000, 1200,1500]
    for step in scroll_steps:
        browser.execute_script(f"window.scrollTo(0, {step})")
        time.sleep(2)

    # Press the Arrow image button which leads at the begining of the child window :

    arrowImage = browser.find_element(By.CSS_SELECTOR,"img[src='/static/media/scroll-up.411ad404d02c0e10d2450b18e6098fd5.svg']")
    action_chains = ActionChains(browser)
    action_chains.double_click(arrowImage).perform()
    time.sleep(3)

    # Press on the "X" button from the searching bar:
    xButton = browser.find_element(By.TAG_NAME, 'span')
    action_chains = ActionChains(browser)
    action_chains.double_click(xButton).perform()
    time.sleep(3)


    # Verify the buttons from the filters:

    oras = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/button")
    oras.click()
    time.sleep(2)
    checkbox = browser.find_element(By.ID,'Abrud')
    actions = ActionChains(browser)

    actions.move_to_element(checkbox).click().perform()
    actions.move_to_element(checkbox).click().perform()
    time.sleep(2)
    checkbox = browser.find_element(By.ID, 'Adjud')
    actions = ActionChains(browser)
    actions.move_to_element(checkbox).click().perform()
    time.sleep(3)


    # Verify "Cauta" button functionality :
    cautaButton = browser.find_element(By.CSS_SELECTOR, "button")
    cautaButton.click()
    time.sleep(1)
    scroll_steps2 = [300, 500,700,900, 1100]
    for step in scroll_steps2:
        browser.execute_script(f"window.scrollTo(0, {step})")
        time.sleep(2)

    # Press again the Arrow image button which leads at the begining of the child window :

    arrowImage = browser.find_element(By.CSS_SELECTOR, "img[src='/static/media/scroll-up.411ad404d02c0e10d2450b18e6098fd5.svg']")
    action_chains = ActionChains(browser)
    action_chains.double_click(arrowImage).perform()
    time.sleep(3)

    # Verify logo functionality :
    logo = browser.find_element(By.XPATH, '//img[contains(@src,"/static/media/logo")]')
    action_chains = ActionChains(browser)
    action_chains.double_click(logo).perform()
    time.sleep(2)

    # Scroll to the element with the link text "ASOCIATIA OPORTUNITATI SI CARIERE"
    browser.execute_script(
        "document.getElementsByTagName('footer')[0].scrollIntoView()")
    time.sleep(3)


    #Double click on the link "Asociatia...":
    vlink2 = browser.find_element(By.CLASS_NAME, 'font-bold')
    vlink2.click()
    time.sleep(3)
    browser.quit()

searching_bar()
