import time
from selenium.webdriver.support.select import Select
from Utils import Utils


class Payment():
    def __init__(self, driver):
        self.driver = driver

        self.CreditCardRadioBtn_id = "paymentmethod_1"
        self.PaymentContinueBTN_xpath = "//input[@type='button'][@class='button-1 payment-method-next-step-button']"
        self.CardHolderName_id = "CardholderName"
        self.CardNumber_id = "CardNumber"
        self.ExpirationMonth_xpath = "//select[@id='ExpireMonth']"
        self.ExpirationYear_xpath = "//select[@id='ExpireYear']"
        self.CVV_xpath = "//input[@id='CardCode']"
        self.Card_ContinueBTN_xpath = "//input[@class='button-1 payment-info-next-step-button']"

    def PaymentOptions(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.find_element_by_id(self.CreditCardRadioBtn_id).click()
        self.driver.find_element_by_xpath(self.PaymentContinueBTN_xpath).click()
        self.driver.find_element_by_id(self.CardHolderName_id).send_keys(Utils.CardHolderName)
        self.driver.find_element_by_id(self.CardNumber_id).send_keys(Utils.CardNo)
        WebElement_Month = self.driver.find_element_by_xpath(self.ExpirationMonth_xpath)

        select_Expdate = Select(WebElement_Month)
        select_Expdate.select_by_index(6)
        WebElement_Year = self.driver.find_element_by_xpath(self.ExpirationYear_xpath)
        select_ExpYear = Select(WebElement_Year)
        select_ExpYear.select_by_index(5)
        self.driver.find_element_by_xpath(self.CVV_xpath).send_keys(Utils.cvv)
        self.driver.find_element_by_xpath(self.Card_ContinueBTN_xpath).click()
        time.sleep(4)
