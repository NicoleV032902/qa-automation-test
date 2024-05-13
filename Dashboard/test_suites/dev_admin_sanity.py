import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    driver = webdriver.Chrome()
    time.sleep(2)

except WebDriverException as e:
    print("An error occurred:", e)

