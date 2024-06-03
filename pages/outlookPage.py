from utilities.utils import Util_Test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Outlook_Page:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        self.user_name = "//input[@type='email']"
        self.submit_userName = "//input[@type='submit']"
        self.password = "//input[@type='password']"
        self.submit_password = "//input[@data-report-event='Signin_Submit']"
        self.home_page_title = "header-home-desktop"
        self.start_button = "//img[@alt='DocuSign']"
        self.check_box = "//input[@name='DontShowAgain']"
        self.Yes = "//input[@value='Yes']"
        self.recent_mail = "//span[contains(text(),'plaintext')][1]"
        self.reason_for_decline = "//div[contains(text(),'Testing')]"
        self.reason_for_void = "//p[contains(text(),'voided for the following reason')]"
        self.others_tab = "//button[@data-content='Other']"
        self.outlook_completed_text = "//p[contains(text(), 'All signers completed Complete with DocuSign')]"
        self.click_summary = "//div[@title='Summary.pdf']"
        self.download_btn = "//button[@aria-label='Download']"
        self.print_button = "//button[@name='Print']"
        self.close_report_btn = "//button[@title='Close']"
        self.Review_Document = "//td/a/span[contains(text(),'REVIEW DOCUMENT')]"
        self.microsoft_logo = "//img[@class='logo']"
        self.home_button = "//span[contains(text(),'Home') and contains(@class,'ms-Button')]"

    def loginToOutlook(self, username, password):
        logo = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.microsoft_logo))).is_displayed()
        assert logo
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name))).send_keys(username)
        self.driver.find_element(By.XPATH, self.submit_userName).click()
        password = Util_Test.password_decrypt(password)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.password))).send_keys(password)
        self.driver.find_element(By.XPATH, self.submit_password).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.Yes))).click()
        home_tab = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.home_button))).is_displayed()
        assert home_tab

    def clickRecentEmail(self, recent_mail_text):
        recent_mail = self.recent_mail.replace('plaintext', recent_mail_text)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, recent_mail))).click()
        time.sleep(2)

    def clickOtherFieldTab(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.others_tab))).click()

    def review_Document(self,screenshot=False):
        review_document_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.Review_Document)))
        self.driver.execute_script("arguments[0].scrollIntoView();", review_document_button)
        assert review_document_button.is_displayed(), 'review document button is not displayed'
        if screenshot:
            self.utils.getscreenshot('/3.Review_Document_Through_Outlook_notification.png')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.Review_Document))).click()
        time.sleep(2)

    def validateDeclineReason(self, expected_reason):
        reason = self.reason_for_decline.replace('Testing', expected_reason)
        reason_text = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, reason))).is_displayed()
        assert reason_text

    def validateVoidReason(self, expected_reason):
        void_reason = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.reason_for_void))).is_displayed()
        if void_reason:
            reason_text = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.reason_for_void))).text
            print('actual reason =', reason_text)
            assert expected_reason in reason_text

    def verifyCompletedEnvelope(self):
        sender_notification = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.outlook_completed_text)))
        assert sender_notification.is_displayed(), ('All signers completed Complete with DocuSign: Envelope1.docx, '
                                                    'Envelope2.pdf is not present')

    def download_Envelope_summary_pdf(self):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.click_summary))).click()
        time.sleep(10)
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.print_button, self.download_btn])
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.download_btn))).click()
        time.sleep(10)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.close_report_btn))).click()
