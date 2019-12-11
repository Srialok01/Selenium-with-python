import time


class CartPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.cart_quantity_xpath = "//td[@class='quantity']//input[@class='qty-input']"
        self.terms_Conditions_id = "termsofservice"
        self.checkout_Button_id = "checkout"

    def cart_validation(self):
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.find_element_by_id(self.terms_Conditions_id).click()
        self.driver.find_element_by_id(self.checkout_Button_id).click()
        time.sleep(3)
