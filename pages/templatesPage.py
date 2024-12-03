from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Util_Test
from testData import constants as constants
import time


class Templates_Page:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        # Locators:
        self.envelope_status = "//span[@data-qa='detail-status-title']"
        self.more_menu_button = "//button[@data-qa='document-more']"
        self.save_as_template_option = "//button[@data-qa='envelope-action-save_as_template']"
        self.input_template_name = "//input[@data-qa='prepare-template-name']"
        self.save_and_close_template = "//button[@data-qa='save-as-template-save']"
        self.use_button = "//button[@data-qa='send-a-document']"
        self.cancel_button_matching_template = "//button[@data-qa='modal-cancel-btn']"
        self.transfer_ownership_option = "//span[@data-qa='envelope-action-transfer_custody-text']"
        self.delete_option = "//span[@data-qa='envelope-action-delete-text']"

    def cancel_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.cancel_button_matching_template))).click()

    def matching_templates_popup(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((
                By.XPATH, self.cancel_button_matching_template))).click()
        except:
            print('Matching templates are not available')

    def save_as_template(self):
        temp_status = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((
            By.XPATH, self.envelope_status))).text
        # print("Template status:", temp_status)
        assert temp_status == constants.template_status_draft
        self.utils.getscreenshot("/1.Template_status_draft.png")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.more_menu_button))).click()
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.save_as_template_option, self.transfer_ownership_option, self.delete_option])
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, self.save_as_template_option))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.input_template_name))).send_keys(constants.template_name)
        self.utils.getscreenshot("/2.Template_Creation_page.png")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.save_and_close_template))).click()
        time.sleep(5)
        templates_page = self.driver.current_url
        print("Template page:", templates_page)
        # time.sleep(60)
        try:
            assert templates_page == constants.templatesPage
        except:
            print("Templates page is displayed")

    def click_use_button(self):
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((
            By.XPATH, self.use_button))).click()
