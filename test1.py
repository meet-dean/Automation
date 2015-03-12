from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from helpers import *
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserStoryTests(AppHelpers):

    url = "http://localhost/xampp/FAT/fields.html"
    def test_FUN_005_add_firstName(self):                                                    
            driver = self.driver
            regex = DataAnchors._regex_list
            length = len(regex)
            for i in range(0,length):
                print regex[i]
                print "pass"
                self.inputText(regex[i], DataAnchors._first_name)
                #self.inputText(" ", DataAnchors._first_name)
                driver.find_element_by_css_selector('#submit').click()
                test = len(driver.find_elements_by_css_selector("#firstNameErrorRegex"))
                self.assertEqual(test, 1)
                if(test == 0):
                    print regex[i]
					
    def test_FUN_010_add_firstName(self):
            self.test_FUN_005_add_firstName()	
            driver = self.driver
            regex = DataAnchors._regex_list_1
            length = len(regex)
            for i in range(0,length):
                print regex[i]
                print "pass"
                self.inputText(regex[i], DataAnchors._first_name)
                #self.inputText(" ", DataAnchors._first_name)
                driver.find_element_by_css_selector('#submit').click()
                test = len(driver.find_elements_by_css_selector("#firstNameErrorRegex"))
                self.assertEqual(test, 1)
                if(test == 0):
                    print "fail"
				

#self.inputText("BT23 4ND", DataAnchors._postcode)
#assert len(driver.find_elements_by_css_selector("#iZipCodeError"))
#error = len(driver.find_elements_by_css_selector("#iZipCodeError"))
#if(error == 0):
#    print "fail"
#    FirefoxSetup.tearDown()			
				
				
			
''' 		   
	def test_FUN_010_add_lastName(self):
	    self.test_FUN_005_add_firstName()
        driver = self.driver
        self.inputText("Wilson@'#~][(*)%19AvB", DataAnchors._last_name)
        #self.click(DataAnchors._middle_yes)
        #self.click(DataAnchors._middle_no)
		
	def test_FUN_010_add_dateOfBirth(self):
	    self.test_FUN_010_add_lastName()
        driver = self.driver
        self.inputText("10/03/91", DataAnchors._date_of_birth)
         
'''		 
'''
           

    def test_ANDES_PPI_PACKAGE_FUN_035_expand_service_with_multiple_packages(self):            
           driver = self.driver

           # expand service with multiple packages.
           self.test_ANDES_PPI_PACKAGE_FUN_030_copy_package()
           self.click(driver.find_element(*DataAnchors._package_select_done_button))
           time.sleep(1)
           self.hover(driver.find_element(*DataAnchors._service))
           self.hover(driver.find_element(*DataAnchors._service_menu))
           expBttn = driver.find_element(*DataAnchors._service_menu_expand)
           time.sleep(1)
           expBttn.click()

           assert len(driver.find_elements_by_css_selector("div.container-body.expanded")) is 2, "Verify service with multiple packages will expand"
'''
#class TestChrome(ChromeSetup, unittest.TestCase, UserStoryTests):
"""
    Tests the UserStoryTests test cases in Chrome.
    The inherited classes are:

    * ChromeSetup - Chrome specific setUp and tearDown methods
    * unittest.TestCase - Indicates that this class is a test
    * UserStoryTests - The class that contains the test
"""

class TestFirefox(FirefoxSetup, unittest.TestCase, UserStoryTests):
    """                                                                                                                                                                                                                    
    Tests the UserStoryTests test cases in Firefox.
    The inherited classes are:

    * FirefoxSetup - Firefox specific setUp and tearDown methods
    * unittest.TestCase - Indicates that this class is a test
    * UserStoryTests - The class that contains the test
    """

#class TestIe(IeSetup, unittest.TestCase, UserStoryTests):
    """
    Tests the UserStoryTests test cases in IE.
    The inherited classes are:

    * IeSetup - IE specific setUp and tearDown methods
    * unittest.TestCase - Indicates that this class is a test
    * UserStoryTests - The class that contains the test
    """

if __name__ == "__main__":
    unittest.main(verbosity=2)
