import time
from Utils import Utils


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.email_id = "Email"
        self.password_id = "Password"
        self.loginbutton_xpath = "//input[@class ='button-1 login-button']"
        self.checkOutAsGuestBTN_xpath = "//input[@class ='button-1 checkout-as-guest-button']"

    def Login(self):
        time.sleep(3)
        email = self.driver.find_element_by_id(self.email_id)
        var = email.location_once_scrolled_into_view
        email.send_keys(Utils.Email)
        # self.driver.find_element_by_id(self.email_id).send_keys(Utils.Email)
        self.driver.find_element_by_id(self.password_id).send_keys(Utils.Password)
        self.driver.find_element_by_xpath(self.loginbutton_xpath).click()


    def Checkout_as_Guest(self):
        CheckOutBTN = self.driver.find_element_by_xpath(self.checkOutAsGuestBTN_xpath)
        var = CheckOutBTN.location_once_scrolled_into_view
        CheckOutBTN.click()
    # self.driver.find_element_by_xpath(self.checkOutAsGuestBTN_xpath).click()
