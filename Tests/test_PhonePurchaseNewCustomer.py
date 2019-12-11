import allure
import moment
import pytest

from Utils import Utils

from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_CellPhonePage import CellPhonePage
from Pages.LoginPage import LoginPage

from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation
from Utils.SS import SS


@pytest.mark.skip(" I don't want to execute this now")


@pytest.mark.usefixtures("test_setup")


class Test_PhonePurchaseNewCustomer():
    global ss_path
    ss_path = '/PhonePurchaseNewCustomer/'

    def test_01HomePage(self):
        driver = self.driver

        homeObj = HomePage(driver)
        homeObj.NavigateToCellPhone()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_02Phone_buy(self):
        driver = self.driver
        cellObj = CellPhonePage(driver)
        cellObj.SelectPhone()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_03Cart_validations(self):
        driver = self.driver
        cartObj = CartPage(driver)
        cartObj.cart_validation()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_04Login(self):
        driver = self.driver
        loginObj = LoginPage(driver)
        loginObj.Checkout_as_Guest()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)
    def test_05Address(self):
        driver = self.driver
        addressObj = Address(driver)
        addressObj.AddressInput()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_06Payment(self):
        driver = self.driver
        paymentObj = Payment(driver)
        paymentObj.PaymentOptions()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_07OrderConfirmation(self):
        driver = self.driver
        orderConfObj = OrderConfirmation(driver)
        orderConfObj.OrderConfirmationdetails()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)