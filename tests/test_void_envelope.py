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
    def test_void_envelope(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        sign_tag = Add_Sign_Tags(driver)
        utils = Util_Test(driver)
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        # Upload envelope file
        utils.execute_script_with_banner("Launching the Home Page")
        home.click_start_button()
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        upload.upload_envelope_documents(constants.testEnvelope_void, False)
        utils.execute_script_with_banner("Adding first recipients and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Adding second recipients and other details:")
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
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
        upload.navigateToEnvelope(constants.envelope_void_test, True)
        approve.validateButtonsInDocumentDetailPage()
        approve.click_more_btn()
        approve.validateOptionsUnderMoreButton()
        approve.voiding_envelope()
        upload.navigateToEnvelope(constants.envelope_void_test, True)
        approve.validate_doc_status(constants.void_status)
        Util_Test.getscreenshot('/2.Voided_Envelope.png')
        utils.execute_script_with_banner("Logout as Signer after completing the Process")
        utils.logout()

    def test_verify_void_notification(self, request):
        driver = request.cls.driver
        outlook = Outlook_Page(driver)
        driver.get(constants.outlook_url)
        outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
        outlook.clickOtherFieldTab()
        outlook.clickRecentEmail(constants.recent_mail_void_envelope)
        outlook.validateVoidReason(constants.void_reason)
        Util_Test.getscreenshot('/3.Envelope_Voided_notification_to_signer.png')
