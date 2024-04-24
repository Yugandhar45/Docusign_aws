from pages.outlookPage import Outlook_Page
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.approveDocument import Approve_Envelope
from utilities.utils import Util_Test
from pages.downloads_page import Download_Page
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_SendEnvelope_Approve:
    def test_send_envelope_approve(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        add_sign = Add_Sign_Tags(driver)
        utils = Util_Test(driver)
        utils.create_directory(request.node.name)
        login.login_page(constants.sender_email, constants.sender_password)
        utils.execute_script_with_banner("Entering the valid credentials (username and password) to log in as the "
                                         "sender")
        home.validate_home_page()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        home.click_start_button()
        home.send_envelope()
        upload.upload_envelope_documents(constants.envelope1_docx, False)
        upload.upload_envelope_documents(constants.envelope2_pdf, False)
        utils.execute_script_with_banner("Adding two recipients and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
        add_sign.addSignatureTag(350)
        utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
        add_sign.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
        add_sign.addSignatureTag(650)
        utils.getscreenshot('/1.Adding_signature_Tags_for_Envelope1.png')
        utils.execute_script_with_banner("Selecting the second document to add the Sign tags")
        add_sign.scroll_to_next_envelope()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
        add_sign.select_signer(constants.index_one)
        add_sign.addSignatureTag(350)
        utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
        add_sign.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
        add_sign.addSignatureTag(650)
        utils.getscreenshot('/2.Adding_signature_Tags_for_Envelope2.png')
        add_sign.click_send_btn()
        # Change signature routing order
        upload.navigateToEnvelope(constants.select_2envelopes, True)
        upload.verifyButtonsForSenderInDocumentDetailPage()
        upload.correctingDocumentDetails()
        # upload.envelope_correction(constants.select_2envelopes)
        upload.clickSetSigningOrderCheckbox()
        upload.set_routing_order(constants.index_one, constants.index_two)
        upload.click_next_btn()
        add_sign.clickCorrectToResendDocument()
        upload.navigateToEnvelope(constants.select_2envelopes, True)
        upload.verifyCorrectedRoutedOrder(constants.select_2envelopes)
        utils.execute_script_with_banner("Logout as Sender, After sending Document")
        utils.logout()

        # Login as approver2 and complete e-sign
        driver.get(constants.baseUrl)
        approve = Approve_Envelope(driver)
        utils.execute_script_with_banner("Login as Signer", False)
        login.login_page(constants.signer2_email, constants.signer2_password)
        home.validate_home_page()
        utils.execute_script_with_banner("Selecting the assign task Document")
        upload.navigateToEnvelope(constants.select_2envelopes)
        upload.clickPrimarySignButton()
        login.login_page(constants.signer2_email, constants.signer2_password)
        approve.clickContinueBtnForSigning()
        utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
        approve.clickSecondarySignButton(constants.index_one)
        approve.e_sign_reason()
        approve.click_continue_btn()
        approve.switchToNewTab(constants.signer2_email, constants.signer2_password)
        approve.clickSecondarySignButton(constants.index_two)
        approve.verifyReasonForSigningPopUpOptions()
        approve.e_sign_reason()
        approve.switchToNewTab(constants.signer2_email, constants.signer2_password)
        approve.click_finish_btn()
        utils.execute_script_with_banner("Logout as Signer after completing the process")
        utils.logout()

        # Login as approver1 and complete e-sign
        driver.get(constants.baseUrl)
        utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
        login.login_page(constants.signer1_email, constants.signer1_password)
        home.validate_home_page()
        utils.execute_script_with_banner("Selecting the assign task Document")
        upload.navigateToEnvelope(constants.select_2envelopes)
        upload.clickPrimarySignButton()
        #login.login_page(constants.signer1_email, constants.signer1_password)
        approve.clickContinueBtnForSigning()
        utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
        approve.clickSecondarySignButton(constants.index_one)
        approve.e_sign_reason()
        approve.click_continue_btn()
        approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
        approve.clickSecondarySignButton(constants.index_two)
        approve.e_sign_reason()
        approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
        approve.click_finish_btn()
        utils.execute_script_with_banner("Logout as Signer1 after completing the process")
        utils.logout()

    # Combine and download all docs
    def test_download_allDocuments(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        # Navigate to document for download
        download = Download_Page(driver)
        utils.execute_script_with_banner("Navigate to the Document download option")
        download.navigate_to_document_download(constants.select_2envelopes)
        utils.execute_script_with_banner("Deleting the Existing document from the folder")
        download.delete_existing_doc(constants.pdf_file_path)
        envelope_id_text = download.getting_envelope_id()
        envelope_id_text = envelope_id_text.upper()
        envelope_id_text2 = envelope_id_text.replace("-", "")
        print("Envelope_id from Test method = ", envelope_id_text)
        # Combine and download the all PDFs into one
        download.combine_download(True)
        file_contents = [constants.pdf_file_path, envelope_id_text2, constants.coc_text]
        utils.execute_script_with_banner("Validating and Verifying the Downloaded document")
        Util_Test.validate_pdf_data(file_contents)
        utils.execute_script_with_banner("Logout as Sender after completing the process")
        utils.logout()

    def test_envelope_completion_notification(self, request):
        driver = request.cls.driver
        driver.get(constants.outlook_url)
        outlook = Outlook_Page(driver)
        utils = Util_Test(driver)
        outlook.loginToOutlook(constants.sender_email, constants.sender_password_outlook)
        #outlook.clickOtherFieldTab()
        outlook.clickRecentEmail(constants.recent_mail_completed_envelope)
        outlook.verifyCompletedEnvelope()
        utils.getscreenshot('/4.Envelope_completed_notification.png')
