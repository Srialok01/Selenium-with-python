import time


class CheckOut():
    def __init__(self, driver):
        self.driver = driver

        self.termsAndConditions_id = "termsofservice"
        self.CheckOutButton_xpath = "//button[@id='checkout']"

    def Check_out(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.find_element_by_id(self.termsAndConditions_id).click()
        self.driver.find_element_by_xpath(self.CheckOutButton_xpath).click()
        time.sleep(4)
