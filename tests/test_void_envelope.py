import time
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.approveDocument import Approve_Envelope
from pages.outlookPage import Outlook_Page
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Voiding_Envelope:
    Generated_text = None  # Global variable to store the generated text

    def test_void_envelope(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        sign_tag = Add_Sign_Tags(driver)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Started the Execution for void envelop")
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        utils.execute_script_with_banner("Home Page is Displayed")
        home.click_start_button()
        utils.execute_script_with_banner("Clicking on start button to send Envelope")
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        upload.upload_envelope_documents(constants.testEnvelope_void, False)
        utils.execute_script_with_banner("Adding recipient-1 and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Adding recipient-2 and other details:")
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
        utils.execute_script_with_banner("Clicking on Next Button")
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
        sign_tag.addSignatureTag(350)
        utils.execute_script_with_banner("Selecting Recipient 2 from the drop-down")
        sign_tag.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
        sign_tag.addSignatureTag(600)
        utils.getscreenshot('/1.signature_Tags.png')
        utils.execute_script_with_banner("Sending Document to Signer")
        sign_tag.click_send_btn()
        # Void envelope as Signer
        approve = Approve_Envelope(driver)
        utils.execute_script_with_banner("Clicking on manage tab to select the requried document")
        upload.navigateToEnvelope(constants.envelope_void_test, True)
        approve.validateButtonsInDocumentDetailPage()
        utils.execute_script_with_banner("Clicking on more buttton to void the document")
        approve.click_more_btn()
        utils.execute_script_with_banner("Entering the reason for voiding the document")
        approve.validateOptionsUnderMoreButton()
        approve.voiding_envelope()
        utils.execute_script_with_banner("Clicking on the manage tab and selecting the document")
        upload.navigateToEnvelope(constants.envelope_void_test, True)
        utils.execute_script_with_banner("The status of the document is voided")
        approve.validate_doc_status(constants.void_status)
        utils.getscreenshot('/2.Voided_Envelope.png')
        utils.execute_script_with_banner("Logout as Signer1 after completing the Process")
        utils.logout()

    def test_verify_void_notification(self, request):
        driver = request.cls.driver
        outlook = Outlook_Page(driver)
        utils = Util_Test(driver)
        driver.get(constants.outlook_url)
        time.sleep(5)
        utils.execute_script_with_banner("Login to outlook as a signer1")
        outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
        # outlook.clickOtherFieldTab()
        utils.execute_script_with_banner("Selecting the void mail")
        outlook.clickRecentEmail(constants.recent_mail_void_envelope)
        utils.execute_script_with_banner("Verifying the voided text")
        outlook.validateVoidReason(constants.void_reason)
        utils.getscreenshot('/3.Envelope_Voided_notification_to_signer.png')
