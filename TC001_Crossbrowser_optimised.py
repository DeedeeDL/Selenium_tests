
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
import time

site = "https://oportunitatisicariere.ro/"

# Test scenario for cross browser testing - the URL could be opened on different broswers : Chrome , Firefox and Edge
def URL(browser, url):
    browser1 = browser()
    browser1.get(url)
    time.sleep(2)
    print(browser1.title)
    browser1.close()

URL(Chrome, site)
URL(Firefox, site)
URL(Edge, site)
print("Test passed succesfully")
