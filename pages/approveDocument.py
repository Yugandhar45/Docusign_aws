from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.loginPage import Login_Page
from testData import constants as constants
from utilities.utils import Util_Test
import time


class Approve_Envelope:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        # Elements:
        self.continue_button = "action-bar-btn-continue"
        self.sign_field = "(//*[contains(@class, 'signature-tab-content')])[index]"
        self.signing_reason = "signingReason"
        self.dialog_submit = "button[data-qa='dialog-submit']"
        self.cfr_continue_button = "button[data-qa='cfr-continue']"
        self.comment_entry_field = "//input[contains(@id,'tab-form-element-')]"
        self.finish_button = "//button[@id='action-bar-btn-finish']"
        self.no_thanks_button = "//button[@data-qa='sign-next-no-thanks']"
        self.other_actions = "//button[@data-qa='toggle-other-actions']"
        # Options under oth actions
        self.finish_later_button = ("//div[contains(@class,'menu below right visible')]//button[contains(text(),"
                                    "'Finish Later')]")
        self.decline_to_sign_button = ("//div[contains(@class,'menu below right visible')]//button[contains(text(),"
                                       "'Decline to Sign')]")
        self.help_support_button = ("//div[contains(@class,'menu below right visible')]//span[contains(text(),'Help & "
                                    "Support')]")
        self.about_docusign_button = ("//div[contains(@class,'menu below right visible')]//span[contains(text(),"
                                      "'About Docusign')]")
        self.view_history_button = ("//div[contains(@class,'menu below right visible')]//button[contains(text(),"
                                    "'View History')]")
        self.decline_continue_button = "//button[@data-qa='show-decline-to-sign']"
        self.decline_reason_text_box = "//textarea[@data-qa='decline-dialog-reason-text']"
        self.dialog_decline_to_sign = "//button[@data-qa='decline-dialog-decline-to-sign']"
        self.document_status = "//span[@data-qa='detail-status-title']"
        # Document Detail Page W.r.t to sender
        self.correct_btn = "//span[contains(text(),'Correct')]"
        self.move_btn = "//span[contains(text(),'Move')]"
        self.resend_btn = "//span[contains(text(),'Resend')]"
        self.more_btn = "//button[@data-qa='document-more']"
        self.void_option = "//button[@data-qa='envelope-action-void']"
        self.void_reason_box = "//*[@data-qa='input-reason-for-voiding']"
        self.void_button = "//button[@data-qa='modal-confirm-btn']"
        self.docusign_logo = "img[data-qa='header-docusign-logo']"
        self.sent_item = "//span[@class='menu_itemIcon icon-sent']"
        # action items under more button
        self.copy_option = "//button[@data-qa='envelope-action-clone']"
        self.save_template_option = "//button[@data-qa='envelope-action-save_as_template']"
        self.void_option = "//button[@data-qa='envelope-action-void']"
        self.history_option = "//button[@data-qa='envelope-action-history']"
        self.form_data_option = "//button[@data-qa='envelope-action-download_form_data']"
        self.transfer_ownership_option = "//button[@data-qa='envelope-action-transfer_custody']"
        self.export_as_csv_option = "//button[@data-qa='envelope-action-export_as_csv']"
        self.delete_option = "//button[@data-qa='envelope-action-delete']"
        self.sign_next = "//span[@data-qa='sign-next-title-heading']"
        # Validating the option under Reason for signing Popup
        self.signatory_name_option = "//span[contains(text(),'Signatory Name')]"
        self.signatory_email_option = "//span[contains(text(),'Signatory Email')]"
        self.signing_reason_option = "//label[contains(text(),'Signing Reason')]"
        # validating the option under reason for signing dropdown
        self.approve_doc_option = "//option[contains(text(),'I approve this document')]"
        self.review_doc_option = "//option[contains(text(),'I have reviewed this document')]"
        self.author_doc_option = "//option[contains(text(),'I am the author of this document')]"
        self.required_label = "//label[normalize-space()='Required']"
        self.access_code_textbox = "//input[@id='ds_hldrBdy_txtAccessCode']"
        self.validate_access_code_button = "//button[@id='ds_hldrBdy_btnDSAccessCode_btnInline']"

    def clickContinueBtnForSigning(self):
        continue_btn = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.ID, self.continue_button)))
        assert continue_btn.is_displayed(), 'continue button is not displayed'
        continue_btn.click()

    def clickSecondarySignButton(self, index_value):
        sign_field = self.sign_field.replace('index', index_value)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, sign_field))).click()

    def e_sign_reason(self, verifyOptions=False, screenshot=False):
        drop_down = self.driver.find_element(By.ID, self.signing_reason)
        select_method = Select(drop_down)
        if verifyOptions:
            assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
                By.XPATH, xpath))).is_displayed() for xpath in
                       [self.approve_doc_option, self.review_doc_option, self.author_doc_option])

        select_method.select_by_visible_text(constants.signingReason)
        if screenshot:
            self.utils.getscreenshot('/3.1.signing_reason.png')

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dialog_submit))).click()

    def switchToNewTab(self, email, password, screenshot=False):
        parent_window = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        login = Login_Page(self.driver)
        if screenshot:
            login.login_page(email, password, True)
            time.sleep(4)
        else:
            login.login_page(email, password)
            time.sleep(4)
        self.driver.switch_to.window(parent_window)

    def verify_required_message(self):
        assert WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.required_label))).is_displayed()

    def add_comment(self):
        #comments = f"{constants.comment_field} - {generated_text}"
        comments = constants.comment_field
        comment_text_field = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, self.comment_entry_field)))
        assert comment_text_field.is_displayed(), 'Comment field is not displayed'
        comment_text_field.send_keys(comments)

    def click_finish_btn(self):
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.finish_button))).click()
        try:
            signNextDialogBox = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.sign_next)))
            assert constants.signNext_PopUp_text in signNextDialogBox.text, \
                f"Expected text '{constants.signNext_PopUp_text}' not found in dialog box"
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.no_thanks_button))).click()
            time.sleep(2)
        except:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
                    By.CSS_SELECTOR, self.docusign_logo)))
            except:
                print('Docusign Logo is not displaying')

        time.sleep(5)

    def click_continue_btn(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cfr_continue_button))).click()

    def decline_envelope(self, decline_reason):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.other_actions))).click()
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.finish_later_button, self.decline_to_sign_button, self.help_support_button,
                    self.about_docusign_button, self.view_history_button])
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.decline_to_sign_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.decline_continue_button))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, self.decline_reason_text_box))).send_keys(decline_reason)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, self.dialog_decline_to_sign))).click()

    def validateButtonsInDocumentDetailPage(self):
        # verifying the buttons in send document details page W.R.T Sender
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, value))).is_displayed() for value in
                   [self.correct_btn, self.move_btn, self.resend_btn, self.more_btn])

    def click_more_btn(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.more_btn))).click()

    def validateOptionsUnderMoreButton(self):
        assert all(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.copy_option, self.save_template_option, self.void_option, self.history_option,
                    self.form_data_option, self.transfer_ownership_option, self.export_as_csv_option,
                    self.delete_option])

    def voiding_envelope(self, void_reason):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_option))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_reason_box))).send_keys(void_reason)
        utils = Util_Test(self.driver)
        utils.getscreenshot('/1.Reason_for_voiding.png')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.void_button))).click()
        time.sleep(2)

    def validate_doc_status(self, doc_status):
        get_doc_status = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((
            By.XPATH, self.document_status))).text
        assert get_doc_status == doc_status

    def verifyReasonForSigningPopUpOptions(self):
        assert all(WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, xpath))).is_displayed() for xpath in
                   [self.signatory_name_option, self.signatory_email_option, self.signing_reason_option])

    def validate_access_code(self, accesscode):
        WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((
            By.XPATH, self.access_code_textbox))).send_keys(accesscode)
        self.utils.getscreenshot('/2.Before_Validating_Access_Code.png')
        WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((
            By.XPATH, self.validate_access_code_button))).click()
        time.sleep(5)
        self.utils.getscreenshot('/3.After_Validating_Access_Code.png')
