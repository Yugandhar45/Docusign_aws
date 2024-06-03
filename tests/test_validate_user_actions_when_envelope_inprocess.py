import time

from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from pages.addSignTagPage import Add_Sign_Tags
from testData import constants as constants
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Validate_EnvelopeRouting:

    def test_validate_user_action(self, request):
        driver = request.cls.driver

        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        utils = Util_Test(driver)
        sign = Add_Sign_Tags(driver)
        utils.create_directory(request.node.name)
        logger = Util_Test.initialize_logger('Validate user actions when envelop inprocess.')
        try:
            utils.execute_script_with_banner("Started the Execution for Validating user actions when envelop in process")
            utils.execute_script_with_banner(
                "Entering the valid credentials (username and password) to log in as the sender")
            # login to Docusign
            driver.get(constants.baseUrl)
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            # Upload docx envelope file
            utils.execute_script_with_banner("Home page is Displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page")
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on the start button to send the envelope")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the first document")
            upload.upload_envelope_documents(constants.test_envelope3)
            Util_Test.write_custom_logs(logger, "Uploaded the document-1 as a sender")
            utils.execute_script_with_banner("Uploading the second document")
            upload.upload_envelope_documents(constants.test_envelope4)
            Util_Test.write_custom_logs(logger, "Uploaded the document-2 as a sender")
            utils.execute_script_with_banner("Selecting Signing Order")
            upload.clickSetSigningOrderCheckbox()
            Util_Test.write_custom_logs(logger, "Clicked on the set signing order checkbox")
            utils.execute_script_with_banner("Adding recipient-1 and other details: as signer3")
            upload.addRecipient(constants.signer3_name, constants.signer3_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            utils.execute_script_with_banner("Adding recipient-2 and other details: as signer2")
            upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient 2 details.")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            utils.execute_script_with_banner("Adding Signature Tag on document 1  for Recipient-1")
            sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.execute_script_with_banner("Selecting Recipient-2 from the dropdown to add sign tag")
            sign.select_signer(constants.index_two)
            Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
            utils.execute_script_with_banner("Adding Signature Tag on document2 for Recipient-2")
            sign.addSignatureTag(650)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2")
            sign.scroll_to_next_envelope()
            Util_Test.write_custom_logs(logger, "Scrolled down to the next envelop")
            utils.execute_script_with_banner("Adding Signature Tag and as a sender for Recipient-2")
            sign.addSignatureTag(650)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2")
            utils.execute_script_with_banner("Selecting Recipient-1 from the dropdown")
            sign.select_signer(constants.index_one)
            Util_Test.write_custom_logs(logger, "Selected the Recipient1 from the drop down")
            utils.execute_script_with_banner("Adding Signature Tag and as a sender for Recipient-1")
            sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            sign.click_send_btn()
            Util_Test.write_custom_logs(logger, "clicked on the send button")
            utils.execute_script_with_banner("Clicking on Manage Tab and Sent Button to select respective envelope")
            upload.navigateToEnvelope(constants.envelope_3_and_4, True)
            Util_Test.write_custom_logs(logger, "Navigated to the document")
            utils.execute_script_with_banner("Correcting details for first time")
            # First time Envelope  correction
            upload.correctingDocumentDetails()
            Util_Test.write_custom_logs(logger, "Clicked on the correct button")
            upload.verifyEnvelopeCorrectionStatus()
            Util_Test.write_custom_logs(logger, "Validated that the envelop status is in correction state")
            # Delete the existing recipient and adding the new recipient
            utils.execute_script_with_banner("Delete recipient-1 which is signer 3 and add recipient-2 which is signer 1")
            upload.scrollToRecipients()
            Util_Test.write_custom_logs(logger, "Scrolled down to the recipients")
            upload.delete_recipient()
            Util_Test.write_custom_logs(logger, "Delete the recipient")
            utils.execute_script_with_banner("Adding Recipient-1")
            upload.addRecipient(constants.signer1_name, constants.signer1_email,constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient")
            utils.getscreenshot("/2.Adding_New_Recipient.png")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            # selecting the signer and place the signature field
            utils.execute_script_with_banner("Selecting Recipient-2 from the dropdown to add sign tag")
            sign.select_signer(constants.index_two)
            Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
            utils.execute_script_with_banner("Adding Signature Tag and comment tag as a sender for Recipient-2")
            sign.addSignatureTag(350)
            utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
            sign.scroll_to_next_envelope()
            Util_Test.write_custom_logs(logger, "Scrolled down to the next envelop")
            utils.execute_script_with_banner("Adding Signature Tag for Recipient-2 on document 2")
            sign.addSignatureTag(350)
            utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
            utils.execute_script_with_banner("first time envelope correction successful")
            sign.clickCorrectToResendDocument()
            Util_Test.write_custom_logs(logger, "Clicked on the correct to resend the document button")
            upload.validate_toast_msg(constants.success_msg_on_envelope_correction)
            Util_Test.write_custom_logs(logger, "Validated the success message")
            utils.execute_script_with_banner("selecting the respective envelope")
            upload.navigateToEnvelope(constants.envelope_3_and_4, True)
            Util_Test.write_custom_logs(logger, "Navigated to the document")
            utils.execute_script_with_banner("second time Envelope correction initiated")
            upload.correctingDocumentDetails()
            Util_Test.write_custom_logs(logger, "")
            upload.verifyEnvelopeCorrectionStatus()
            Util_Test.write_custom_logs(logger, "")
            # In below method we are verifying and updating the Recipient action
            utils.execute_script_with_banner("Updating Recipient-1 action to received as a carbon copy")
            upload.updateRecipientAction()
            Util_Test.write_custom_logs(logger, "Updated the Recipient Action")
            utils.execute_script_with_banner("Replacing the document with new document")
            # In below method we are verifying the more options and also replacing the envelope
            upload.replace_document(constants.test_envelope3_1)
            Util_Test.write_custom_logs(logger, "Replace the document with new one")
            utils.execute_script_with_banner("Uploading the New Document")
            upload.upload_envelope_documents(constants.test_envelope5)
            Util_Test.write_custom_logs(logger, "Uploaded the new document")
            utils.getscreenshot("/6.uploaded_new_Document.png")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            sign.scroll_to_next_envelope()
            Util_Test.write_custom_logs(logger, "Scrolled down to the next envelop")
            sign.scroll_to_next_envelope()
            utils.execute_script_with_banner("Adding Signature Tag for recepient 2 on a new document")
            sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            sign.clickCorrectToResendDocument()
            Util_Test.write_custom_logs(logger, "Clicked on the resend button to send the document")
            upload.validate_toast_msg(constants.success_msg_on_envelope_correction)
            Util_Test.write_custom_logs(logger, "Validated the success message")
            utils.execute_script_with_banner("Logout as a sender after completing the Process")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Log out as sender")
        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            pytest.fail()
