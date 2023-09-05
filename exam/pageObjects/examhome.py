import time

from selenium.webdriver.common.by import By

class exam_home:
    def __init__(self,driver):
        self.driver =driver

    def launch_app_with_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def google_logo_validation(self,Xpath):
        # click Text box tab
        print(self.driver.title)
        Xpath =self.driver.find_elements(By.XPATH,Xpath)
        assert  len(Xpath)>0

    def validate_google_title(self,title):
        assert self.driver.title==title
    def selectdropdown(self):
        try:
            # self.driver.get("https://www.pizzahut.co.in/")
            self.driver.implicitly_wait(8)

    # Type Address in Address Search Box ...
            time.sleep(5)
            try:
                if self.driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                    self.driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").click()
            except:
                print("Preselect option is not available....")

            if self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").is_displayed():
                self.driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").send_keys("Lulu mall bangalore")
                time.sleep(3)
                if self.driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").is_displayed():
                    self.driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").click()
                    if self.driver.find_element(By.XPATH, "//button[@data-testid='close-offer-collection']").is_displayed():
                        print("User successfully selected the Auto Select drop down option....")
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//div[@data-testid='button-select-collection'][1]").click()
            time.sleep(7)

            # to select the drinks from the header menu

            self.driver.find_element(By.XPATH,"//a[@class='typography-4 side-menu__link side-menu__link--drinks text-white lg:text-black  capitalize lg:border-r']").click()
            time.sleep(4)

            self.driver.find_element(By.XPATH, "//button[@data-synth='button--pepsi-600ml--one-tap']").click()
            time.sleep(2)
            # val = int(float(value))
            # if val <= 350:
            #     print("You can't place order")
            # else:
            #     print("Your Order placed")
            # # click on the Pizza menu
            # self.driver.find_element(By.XPATH, "(//span[text()='Pizzas'])[2]").click()
            # Pizaa Adding....
            # click on the 2 number pizza button
            self.driver.find_element(By.XPATH, "(//span[text()='Pizzas'])[2]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"(//button[@class='button button--md button--green flex-1 font-semibold'])[2]").click()
            time.sleep(3)
            value = self.driver.find_element(By.XPATH,"//a[@class='button button--primary  justify-between']//span[@data-synth='basket-value']").text[1:]
            print("The Value is ", value)

            if int(float(value)) <= 350:
                print("You can't place order")
            else:
                print("Your Order placed")

            # if self.driver.find_element(By.XPATH, "//a[@href='/order/checkout/']").click():
            #     m = self.driver.find_element(By.XPATH, "//span[@class='price-number']").text()
            # # if self.driver.find_element(By.XPATH, "//a[@href='/order/checkout/']//span[@data-synth='basket-value']").text < 350 :
            # print(m)
            # time.sleep(2)


        except:
            self.driver.save_screenshot("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/exam/failed_ss/logo.png")
            print("User is unable to select the Pizza address ....")



