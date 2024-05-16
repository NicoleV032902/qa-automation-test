import os

import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException


# Path to the newly downloaded chromedriver and passed it in the object
# service_obj = Service("C:/Users/NCTV_User_010/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# fixture - it will be initially executed before each run of the test cases
# it will initialize the driver object, load the app URL and script will continue

# setup will invoke the browser and go to the URL

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


# set up if it will run using a different browser

@pytest.fixture(scope="class")
def setting_browser(request):
    browser_name = request.config.getoption("browser_name")
    driver = None

    if browser_name == "chrome":
        print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../chromedriver/123-0-6312-122.exe")))
        service_obj = Service(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../chromedriver/123-0-6312-122.exe")))
        driver = webdriver.Chrome(service=service_obj)
        # driver = webdriver.Chrome()
    elif browser_name == "firefox":
        print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../geckodriver.exe")))
        service_obj = Service(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../geckodriver.exe")))
        driver = webdriver.Firefox(service=service_obj)
        # driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://dev-dashboard.n-compass.online/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    # request.cls.driver = driver
    yield
    print("sleep")
    # Closing the browser after running the test
    # driver.close()


# @pytest.fixture()
# def Admin_Login(request):
#     pass
#
#
# @pytest.fixture()
# def DealerAdmin_Login(request):
#     pass
#
#
# @pytest.fixture()
# def Dealer_Login(request):
#     pass
