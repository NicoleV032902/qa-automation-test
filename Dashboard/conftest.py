import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Path to the newly downloaded chromedriver and passed it in the object
# service_obj = Service("C:/Users/NCTV_User_010/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# fixture - it will be initially executed before each run of the test cases
# it will initialize the driver object, load the app URL and script will continue

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


# set up iff it will run using a different browser
@pytest.fixture()
def setting_browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../chromedriver/123-0-6312-122.exe")))
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../geckodriver.exe")))
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # this setup will invoke the browser and go to this URL
    driver.get("https://dev-dashboard.n-compass.online/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver

    # Closing the browser after running the test
    driver.close()


@pytest.fixture()
def Admin_Login(request, setting_browser):
    user = {'username': 'nicolev@n-compass.biz', 'password': 'qwerty123'}
    driver = setting_browser
    wait_driver = WebDriverWait(driver, 30)

    username_field = wait_driver.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@ng-reflect-name='username']")))
    username_field.send_keys(user['username'])

    locator = (By.XPATH, "//input[@ng-reflect-name='password']")
    password_field = wait_driver.until(EC.visibility_of_element_located(locator))
    password_field.send_keys(user['password'])

    locator = (By.XPATH, "//button[contains(@class, 'mat-raised-button')]/span[contains(text(), 'LOGIN')]")
    login_button = wait_driver.until(EC.element_to_be_clickable(locator))

    login_button.click()

    try:
        locator = (By.XPATH, "//div[contains(@style, 'justify-content: flex-end')]//button[text()='Close']")
        onLoginClose_button = wait_driver.until(EC.element_to_be_clickable(locator))

        onLoginClose_button.click()

    except Exception as e:
        print(e)

    yield driver


@pytest.fixture()
def DealerAdmin_Login(request, setting_browser):
    user = {'username': 'ricos-dealer-admin@n-compass.biz', 'password': 'qwerty123'}
    driver = setting_browser
    wait_driver = WebDriverWait(driver, 30)

    username_field = wait_driver.until(
        EC.visibility_of_element_located((By.XPATH, "//input[@ng-reflect-name='username']")))
    username_field.send_keys(user['username'])

    locator = (By.XPATH, "//input[@ng-reflect-name='password']")
    password_field = wait_driver.until(EC.visibility_of_element_located(locator))
    password_field.send_keys(user['password'])

    locator = (By.XPATH, "//button[contains(@class, 'mat-raised-button')]/span[contains(text(), 'LOGIN')]")
    login_button = wait_driver.until(EC.element_to_be_clickable(locator))

    login_button.click()

    try:
        locator = (By.XPATH, "//div[contains(@style, 'justify-content: flex-end')]//button[text()='Close']")
        onLoginClose_button = wait_driver.until(EC.element_to_be_clickable(locator))

        onLoginClose_button.click()

    except Exception as e:
        print(e)

    yield driver


@pytest.fixture()
def Dealer_Login(request):
    pass
