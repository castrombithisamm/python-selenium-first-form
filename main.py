
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

try:
    no_button = driver.find_element("class name", "at-cm-no-button")
    no_button()
except:
    print("No element with this class name. Skipping ...")

sum1 = driver.find_element("id", "sum1")
sum2 = driver.find_element("id", "sum2")

sum1.send_keys(15)
sum2.send_keys(15)
