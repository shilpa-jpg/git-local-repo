import unittest
from selenium import webdriver

from pageObjects.practicePage import Practice


class test_practicePage(unittest.TestCase):
    BaseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome(
        "C:\\Users\\shilp\\Downloads\\UFT_One_15.0_DVD\\Unified Functional Testing\\MSI\\Micro Focus\\Unified Functional Testing\\bin\\WebDriver\\chromedriver.exe")
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.BaseURL)
        cls.driver.maximize_window()

    def test_practicePage(self):
        self.prac_obj = Practice(self.driver)
        self.prac_obj.get_practice_page_title()
        self.prac_obj.click_practice_link()
        self.prac_obj.select_radio_btn()
        self.prac_obj.select_dropdown("Benz")
        self.prac_obj.select_checkbox()
        self.prac_obj.click_open_window()
        self.prac_obj.check_alert("Test")
        self.prac_obj.web_table_details()
        self.prac_obj.mouse_hover()
        self.prac_obj.switch_frame("Python")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
