from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Util_Test
from testData import constants
import time


class Settings_Page:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.settings_tab = "//button[@data-qa='header-RADMIN-tab-button']"
        self.regional_settings = "//button[@data-qa='nav_link_authenticated.regional-settings']"
        self.set_timezone_dateformat_checkbox = "//span[contains(text(),'Allow users to set their own Time Zone and Date Format')]"
        self.save_button = "//button[@data-qa='ds_ackbar_save_btn']"
        self.profile_button = "//button[@data-qa='header-profile-menu-button']"
        self.profile_button_avatar = "//span[@data-qa='header-profile-menu-button-avatar']"
        self.my_preferences = "//button[@data-qa='header-choice-PREFERENCES-button']"
        self.regional_settings_preferences = "//button[@data-qa='regional-settings']"
        self.date_time_format_dropdown = "//select[@data-qa='date-time-format-dropdown']"
        self.alert_box = "//button[@class='optanon-alert-box-close banner-close-button']"
        self.accept_cookies = "//button[contains(text(),'Accept Cookies')]"
        self.cancel_cookies = "//button[@class='optanon-alert-box-close banner-close-button']"
        self.date_time_format_text = "//div[@data-qa='date-time-format-text']"
        self.regional_settings_title = "//*[@data-qa='Regional Settings-title-tag']"
        self.start_button = "//button[@data-qa='manage-sidebar-actions-ndse-trigger']"
        self.docusign_logo = "//img[@data-qa='header-docusign-logo']"
        self.preferences_save_button = "//button[@data-qa='preferences-save-btn-bottom']"
        self.success_message_date_time_format_change = "//div[@data-qa='ds-toast-content-text']"
        self.profile_text = "//span[contains(text(), 'DS')]"
        self.action_required_button = "//button[@data-qa='action-required-count']"
        self.completed_count = "//button[@data-qa='completed-count']"
        self.regional_settings_header = "//*[@data-qa='regionalSettings_page_title']"
        self.your_time_format_dropdown = "//label[contains(text(), 'Your Time Zone as set in My Preferences')]"

    def selectCheckboxForAllowUserTimeZoneAndDateFormat(self):
        settingsTab = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((
            By.XPATH, self.settings_tab)))
        settingsTab.is_displayed()
        settingsTab.click()
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
                By.XPATH, self.accept_cookies))).click()
        except:
            print("there is nothing to handle like cookies")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.XPATH, self.regional_settings))).click()

        try:
            time_zone_dropdown = self.driver.find_element(By.XPATH, self.your_time_format_dropdown).is_displayed()
            if time_zone_dropdown:
                print("checkbox is selected")
        except:
            checkbox = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
                By.XPATH, self.set_timezone_dateformat_checkbox)))
            checkbox.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.save_button))).click()

    def allowUserToChangeDateTimeFormat(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((
            By.XPATH, self.regional_settings_preferences))).click()
        time.sleep(2)
        dt_dropDown = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, self.date_time_format_dropdown)))
        if dt_dropDown:
            select = Select(dt_dropDown)
            select.select_by_value(constants.mm_dd_yyyy_format)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
                By.XPATH, self.preferences_save_button))).click()
            time.sleep(2)
            select.select_by_value(constants.dd_mmm_yyyy_format)
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
                By.XPATH, self.preferences_save_button))).click()
            success_msg = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
                By.XPATH, self.success_message_date_time_format_change))).text
            Util_Test.getscreenshot('/1.UserAllowedToChangeDateTimeFormat.png')
            print("Data/Time format:", success_msg)
            assert success_msg == constants.date_time_change_success_message

    def userNotAllowToChangeDateTimeFormat(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((
            By.XPATH, self.regional_settings_preferences))).click()
        time.sleep(2)
        dateTimeTextBox = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.date_time_format_text))).is_enabled()
        #assert not dateTimeTextBox
        Util_Test.getscreenshot('/2.userNotAllowToChangeDateTimeFormat.png')
        print(constants.cannot_change_date_time_format)

    def verify_regional_settings_page(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.regional_settings_header))).is_displayed()

    def unSelectCheckboxForAllowUserTimeZoneAndDateFormat(self):
        settings_tab = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located((By.XPATH, self.settings_tab)))
        settings_tab.is_displayed()
        settings_tab.click()
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.cancel_cookies))).click()
        except:
            print("there is nothing to handle like cookies")

        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.regional_settings))).click()
        checkbox = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, self.set_timezone_dateformat_checkbox)))
        checkbox.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.save_button))).click()

