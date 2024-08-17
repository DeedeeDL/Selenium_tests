
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
import time

# TC 01 - Cross-browser testing - The website cand be opened with different browsers (Chrome, Firefox and Edge): : Chrome , Firefox and Edge

site = "https://oportunitatisicariere.ro/"

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
