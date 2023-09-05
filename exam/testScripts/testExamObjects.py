import time
import sys
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/exam')
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObjects.examhome import exam_home
from Locators import examlocators

@pytest.mark.usefixtures("browser_cls")
class TestExamApp:
    # @pytest.mark.smoke
    # def test_google_Logo(self):
    #     obj1=exam_home(self.driver)
    #     obj1.launch_app_with_url("https://www.pizzahut.co.in/")
    #     obj1.google_logo_validation(examlocators.pizza_logo())
    # def test_add_address(self):
    #     obj1=exam_home(self.driver)
    #     obj1.launch_app_with_url("https://www.pizzahut.co.in/")
    #     obj1.selectdropdown()
    def test_select_drink(self):

        obj1 = exam_home(self.driver)
        obj1.launch_app_with_url("https://www.pizzahut.co.in/")
        obj1.selectdropdown()








