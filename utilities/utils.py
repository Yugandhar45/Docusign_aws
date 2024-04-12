import base64
from datetime import datetime
from pyhtml2pdf import converter
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from testData import constants as constants
import pyttsx3
import pandas as pd
from pathlib import Path
import pypdf
import os
import time
from PIL import ImageGrab


def get_project_root() -> Path:
    return Path(__file__).parent.parent


class Util_Test:
    folder_path = constants.screenshots_path

    def __init__(self, driver):
        self.driver = driver

        # Locators:
        self.profile_button = "//button[@data-qa='header-profile-menu-button']"
        self.logoff_button = "button[data-qa='header-logoff-button']"
        self.settings_tab = "//button[@data-qa='header-RADMIN-tab-button']"
        self.regional_settings_field = "//button[@data-qa='nav_link_authenticated.regional-settings']"
        self.regional_settings = "//button[@data-qa='regional-settings']"
        self.allow_user_set_time_zone_format = \
            "//button[@data-qa='regional_settings_allow_user_to_set_time_zone_format_cb']"
        self.dat_time_format_dropdown = "//select[@data-qa='date-time-format-dropdown']"

    def read_data_from_csv(self, fileName):
        date_time_columns = pd.read_csv(fileName, usecols=[
            'Sent On (Date)', 'Sent On (Time)', 'Last Activity (Date)', 'Last Activity (Time)', 'Completed On (Date)',
            'Completed On (Time)'])
        print(date_time_columns)
        assert "Sent On (Date)" in date_time_columns
        assert "Sent On (Time)" in date_time_columns
        assert "Last Activity (Date)" in date_time_columns
        assert "Last Activity (Time)" in date_time_columns
        assert "Completed On (Date)" in date_time_columns
        assert "Completed On (Time)" in date_time_columns
        self.driver.save_screenshot('./screenshots/Envelope_csv_report.png')

    def logout(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((
            By.XPATH, self.profile_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.logoff_button))).click()
        loginpage = WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((
            By.XPATH, "//span [contains(text(),'Log in to DocuSign')]"))).is_displayed()
        assert loginpage

    @staticmethod
    def scroll_page(self):
        self.driver.find_element('css selector', "button[data-qa='tutorial-got-it']").click()
        time.sleep(5)
        self.driver.execute.script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    def switch_to_window(self):
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
                yield
        self.driver.switch_to.window(parentWindow)

    @staticmethod
    def validate_pdf_data(filecontents, first_page=False):
        file = open(filecontents[0], "rb")
        reader = pypdf.PdfReader(file)
        data = ""
        for page in reader.pages:
            data += page.extract_text()
            print(data)
        if first_page:
            pass
        else:
            assert filecontents[2] in data
        assert filecontents[1] in data

    @staticmethod
    def create_directory(test_name):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        folder_name = test_name + '_' + timestamp
        # global folder_path
        Util_Test.folder_path = os.path.join(constants.screenshots_path, folder_name)
        os.makedirs(Util_Test.folder_path)

    @staticmethod
    def getscreenshot(fileName):
        screenshot = ImageGrab.grab()
        filepath = os.path.abspath(Util_Test.folder_path) + fileName
        screenshot.save(filepath)

    @staticmethod
    def convert_html_to_pdf(html_report_path, pdf_report_path):
        path = os.path.abspath(html_report_path)
        converter.convert(f"file:///{path}", pdf_report_path)

    @staticmethod
    def password_encrypt(*args):
        for value_to_encrypt in args:
            string = value_to_encrypt
            encrypt_string = base64.b64encode(string.encode("utf-8"))
            print(value_to_encrypt + ":", encrypt_string)

    @staticmethod
    def password_decrypt(value_to_decrypt):
        string = value_to_decrypt
        decrypt_string = base64.decodebytes(string).decode("utf-8")
        return decrypt_string

    @staticmethod
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def execute_script_with_banner(self, text, apply_fixed_position=True, isBanner=True):
        # Display Banner
        if isBanner:
            text_for_banner = f'<b>{text}</b>'
            script = f''' 
                        var banner = document.createElement('div'); 
                        banner.style.position = '{'fixed' if apply_fixed_position else 'relative'}'; 
                        banner.style.top = '0'; 
                        banner.style.left = '0'; 
                        banner.style.right = '0'; 
                        banner.style.margin = 'auto'; 
                        banner.style.width = '700px'; 
                        banner.style.height = '50px'; 
                        banner.style.backgroundColor = 'yellow'; 
                        banner.style.color = 'black'; 
                        banner.style.textAlign = 'center'; 
                        banner.style.lineHeight = '50px'; 
                        banner.style.zIndex = '9999'; 
                        banner.innerHTML = '{text_for_banner}'; 
                        document.body.appendChild(banner); 
                    '''
            self.driver.execute_script(script)
            # Speak
            # self.speak(text)
