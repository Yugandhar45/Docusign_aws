import os
import time
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.approveDocument import Approve_Envelope
from utilities.utils import Util_Test
import pytest
from pages.downloads_page import Download_Page
from pages.uploadPage import Upload_Page


@pytest.mark.usefixtures("test_setup")
class Test_Verify_Comment_Field:
    def test_verify_comment_field(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        utils = Util_Test(driver)
        sign = Add_Sign_Tags(driver)
        approve = Approve_Envelope(driver)
        download = Download_Page(driver)
        utils.execute_script_with_banner("Started the Execution for verifying the comment field")
        utils.create_directory(request.node.name)
        logger = Util_Test.initialize_logger('Verify Comment field')
        try:
            utils.execute_script_with_banner(
                "Entering the valid credentials (username and password) to log in as the sender")
            Util_Test.write_custom_logs(logger, "Verify comment field script execution - Started")
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            utils.execute_script_with_banner("Home page is Displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page")
            utils.execute_script_with_banner("Uploading the Document as a sender")
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on start to send the envelope")
            home.send_envelope()
            upload.upload_envelope_documents(constants.testEnvelope_VerifyComment, False)
            Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
            utils.execute_script_with_banner("Adding recipients and other details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient details.")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            utils.execute_script_with_banner("Adding Signature Tag and comment tag as a sender")
            sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient")
            sign.add_comment_field()
            Util_Test.write_custom_logs(logger, "Dragged and dropped the comment field for recipient")
            utils.getscreenshot('/1.signatureTags_with_comment_text_box.png')
            utils.execute_script_with_banner("Sending Document to Signer")
            sign.click_send_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the send button to send the document.")
            utils.execute_script_with_banner("Logout as Sender, After sending Document")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the sender after sending the document.")
            # Login as approver1 and complete e-sign and comment
            driver.get(constants.baseUrl)
            utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page.")
            utils.execute_script_with_banner("Clicking on Manage Tab and Send Button to select respective envelope")
            upload.navigateToEnvelope(constants.envelope_Envelope_VerifyComment)
            Util_Test.write_custom_logs(logger, "Navigated to the document that was sent by the sender.")
            utils.getscreenshot('/2.EnabledSignButtonForEnvelopeSigning.png')
            upload.clickPrimarySignButton()
            Util_Test.write_custom_logs(logger, "Clicked on the primary sign button.")
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the authentication before signing.")
            #approve.clickContinueBtnForSigning()
            Util_Test.write_custom_logs(logger, "Clicked on the continue button")
            utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
            approve.clickSecondarySignButton(constants.index_one)
            Util_Test.write_custom_logs(logger, "Clicked on the Secondary sign button.")
            approve.e_sign_reason()
            Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
            approve.click_continue_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the continue button for signing.")
            approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the final authentication step before signing")
            utils.execute_script_with_banner("without comment unable to finish the process")
            approve.click_finish_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button to complete sign.")
            utils.execute_script_with_banner("required popup is displayed")
            approve.verify_required_message()
            Util_Test.write_custom_logs(logger, "Validated the required label is displayed.")
            utils.getscreenshot('/3.comment_Required.png')
            approve.add_comment()
            Util_Test.write_custom_logs(logger, "Added the comment")
            utils.getscreenshot('/4.signers_comment.png')
            approve.click_finish_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button to complete sign.")
            utils.execute_script_with_banner("Logout as Signer")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the signer.")

            driver.get(constants.baseUrl)
            # Login as Sender and verify signature and comment
            utils.execute_script_with_banner("Login to DocuSign again, this time using the sender credentials", False)
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1 again.")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page.")
            upload.navigateToEnvelope(constants.envelope_Envelope_VerifyComment, True)
            Util_Test.write_custom_logs(logger, "Navigated to the required document.")
            try:
                os.remove(constants.pdf_file_path1)
            except:
                print("downloads folder is empty")

            print("complete")
            utils.execute_script_with_banner("Verifying the signature and comment Fields as a sender ")
            download.combine_download()
            Util_Test.write_custom_logs(logger, "Downloaded the document.")
            Util_Test.validate_pdf_data(filecontents=[constants.pdf_file_path1, constants.comment_field], first_page=True)
            Util_Test.write_custom_logs(logger, "Validated the comment message")
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()

        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()
            pytest.fail()


