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

logger = Util_Test.initialize_logger('void envelop')


@pytest.mark.usefixtures("test_setup")
class Test_Voiding_Envelope:
    @pytest.mark.dependency()
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
        Util_Test.write_custom_logs(logger, "Void envelop script execution - Started")
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        try:
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            utils.execute_script_with_banner("Home Page is Displayed")
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on start button to send Envelope")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the Document as a sender")
            upload.upload_envelope_documents(constants.testEnvelope_void, False)
            Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
            utils.execute_script_with_banner("Adding recipient-1 and other details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            utils.execute_script_with_banner("Adding recipient-2 and other details:")
            upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient 2 details.")
            utils.execute_script_with_banner("Clicking on Next Button")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
            sign_tag.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.execute_script_with_banner("Selecting Recipient 2 from the drop-down")
            sign_tag.select_signer(constants.index_two)
            Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
            utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
            sign_tag.addSignatureTag(600)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2")
            utils.execute_script_with_banner("Sending Document to Signer")
            sign_tag.click_send_btn()
            Util_Test.write_custom_logs(logger, "clicked on the send button")
            # Void envelope as Signer
            approve = Approve_Envelope(driver)
            utils.execute_script_with_banner("Clicking on manage tab to select the requried document")
            upload.navigateToEnvelope(constants.envelope_void_test, True)
            Util_Test.write_custom_logs(logger, "Navigated to the document to void it.")
            approve.validateButtonsInDocumentDetailPage()
            Util_Test.write_custom_logs(logger,
                                        "Validated the buttons i.e correct, move, resend and more options are displayed")
            utils.execute_script_with_banner("Clicking on more buttton to void the document")
            approve.click_more_btn()
            Util_Test.write_custom_logs(logger, "Clicked on more button.")
            utils.execute_script_with_banner("Entering the reason for voiding the document")
            approve.validateOptionsUnderMoreButton()
            Util_Test.write_custom_logs(logger, "Validated all the button under more option")
            approve.voiding_envelope()
            Util_Test.write_custom_logs(logger, "Clicked on the void option and given a reason for void")
            utils.execute_script_with_banner("Clicking on the manage tab and selecting the document")
            upload.navigateToEnvelope(constants.envelope_void_test, True)
            Util_Test.write_custom_logs(logger, "Again Navigated to the envelop to check the status")
            utils.execute_script_with_banner("The status of the document is voided")
            approve.validate_doc_status(constants.void_status)
            Util_Test.write_custom_logs(logger, "Validated the envelop status that is in Voided")
            utils.getscreenshot('/2.Voided_Envelope.png')
            utils.execute_script_with_banner("Logout as Signer1 after completing the Process")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the sender")
            Util_Test.write_custom_logs(logger, "Void envelop script execution - Completed")
        except:
            Util_Test.write_custom_logs(logger, f" void_envelope Test case failed")
            pytest.fail()

    @pytest.mark.dependency(depends=["Test_Voiding_Envelope::test_void_envelope"])
    def test_verify_void_notification(self, request):
        driver = request.cls.driver
        outlook = Outlook_Page(driver)
        utils = Util_Test(driver)
        driver.get(constants.outlook_url)
        Util_Test.write_custom_logs(logger, "*****************************************************")
        Util_Test.write_custom_logs(logger, "verify_void_notification Test case execution -- Started")
        Util_Test.write_custom_logs(logger, "Navigated to the Outlook URL.")
        time.sleep(5)
        utils.execute_script_with_banner("Login to outlook as a signer1")
        try:
            outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Signer logged into the Outlook account.")
            # outlook.clickOtherFieldTab()
            utils.execute_script_with_banner("Selecting the void mail")
            outlook.clickRecentEmail(constants.recent_mail_void_envelope)
            Util_Test.write_custom_logs(logger, "Selected the email related to void")
            utils.execute_script_with_banner("Verifying the voided text")
            outlook.validateVoidReason(constants.void_reason)
            Util_Test.write_custom_logs(logger, "Validated the void envelop reason.")
            utils.getscreenshot('/2.Envelope_Voided_notification_to_signer.png')
            Util_Test.write_custom_logs(logger, f"verify_void_notification Execution - Completed")
        except:
            Util_Test.write_custom_logs(logger, f"verify_void_notification Test case failed")
            pytest.fail()

