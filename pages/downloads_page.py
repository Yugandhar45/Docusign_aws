from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from testData import constants as constants
import time
import os
from utilities.utils import Util_Test


class Download_Page:

    def __init__(self, driver):
        self.driver = driver
        # Elements:
        self.action_completed = "//span[@data-qa='completed-count-count']"
        self.document_status = "//span[@data-qa='detail-status-title']"
        self.download_button = "//button[@data-qa='document-download-button']"
        self.combine_all_pdfs_checkbox = "//span[@data-qa='download-combined-label-label-text']"
        self.download_combine_button = "button[data-qa='download-document-button']"
        self.envelope_id_link = "span[data-qa='envelope-id-link-text']"
        self.envelope_id = "p[data-qa='document-id']"
        self.select_document = "//button[@aria-label='Complete with Docusign: document_name']"
        self.start_button = "button[data-qa='manage-sidebar-actions-ndse-trigger']"
        self.all_checkbox = "//span[@data-qa='download-all-label-label-text']"
        self.document_checkbox = "//span[contains(text(),'Document')]"
        self.certificate_of_completion_checkbox = "//span[contains(text(),'Certificate of Completion')]"

    def navigate_to_document_download(self, fileName):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).is_displayed()
        action_completed = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, self.action_completed)))
        self.driver.execute_script("arguments[0].click();", action_completed)
        time.sleep(5)
        select_doc = self.select_document.replace("document_name", fileName)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, select_doc))).click()
        doc_status = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, self.document_status))).text
        print("document Status :", doc_status)
        assert constants.completed_docusign_status in doc_status

    def combine_download(self, screenshot=False):
        download_btn = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.download_button)))
        assert download_btn.is_displayed(), 'Download button is not Displayed'
        assert download_btn.is_enabled(), 'Download button is not Enabled'
        download_btn.click()
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.all_checkbox, self.document_checkbox,
                    self.certificate_of_completion_checkbox, self.combine_all_pdfs_checkbox])
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.combine_all_pdfs_checkbox))).click()
        if screenshot:
            utils = Util_Test(self.driver)
            utils.getscreenshot('/5.Downloading_the_Combined_pdf_documents.png')
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.download_combine_button))).click()
        time.sleep(25)

    def getting_envelope_id(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.envelope_id_link))).click()
        envelope_id = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.envelope_id))).text
        print("Envelope_id = ", envelope_id)
        return envelope_id

    @staticmethod
    def delete_existing_doc(filepath):

        if os.path.exists(filepath):
            # Delete the File in the file path
            os.remove(filepath)
            print("Deleted already existing file with same name")
        else:
            print("No file is existing with same name")
