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
        utils.execute_script_with_banner("Started the Execution for Validating user actions when envelop in process")
        utils.execute_script_with_banner(
            "Entering the valid credentials (username and password) to log in as the sender")
        # login to Docusign
        driver.get(constants.baseUrl)
        login.login_page(constants.sender_email, constants.sender_password)
        # Upload docx envelope file
        utils.execute_script_with_banner("Home page is Displayed")
        home.validate_home_page()
        home.click_start_button()
        utils.execute_script_with_banner("Clicking on the start button to send the envelope")
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the first document")
        upload.upload_envelope_documents(constants.test_envelope3)
        utils.execute_script_with_banner("Uploading the second document")
        upload.upload_envelope_documents(constants.test_envelope4)
        utils.execute_script_with_banner("Selecting Signing Order")
        upload.clickSetSigningOrderCheckbox()
        utils.execute_script_with_banner("Adding recipient-1 and other details: as signer3")
        upload.addRecipient(constants.signer3_name, constants.signer3_email, constants.index_one)
        utils.execute_script_with_banner("Adding recipient-2 and other details: as signer2")
        upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding Signature Tag on document 1  for Recipient-1")
        sign.addSignatureTag(350)
        utils.execute_script_with_banner("Selecting Recipient-2 from the dropdown to add sign tag")
        sign.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag on document2 for Recipient-2")
        sign.addSignatureTag(650)
        sign.scroll_to_next_envelope()
        utils.execute_script_with_banner("Adding Signature Tag and as a sender for Recipient-2")
        sign.addSignatureTag(650)
        utils.execute_script_with_banner("Selecting Recipient-1 from the dropdown")
        sign.select_signer(constants.index_one)
        utils.execute_script_with_banner("Adding Signature Tag and as a sender for Recipient-1")
        sign.addSignatureTag(350)
        utils.getscreenshot('/1.sendButtonWithSignatureTags.png')
        sign.click_send_btn()
        utils.execute_script_with_banner("Clicking on Manage Tab and Sent Button to select respective envelope")
        upload.navigateToEnvelope(constants.envelope_3_and_4, True)
        utils.execute_script_with_banner("Correcting details for first time")
        # First time Envelope  correction
        upload.correctingDocumentDetails()
        upload.verifyEnvelopeCorrectionStatus()
        utils.getscreenshot("/2.first_time_Envelope_correction.png")
        # Delete the existing recipient and adding the new recipient
        utils.execute_script_with_banner("Delete recipient-1 which is signer 3 and add recipient-2 which is signer 1")
        upload.delete_recipient()
        utils.getscreenshot("/3.Delete_Existing_Recipient.png")
        utils.execute_script_with_banner("Adding Recipient-2")
        upload.addRecipient(constants.signer1_name, constants.signer1_email,constants.index_two)
        utils.getscreenshot("/4.Adding_New_Signer.png")
        upload.click_next_btn()
        # selecting the signer and place the signature field
        utils.execute_script_with_banner("Selecting Recipient-2 from the dropdown to add sign tag")
        sign.select_signer(constants.index_two)
        utils.execute_script_with_banner("Adding Signature Tag and comment tag as a sender for Recipient-2")
        sign.addSignatureTag(350)
        sign.scroll_to_next_envelope()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient-2 on document 2")
        sign.addSignatureTag(350)
        utils.execute_script_with_banner("first time envelope correction successful")
        sign.clickCorrectToResendDocument()
        utils.getscreenshot('/5.First_time_successful_correction.png')
        upload.validate_toast_msg(constants.success_msg_on_envelope_correction)
        utils.execute_script_with_banner("selecting the respective envelope")
        upload.navigateToEnvelope(constants.envelope_3_and_4, True)
        utils.execute_script_with_banner("second time Envelope correction initiated")
        upload.correctingDocumentDetails()
        upload.verifyEnvelopeCorrectionStatus()
        utils.getscreenshot("/6.Second_time_Envelope_correction.png")
        # In below method we are verifying and updating the Recipient action
        utils.execute_script_with_banner("Updating Recipient-1 action to received as a carbon copy")
        upload.updateRecipientAction()
        utils.getscreenshot("/7.change_Recipient_Type.png")
        utils.execute_script_with_banner("Replacing the document with new document")
        # In below method we are verifying the more options and also replacing the envelope
        upload.replace_document(constants.test_envelope3_1)
        utils.execute_script_with_banner("Uploading the New Document")
        upload.upload_envelope_documents(constants.test_envelope5)
        upload.click_next_btn()
        sign.scroll_to_next_envelope()
        sign.scroll_to_next_envelope()
        utils.execute_script_with_banner("Adding Signature Tag for recepient 2 on a new document")
        sign.addSignatureTag(350)
        sign.clickCorrectToResendDocument()
        utils.getscreenshot("/8.Corrected_Envelope.png")
        upload.validate_toast_msg(constants.success_msg_on_envelope_correction)
        utils.execute_script_with_banner("Logout as a sender after completing the Process")
        utils.logout()
