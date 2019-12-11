import inspect
import abc
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type in browser name e.g. chrome OR firefox")


@abc.fixture(params=["chrome", "firefox"], scope="class")
def test_setup(request):
    if request.param == "chrome":
        # Local webdriver implementation
        # web_driver = webdriver.Chrome()
        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://192.168.29.70:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    if request.param == "firefox":
        # Local webdriver implementation
        # web_driver = webdriver.Firefox()

        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://192.168.29.70:5555/wd/hub',
            desired_capabilities={'browserName': 'firefox'})
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")


def whoami():
    return inspect.stack()[1][3]

