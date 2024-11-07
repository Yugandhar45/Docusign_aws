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

logger = Util_Test.initialize_logger('Verify receiver receives envelop')


@pytest.mark.usefixtures("test_setup")
class Test_ReceiverReceivesEnvelope:
    envelope_id = ''

    @pytest.mark.dependency()
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
        try:
            Util_Test.write_custom_logs(logger, "Verify receiver receives envelop script execution - Started")
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")

            # Upload docx envelope file
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on the start button to send document")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the Document as a sender")
            upload.upload_envelope_documents(constants.envelope1_docx, False)
            Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
            upload.clickSetSigningOrderCheckbox()
            Util_Test.write_custom_logs(logger, "Selected the set signing order checkbox")
            utils.execute_script_with_banner("Adding recipient-1 and other details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            utils.getscreenshot('/1.Recipient_1_with_need_Sign-action.png')
            utils.execute_script_with_banner("Adding recipient-2 and other details:")
            upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient 2 details.")
            utils.execute_script_with_banner("Selecting \"receives a copy option\" for signer2")
            upload.SelectRecipientAction()
            Util_Test.write_custom_logs(logger,
                                        "Navigated to Recipient action and selected a receive a copy for recipient 2.")
            utils.getscreenshot('/2.Recipient_2_with_Recieves_a_Copy-action.png')
            utils.execute_script_with_banner("clicking on Next Button to send a document to signer1")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            utils.execute_script_with_banner("Adding signature tag for signer1")
            signTags.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.execute_script_with_banner("Sending Document to Signers")
            signTags.click_send_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the send button to send the document.")
            utils.execute_script_with_banner("Verifying receiver receives Document")
            upload.navigateToEnvelope(constants.envelope_file_docx, True)
            Util_Test.write_custom_logs(logger, "Navigated to the document.")
            upload.verifyRecipientActionInDocumentDetailPage(constants.signer2_name, constants.recipient_status)
            envelope_id_text = download.getting_envelope_id()
            envelope_id_text = envelope_id_text.upper()
            envelope_id_text2 = envelope_id_text.replace("-", "")
            Test_ReceiverReceivesEnvelope.envelope_id = envelope_id_text2
            print("Envelope_id from Test method = ", envelope_id_text2)
            utils.execute_script_with_banner("Logout as sender after sending document")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the signer.")

            driver.get(constants.baseUrl)
            utils.execute_script_with_banner("Login to DocuSign again, this time using the signer1 credentials", False)
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page.")
            utils.execute_script_with_banner("Clicking on manage tab to select the required Document")
            upload.navigateToEnvelope(constants.envelope_file_docx)
            Util_Test.write_custom_logs(logger, "Navigated to the document that was sent by the sender.")
            utils.execute_script_with_banner("Clicking on sign button to complete the process")
            upload.clickPrimarySignButton()
            Util_Test.write_custom_logs(logger, "Clicked on the Primary sign button.")
            utils.execute_script_with_banner("Completing Authentication process before signer sign the document")
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the authentication before signing.")
            #approve.clickContinueBtnForSigning()
            Util_Test.write_custom_logs(logger,
                                        "Clicked on the 'Continue' button for signing and validated that the button was displayed.")
            utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
            approve.clickSecondarySignButton(constants.index_one)
            Util_Test.write_custom_logs(logger, "Clicked on the signing tag button.")
            utils.execute_script_with_banner("Selecting the I approve this document option to approve the document")
            approve.e_sign_reason()
            Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
            approve.click_continue_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for completing the sign.")
            approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the final authentication step before signing.")
            utils.execute_script_with_banner("Clicking on Finish Button to complete the signature")
            approve.click_finish_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button.")
            utils.execute_script_with_banner("Logout as Signer1 after completing the signature")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the signer 2 after completing the process.")

        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            pytest.fail()

    @pytest.mark.dependency(depends=["Test_ReceiverReceivesEnvelope::testReceiverReceivesEnvelope"])
    def test_verify_receiver_receives_copy(self, request):
        driver = request.cls.driver
        outlook = Outlook_Page(driver)
        download = Download_Page(driver)
        utils = Util_Test(driver)
        try:
            driver.get(constants.outlook_url)
            Util_Test.write_custom_logs(logger, "Navigated to the Outlook URL.")
            time.sleep(5)
            utils.execute_script_with_banner("Login to outlook as a signer2")
            outlook.loginToOutlook(constants.signer2_email, constants.signer2_password)
            Util_Test.write_custom_logs(logger, "Logged in to the Outlook account successfully")
            # outlook.clickOtherFieldTab()
            utils.execute_script_with_banner("Selecting the mail from sender")
            outlook.clickRecentEmail(constants.recent_mail_completed_envelope)
            Util_Test.write_custom_logs(logger, "Navigated to the recent mail and Found and opened the desired mail.")
            Download_Page.delete_existing_doc(constants.downloaded_summary_file)
            utils.execute_script_with_banner("Downloading the summary report and verifying the envelope id")
            outlook.download_Envelope_summary_pdf()
            Util_Test.write_custom_logs(logger, "Downloaded the envelop summary document.")
            utils.validate_pdf_data(
                filecontents=[constants.downloaded_summary_file, Test_ReceiverReceivesEnvelope.envelope_id],
                first_page=True)
            Util_Test.write_custom_logs(logger, "Validated that the signer 2 received a copy")
        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            pytest.fail()

    def test_ReceiverReceivesEnvelopeCopy(self, request):
        Util_Test.add_test_name_to_doc(request.node.name)
        Util_Test.add_screenshots_to_doc()
