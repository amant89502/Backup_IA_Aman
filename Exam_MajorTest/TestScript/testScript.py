import time
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/Exam_MajorTest')
from selenium import webdriver
from TestHtmlLocators import examTestLocation
from TestPageObject.examObject import Major_test
from Reusable import common_Method

@pytest.mark.usefixtures("multiBrowserTesting")
class Test_Script:

    def test_validateLogo(self,jsonData):
        obj1 = Major_test(self.driver)
        #here called the json data
        obj1.launch_web_Url(jsonData['url_ganpat'])
        obj1.logo_validation(examTestLocation.documentation_logo())
        time.sleep(2)

    #Header Validating from xml file.....
    def test_Header_validate(self,jsonData):
        obj1 = Major_test(self.driver)
        # here called the json data
        obj1.launch_web_Url(jsonData['url_ganpat'])
        obj1.gnu_Header()
        time.sleep(2)

    #Redirecting the campus Life Page...
    def test_CampusLife(self,jsonData):
        obj1 = Major_test(self.driver)
        # here called the json data
        obj1.launch_web_Url(jsonData['url_ganpat'])
        obj1.gnu_campusLife(examTestLocation.campusLife(),examTestLocation.gallery(),examTestLocation.images())
        time.sleep(3)

     # Scroll New Later and Validate...
    def test_newsLater(self, jsonData):
        obj1 = Major_test(self.driver)
        # here called the json data
        obj1.launch_web_Url(jsonData['url_ganpat'])
        obj1.gnu_validateNewsLater(examTestLocation.validateNewslater(),examTestLocation.validateEMailText())
        time.sleep(2)

 # Click on International and Validate...

    def test_international(self, jsonData):
        obj1 = Major_test(self.driver)
        # here called the json data
        obj1.launch_web_Url(jsonData['url_ganpat'])
        obj1.gnu_International(examTestLocation.international())
        time.sleep(2)




