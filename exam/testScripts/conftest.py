import json
import time
import sys

sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/exam')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

# appium



@pytest.fixture()
def browser(request):
    print("initial chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def browser_cls(request):
    print("initial chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()

    yield driver
    driver.quit()
