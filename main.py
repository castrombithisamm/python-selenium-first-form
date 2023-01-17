
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(8)
# progress_element = driver.find_element("class name", "progress-label")
# print(f"{progress_element.text == 'Completed!'}")
