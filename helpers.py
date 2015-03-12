from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import json



class DataAnchors(object):
    """
    DataAnchors holds all the data-anchor selectors required for the tests.
    Keeping them modular ensures tests can be developed and maintained easily.
    """

    #DataAnchors
    _first_name         = (By.XPATH, "//*[@data-anchor='first-name']")
    _last_name		 = (By.XPATH, "//*[@data-anchor='last-name']")
    _date_of_birth = (By.XPATH, "//*[@data-anchor='date-of-birth']")
    _regex_list = ['T', '_', '$', '%', '&', '*', '!',';', '(', ')', '@' ,'[', ']']
    _regex_list_1 = ['T', '_', '$', '%', '&', '*', '!','(', ')', '@' ,'[', ']']
    _save_button = (By.XPATH, "//*[@data-anchor='save-button']")
    _postcode = (By.CSS_SELECTOR, "#PostalContainer #iZipCode")
	

class AppHelpers(object):
    """
    This class should contain any helper elements that the tests might need.
    It helps keeping them here, as they can be reused easily. This class should
    be inherited into the TestCase as they rely on the self.driver defined in
    the test setup.
    """
    def click(self, element):
        """
        Triggers a mouse 'click' on the passed WebElement.
        """
        mouse = ActionChains(self.driver)
        mouse.move_to_element(element).click()
        mouse.perform()

    def hover(self, element):
        """
        simulates hovering the mouse above an element
        """
        mouse = ActionChains(self.driver)
        mouse.move_to_element(element)
        mouse.perform()

    def move(self, fromElement, toElement):
        """
        Drags the passed 'fromElement' WebElement to the 'toElement' WebElement.
        """ 
        mouse = ActionChains(self.driver)
        mouse.click_and_hold(fromElement).move_to_element(toElement).release(fromElement)
        mouse.perform()

    def inputText(self, text, selector):
        """
        Enters text into the passed selector and presses 'Enter'.
        Selector should be an input box / textarea.
        """
        Create = self.driver.find_element(*selector)
        Create.clear()
        Create.send_keys(text + Keys.RETURN)
		
class ChromeSetup(object):
    """
    run the tests in UserStoryTests in Chrome
    """
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://192.168.1.89:5555/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.set_window_size(2000, 2000)
        self.driver.implicitly_wait(10)
        self.driver.set_script_timeout(10)
        self.driver.get(self.url)
        self.driver.execute_script("localStorage.clear()")
				
    def tearDown(self):
        self.driver.save_screenshot('C:\Users\dewilson\Desktop\Auto-SS\error.png')
        self.driver.execute_script("localStorage.clear()")
        self.driver.close()
        self.driver.quit()

class FirefoxSetup(object):
    """
    run the tests in UserStoryTests in Firefox
    """
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(command_executor='http://localhost:5555/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.set_window_size(1500, 1500)
        self.driver.implicitly_wait(10)
        self.driver.set_script_timeout(10)
        self.driver.get(self.url)
        self.driver.execute_script("localStorage.clear()")

    def tearDown(self):
        self.driver.execute_script("localStorage.clear()")
        self.driver.close()
        self.driver.quit()

class IeSetup(object):
    """
    run the tests in UserStoryTests in IE
    """
    def setUp(self):
        #self.driver = webdriver.Ie()
        self.driver = webdriver.Remote(command_executor='http://192.168.1.89:5555/wd/hub',desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        self.driver.implicitly_wait(10)
        self.driver.set_script_timeout(10)
        self.driver.get(self.url)
        self.driver.execute_script("localStorage.clear()")

    def tearDown(self):
        self.driver.execute_script("localStorage.clear()")
        self.driver.close()
        self.driver.quit()

def skipIfNotAvailable(obj):
    """
    this is a helper to determine if we should run the test or not.
    pass in the driver name (as string) and we attempt to use it.
    if not successful the test is skipped.

    TODO: get method where we don't have to run the driver
    """
    try:
        driver = obj()
        driver.close()
        driver.quit()
    except:
        return unittest.skip("Skipping as {0!r} not available".format(obj))
    return lambda func: func
    