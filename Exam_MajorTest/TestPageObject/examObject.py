import time
import sys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from TestHtmlLocators import examTestLocation
sys.path.append('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/Exam_MajorTest')
from selenium import webdriver

from Reusable import common_Method
class Major_test:
    def __init__(self,driver):
        self.driver=driver

    def launch_web_Url(self,url):
        self.driver.get(url)
        time.sleep(2)

    def logo_validation(self,xpath):
        try:
            print(self.driver.title)
            Xpath=self.driver.find_elements(By.XPATH,xpath)
            assert len(Xpath)>0
            print("Logo Validated")
        except:
            print("Logo Not Found!!")

    # validating the Header Menu.............
    def gnu_Header(self):
        try:
            #xml file will call...........
            list_of_header = common_Method.readXmlAsPerNode("gnuheaderMenu")
            value = list_of_header.split(",")
            for i in value:
                if self.driver.find_element(By.XPATH, examTestLocation.header_validate(i)).is_displayed():
                    print("Header Got .........>>", i)



        except:
            print("Not Fecth Header!!")

    #Redirecting campus Life..........
    def gnu_campusLife(self,xpath,xpath2,xpath3):
        try:
            self.driver.find_element(By.XPATH,xpath).click()
            print("Successfully Redirect to CampusLife")
            time.sleep(5)
            ele = self.driver.find_element(By.XPATH,xpath2)
            Actions = ActionChains(self.driver)
            Actions.move_to_element(ele).perform()
            time.sleep(6)
            if ele.is_displayed():
                print("Found the Gallery in H2")
            else:
                print("Not Found")

            #counting number of images.......

            coun = self.driver.find_elements(By.XPATH,xpath3)
            print("Total Images are", len(coun))

            #printing src value of all present Images......
            for i in coun:
                print(i.text," ---> ",i.get_attribute("src"))
            time.sleep(4)

            # Clicking on logo and move back to Home Page.......
            self.driver.find_element(By.XPATH,examTestLocation.documentation_logo()).click()
            print("The Application Move to Home Page From Campus Life")
            time.sleep(3)








        except:
            print("Not get click!!")

    # Validate News Later..........
    def gnu_validateNewsLater(self,xpath,xpath2):
        ele = self.driver.find_element(By.XPATH, xpath)
        Actions = ActionChains(self.driver)
        Actions.move_to_element(ele).perform()
        time.sleep(6)
        if ele.is_displayed():
            print("Scrolled to News Later...")
            if self.driver.find_element(By.XPATH,xpath2).is_displayed():
                print("Enter Your Email Here --->Text Box Found")
                subscribe,validation=examTestLocation.subscribeClick()
                self.driver.find_element(By.XPATH,subscribe).click()
                print("Clicked On Subscribe")
                '''
                ele = self.driver.find_element(By.XPATH,xpath)
                Actions = ActionChains(self.driver)
                Actions.move_to_element(ele).perform()
                time.sleep(4)
                if self.driver.find_element(By.XPATH,validation).is_displayed():
                    print("Found the Email Not Available Alert")
                else:
                    print("Not Found Alert")
                    '''
            else:
                print("Not Found Email Placeholder....")

        else:
            print("Not Found")


    # Validate InterNational From header Menu..........
    def gnu_International(self,xpath):
        try:
            self.driver.find_element(By.XPATH,xpath).click()
            print("Successfully Redirect to CampusLife")
            time.sleep(5)
            course=self.driver.find_element(By.XPATH,examTestLocation.courseyears()).text
            print(course,"-->This Course Years Validated")

        except:
            print("Not redirected!!")








