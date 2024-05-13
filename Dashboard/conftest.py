import pytest
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Path to the newly downloaded chromedriver and passed it in the object
service_obj = Service("C:\Users\NCTV_User_010\Downloads\chromedriver-win64\chromedriver-win64.exe")
driver = webdriver.Chrome(service=service_obj)
