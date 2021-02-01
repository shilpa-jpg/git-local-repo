from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Practice:
    practice_click_xpath = "//a[@href='/pages/practice']"
    radio_btn_id = "bmwradio"
    dropDown_id = "carselect"
    check_box_id = "bmwcheck"
    open_window_id = "openwindow"
    enter_name_alert_txt_id = "name"
    click_alert_btn_id = "alertbtn"
    click_confirmation_alert_btn_id = "confirmbtn"
    get_rows_xpath = "//table/tbody/tr"
    get_columns_xpath = "//table/tbody/tr[2]/td"
    mouse_hover_id = "mousehover"
    search_courses_id = "search-courses"



    def __init__(self, driver):
        self.driver = driver

    def get_practice_page_title(self):
        title = self.driver.title
        print(title)
        assert True

    def click_practice_link(self):
        self.driver.find_element_by_xpath(self.practice_click_xpath).click()

    def select_radio_btn(self):
        radio_btn = self.driver.find_element_by_id(self.radio_btn_id)
        radio_btn.click()
        print(radio_btn.text)

    def select_dropdown(self, value):
        drp = Select(self.driver.find_element_by_id(self.dropDown_id))
        drp.select_by_visible_text(value)

    def select_checkbox(self):
        check_box = self.driver.find_element_by_id(self.check_box_id)
        check_box.click()
        print(check_box.text)

    def click_open_window(self):
        parent_handle = self.driver.current_window_handle
        self.driver.find_element_by_id(self.open_window_id).click()
        handles = self.driver.window_handles
        for child_handle in handles:
            if child_handle not in parent_handle:
                self.driver.switch_to.window(child_handle)
                print("Window switched successfully")
        self.driver.find_element_by_xpath(self.practice_click_xpath).click()
        self.driver.maximize_window()

    def check_alert(self, text):
        self.driver.find_element_by_id(self.enter_name_alert_txt_id).send_keys(text)
        self.driver.find_element_by_id(self.click_alert_btn_id).click()
        if self.driver.switch_to.alert.accept():
            assert True

        # Confirmation Alert
        self.driver.find_element_by_id(self.click_confirmation_alert_btn_id).click()
        self.driver.switch_to.alert.dismiss()

        # Web-Table example

    def web_table_details(self):
        rows = len(self.driver.find_elements_by_xpath(self.get_rows_xpath))
        print("No.of Rows", rows)
        columns = len(self.driver.find_elements_by_xpath(self.get_columns_xpath))
        print("No.of columns", columns)
        for r in range(2, rows + 1):
            for c in range(1, columns + 1):
                value = self.driver.find_element_by_xpath("//table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
                print(value)

    # Mouse Hover example
    def mouse_hover(self):
        mouse_element = self.driver.find_element_by_id(self.mouse_hover_id)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(mouse_element).perform()
            self.driver.find_element_by_xpath("//a[text()='Reload']").click()
            print("Mouse-Hover was successful")

        except Exception as e:
            print("Exception error raised as : {}".format(e))

    # switch into frame example

    def switch_frame(self,text):
        self.driver.switch_to.frame("iframe-name")
        self.driver.find_element_by_id(self.search_courses_id).send_keys(text)
        print("Frame switch was successful")






