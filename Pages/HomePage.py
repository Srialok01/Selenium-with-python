from selenium.webdriver.common.action_chains import ActionChains
import time


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.Electronics_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics ')]"
        self.Cell_Phones_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Cell phones')]"
        self.Others_xpath = "//ul[@class='top-menu notmobile']//a[contains(text(),'Others')]"

    def Hover(self):
        hoverElement = self.driver.find_element_by_xpath(self.Electronics_xpath)
        time.sleep(2)
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()
        time.sleep(2)

    def NavigateToCellPhone(self):
        self.Hover()
        self.driver.find_element_by_xpath(self.Cell_Phones_xpath).click()

    def NavigateToOthers(self):
        self.Hover()
        self.driver.find_element_by_xpath(self.Others_xpath).click()
