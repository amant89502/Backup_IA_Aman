import json

import pytest
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/Exam_MajorTest')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(scope="class")
def exam_class(request):
    print("Intial chrome Driver")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver=driver
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption("--browser", action="store",help="input browser")

@pytest.fixture(scope="class")
def params(request):
    params={}
    params['browser']=request.config.getoption('--browser')
    return params

@pytest.fixture(scope="class")
def multiBrowserTesting(request, params):
    print("Initiating chrome driver")
    driver=""
    if params['browser']=="chrome":
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if params['browser']=="firefox":
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    request.cls.driver=driver
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    driver.quit()


# json Data set
@pytest.fixture()
def jsonData():
    with open('TestData/testData.json') as config_file:
        data=json.load(config_file)
    return data

