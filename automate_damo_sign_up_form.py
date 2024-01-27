import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# Variables
driver_path='chromedriver.exe'
navigate_url = "https://www.techlistic.com/p/selenium-practice-form.html"

class DemoqaTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        self.driver.get(navigate_url)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_automate_form(self):
        # Enter First Name
        first_name = self.driver.find_element(By.NAME,'firstname')
        first_name.send_keys('Jassi')

        # Enter Last Name
        last_name = self.driver.find_element(By.NAME,'lastname')
        last_name.send_keys('Maurya')

        # Click on Gender Radio button
        gender = self.driver.find_element(By.ID, 'gender')
        print(gender.is_selected())
        gender.click()

        # Enter DOB
        dob = self.driver.find_element(By.ID,'datepicker')
        dob.clear()
        dob.send_keys('19 Mar 1990')

        # Select Profession checkbox
        profession = self.driver.find_element(By.ID,'profession-1')
        profession.click()

        # Select Automation tool checkbox
        automation_tool = self.driver.find_element(By.ID,'tool-2')
        automation_tool.click()

        # Click Submit button
        submit_button = self.driver.find_element(By.ID,'submit')
        submit_button.click()

        time.sleep(5)


if __name__=='__main__':
    unittest.main()
