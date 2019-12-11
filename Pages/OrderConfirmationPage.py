import time
class OrderConfirmation():
    def __init__(self, driver):
        self.driver = driver

        self.confirmBtn_xpath = "//input[@class='button-1 confirm-order-next-step-button']"
        self.OrderNo_xpath = "//div[@class='order-number']/strong"

    def OrderConfirmationdetails(self):

        self.driver.execute_script("window.scrollTo(0, 800);")
        self.driver.find_element_by_xpath(self.confirmBtn_xpath).click()
        time.sleep(4)
        OrderNo = self.driver.find_element_by_xpath(self.OrderNo_xpath).text
        print(OrderNo)
        text_file = open('C:/files/file.txt', 'a')
        text_file.writelines("/n"+ OrderNo)
        text_file.close()