import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class OtherItems:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

        self.SoundSpeakers_Linktxt = "Portable Sound Speakers"
        self.Add_to_Cart_xpath = "//input[@id='add-to-cart-button-23']"
        self.shoppingCart_xpath = "//div[@class='header-links']//descendant::span[@class ='cart-label']"
        self.shoppingCartConfirmation_xpath = "//div[@id='bar-notification']//span"
        self.GoToCart_xpath = "//div[@class='buttons']/input[@value='Go to cart']"

    def SelectSpeakers(self):
        self.driver.find_element_by_partial_link_text(self.SoundSpeakers_Linktxt).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Add_to_Cart_xpath).click()
        self.driver.execute_script("window.scrollTo(0, -400);")
        cart_button = WebDriverWait(self.driver, 10).until(
            lambda s: s.find_element_by_xpath(self.shoppingCartConfirmation_xpath))
        cart_button.click()
        self.driver.execute_script("window.scrollTo(0, -300);")
        self.Hover()

    def Hover(self):
        hoverElement = self.driver.find_element_by_xpath(self.shoppingCart_xpath)
        time.sleep(2)
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.GoToCart_xpath).click()

