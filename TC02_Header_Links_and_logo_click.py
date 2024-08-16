import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Test scenario for links from the header menu functionality; each link from the menu should work properly
def menu():
    browser = webdriver.Chrome()
    browser.get("https://oportunitatisicariere.ro/")
    browser.fullscreen_window()
    time.sleep(3)
    links = browser.find_elements(By.XPATH,'//*[@id="top-redirect"]/nav/div[2]/ul/li/a')

    linkshover = browser.find_elements(By.XPATH, '//*[@id="top-redirect"]/nav/div[2]/ul/li/a')

    # Initialize ActionChains
    actions = ActionChains(browser)

    for link in linkshover:
        actions.move_to_element(link).perform()  # Perform hover action
        time.sleep(3)  # Wait for 3 seconds

    for link in links:
        link.click()
        time.sleep(3)
        print(link.get_attribute('href'))

    action_chains = ActionChains(browser)
    logo = browser.find_element(By.XPATH,'/html/body/header/nav/div[1]/div[1]')
    action_chains.double_click(logo).perform()
    time.sleep(3)

    print("All the links are working properly")
    print("Test passed succesfully !")

    '''
    un alt co pentru scrolling ar fi fost : 
    browser.execute_script("window.scrollTo(0,document.body.scroolHeight)")  
    time.sleep(3)
    '''

menu()

