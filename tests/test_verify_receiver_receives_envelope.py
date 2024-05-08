import time
from pages.outlookPage import Outlook_Page
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from pages.addSignTagPage import Add_Sign_Tags
from pages.downloads_page import Download_Page
from pages.approveDocument import Approve_Envelope
from testData import constants as constants
import pytest
from utilities.utils import Util_Test


@pytest.mark.usefixtures("test_setup")
class Test_ReceiverReceivesEnvelope:
    envelope_id = ''

    def testReceiverReceivesEnvelope(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        download = Download_Page(driver)
        approve = Approve_Envelope(driver)
        utils = Util_Test(driver)
        signTags = Add_Sign_Tags(driver)
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner("Started the Execution for verify receiver receives envelop")
        utils.execute_script_with_banner(
            "Entering the valid credentials to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)

        # Upload docx envelope file
        home.click_start_button()
        utils.execute_script_with_banner("Clicking on the start button to send document")
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        upload.upload_envelope_documents(constants.envelope1_docx, False)
        upload.clickSetSigningOrderCheckbox()
        utils.execute_script_with_banner("Adding recipient-1 and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Adding recipient-2 and other details:")
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
        utils.execute_script_with_banner("Selecting \"receives a copy option\" for signer2")
        upload.SelectRecipientAction()
        utils.getscreenshot('/1.Signer1_and_Signer2_Action-types.png')
        utils.execute_script_with_banner("clicking on Next Button to send a document to signer1")
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding signature tag for signer1")
        signTags.addSignatureTag(350)
        utils.execute_script_with_banner("Sending Document to Signers")
        signTags.click_send_btn()
        utils.getscreenshot('/2.Envelope_sent_successfully.png')
        utils.execute_script_with_banner("Verifying receiver receives Document")
        upload.navigateToEnvelope(constants.envelope_file_docx, True)
        upload.verifyRecipientActionInDocumentDetailPage(constants.signer2_name, constants.recipient_status)
        envelope_id_text = download.getting_envelope_id()
        envelope_id_text = envelope_id_text.upper()
        envelope_id_text2 = envelope_id_text.replace("-", "")
        Test_ReceiverReceivesEnvelope.envelope_id = envelope_id_text2
        print("Envelope_id from Test method = ", envelope_id_text2)
        utils.execute_script_with_banner("Logout as sender after sending document")
        utils.logout()
        driver.get(constants.baseUrl)
        utils.execute_script_with_banner("Login to DocuSign again, this time using the signer1 credentials", False)
        login.login_page(constants.signer1_email, constants.signer1_password)
        home.validate_home_page()
        utils.execute_script_with_banner("Clicking on manage tab to select the required Document")
        upload.navigateToEnvelope(constants.envelope_file_docx)
        utils.execute_script_with_banner("Clicking on sign button to complete the process")
        upload.clickPrimarySignButton()
        utils.execute_script_with_banner("Completing Authentication process before signer sign the document")
        login.login_page(constants.signer1_email, constants.signer1_password)
        approve.clickContinueBtnForSigning()
        utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
        approve.clickSecondarySignButton(constants.index_one)
        utils.execute_script_with_banner("Selecting the I approve this document option to approve the document")
        approve.e_sign_reason()
        approve.click_continue_btn()
        approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
        utils.execute_script_with_banner("Clicking on Finish Button to complete the signature")
        approve.click_finish_btn()
        utils.execute_script_with_banner("Logout as Signer1 after completing the signature")
        utils.logout()

    def test_verify_receiver_receives_copy(self, request):
        driver = request.cls.driver
        outlook = Outlook_Page(driver)
        download = Download_Page(driver)
        utils = Util_Test(driver)
        driver.get(constants.outlook_url)
        time.sleep(5)
        utils.execute_script_with_banner("Login to outlook as a signer2")
        outlook.loginToOutlook(constants.signer2_email, constants.signer2_password)
        # outlook.clickOtherFieldTab()
        utils.execute_script_with_banner("Selecting the mail from sender")
        outlook.clickRecentEmail(constants.recent_mail_completed_envelope)
        download.delete_existing_doc(constants.downloaded_summary_file)
        utils.execute_script_with_banner("Downloading the summary report and verifying the envelope id")
        outlook.download_Envelope_summary_pdf()
        utils.validate_pdf_data(
            filecontents=[constants.downloaded_summary_file, Test_ReceiverReceivesEnvelope.envelope_id],
            first_page=True)
