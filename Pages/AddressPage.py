import time
from Utils import Utils
from selenium.webdriver.support.select import Select


class Address():
    def __init__(self, driver):
        self.driver = driver

        self.FirstName_id = "BillingNewAddress_FirstName"
        self.LastName_id = "BillingNewAddress_LastName"
        self.Email_id = "BillingNewAddress_Email"
        self.Country_xpath = "//Select[@id= 'BillingNewAddress_CountryId']"
        self.State_id = "BillingNewAddress_StateProvinceId"
        self.City_id = "BillingNewAddress_City"
        self.Address1_id = "BillingNewAddress_Address1"
        self.PostCode_id = "BillingNewAddress_ZipPostalCode"
        self.PhoneNo_id = "BillingNewAddress_PhoneNumber"
        self.BillingAddressContinueBTN_xpath = "//div[@id='billing-buttons-container']//input"
        self.ShipAddressContinueBTN_xpath = "//input[@class='button-1 shipping-method-next-step-button']"

    def continueAddress(self):
        self.driver.find_element_by_xpath(self.BillingAddressContinueBTN_xpath).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.driver.find_element_by_xpath(self.ShipAddressContinueBTN_xpath).click()
        time.sleep(5)

    def SelectCountry(self):
        WebElement_Country = self.driver.find_element_by_xpath(self.Country_xpath)
        select_Country = Select(WebElement_Country)
        select_Country.select_by_value("133")

    def AddressInput(self):
        self.driver.find_element_by_id(self.FirstName_id).clear()
        self.driver.find_element_by_id(self.FirstName_id).send_keys(Utils.dict_address.get('First_Name'))
        self.driver.find_element_by_id(self.LastName_id).clear()
        self.driver.find_element_by_id(self.LastName_id).send_keys(Utils.dict_address.get('Last_Name'))
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.find_element_by_id(self.Email_id).clear()
        self.driver.find_element_by_id(self.Email_id).send_keys(Utils.dict_address.get('Guest_Email'))
        self.SelectCountry()
        self.driver.find_element_by_id(self.City_id).send_keys(Utils.dict_address.get('City'))
        self.driver.find_element_by_id(self.Address1_id).send_keys(Utils.dict_address.get('Address1'))
        self.driver.find_element_by_id(self.PostCode_id).send_keys(Utils.dict_address.get('PostCode'))
        self.driver.find_element_by_id(self.PhoneNo_id).send_keys(Utils.dict_address.get('PhoneNo'))
        time.sleep(2)
        self.driver.find_element_by_xpath(self.BillingAddressContinueBTN_xpath).click()
        self.driver.find_element_by_xpath(self.ShipAddressContinueBTN_xpath).click()

    def AddressInputExisting(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        self.SelectCountry()
        self.driver.find_element_by_id(self.City_id).send_keys(Utils.dict_address.get('City'))
        self.driver.find_element_by_id(self.Address1_id).send_keys(Utils.dict_address.get('Address1'))
        self.driver.find_element_by_id(self.PostCode_id).send_keys(Utils.dict_address.get('PostCode'))
        self.driver.find_element_by_id(self.PhoneNo_id).send_keys(Utils.dict_address.get('PhoneNo'))
        self.driver.find_element_by_xpath(self.BillingAddressContinueBTN_xpath).click()
        self.driver.find_element_by_xpath(self.ShipAddressContinueBTN_xpath).click()


""" Selecting state is not mandatory
    def SelectState(self):
        WebElement_State = self.driver.find_element_by_xpath(self.State_id)
        select_State = Select(WebElement_State)
        select_State.select_by_value(133)
"""
