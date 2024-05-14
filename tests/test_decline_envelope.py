import time
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.approveDocument import Approve_Envelope
from utilities.utils import Util_Test
from pages.outlookPage import Outlook_Page
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_DeclineEnvelope:
    def test_declineEnvelope(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        sign = Add_Sign_Tags(driver)
        signing = Approve_Envelope(driver)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Started the Execution for decline envelop")
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        # Upload envelope file and add signature fields
        home.validate_home_page()
        utils.execute_script_with_banner("Home page is Displayed")
        home.click_start_button()
        utils.execute_script_with_banner("Clicking on start button to send Envelope")
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        upload.upload_envelope_documents(constants.testEnvelope_decline, False)
        upload.clickSetSigningOrderCheckbox()
        utils.execute_script_with_banner("Adding recipient 1 and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Adding recipient 2 and other details:")
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
        sign.addSignatureTag(350)
        utils.getscreenshot('/1.signature_tag1.png')
        utils.execute_script_with_banner("Selecting Recipient 2 from the dropdown")
        sign.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
        sign.addSignatureTag(650)
        utils.getscreenshot('/2.signature_tag2.png')
        sign.click_send_btn()
        utils.execute_script_with_banner("Sending Document to Signer")
        utils.execute_script_with_banner("Logout as Sender, After sending Document to signer")
        utils.logout()
        # Login as approver_1 and decline to sign
        driver.get(constants.baseUrl)
        time.sleep(3)
        utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
        login.login_page(constants.signer1_email, constants.signer1_password)
        home.validate_home_page()
        utils.execute_script_with_banner(
            "Navigating to the manage tab and selecting the respective document which was sent by the sender")
        upload.navigateToEnvelope(constants.envelope_decline_test)
        upload.clickPrimarySignButton()
        utils.execute_script_with_banner("Completing Authentication process before signer sign the document")
        login.login_page(constants.signer1_email, constants.signer1_password)
        utils.execute_script_with_banner("Signer decline the Envelop without adding signature")
        signing.decline_envelope()
        utils.execute_script_with_banner("Giving the reason for declining the Document")
        signing.validate_doc_status(constants.decline_status)
        utils.getscreenshot('/3.Decline_Envelope.png')

    def Atest_verify_decline_notification(self, request):
        driver = request.cls.driver
        driver.get(constants.outlook_url)
        utils = Util_Test(driver)
        outlook = Outlook_Page(driver)
        outlook.loginToOutlook(constants.sender_email, constants.sender_password_outlook)
        utils.execute_script_with_banner("login to out look and Selecting the Declined mail")
        outlook.clickRecentEmail(constants.recent_mail_decline_envelop)
        utils.execute_script_with_banner("Verifying the Declined Text")
        outlook.validateDeclineReason(constants.decline_reason)
        utils.getscreenshot('/4.Envelope_declined_notification_to_sender.png')

