# import time
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from pages.uploadPage import Upload_Page
# from testData import constants as constants
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.approveDocument import Approve_Envelope
# from utilities.utils import Util_Test
# import pytest
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_NoDel_SignedDoc:
#     def test_NoDel_SignedDoc(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Started the execution for Not Allowed to delete signed document")
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner("Entering the valid credentials to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         # Upload envelope file
#         utils.execute_script_with_banner("Home page is Displayed")
#         home.validate_home_page()
#
#         home.click_start_button()
#         utils.execute_script_with_banner("Clicking on start button to send an envelope")
#         home.send_envelope()
#         utils.execute_script_with_banner("Uploading the Document as a sender")
#         upload.upload_envelope_documents(constants.testEnvelope_delete, False)
#         utils.execute_script_with_banner("Adding recipient 1 and other details:")
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         utils.execute_script_with_banner("Adding recipient 2 and other details:")
#         upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
#         utils.getscreenshot('/1.Assigned_recipients.png')
#         upload.click_next_btn()
#         sign = Add_Sign_Tags(driver)
#         utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#         sign.addSignatureTag(350)
#         utils.getscreenshot('/2.signature_tag1.png')
#         utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
#         sign.select_signer(constants.index_two)
#         utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
#         sign.addSignatureTag(650)
#         utils.getscreenshot('/3.signature_tag2.png')
#         utils.execute_script_with_banner("Sending Document to Signer")
#         sign.click_send_btn()
#         utils.execute_script_with_banner("Logout as Sender, After sending Document")
#         utils.logout()
#
#         # Login as approver1 and complete e-sign
#         time.sleep(2)
#         driver.get(constants.baseUrl)
#         utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         home.validate_home_page()
#         utils.execute_script_with_banner(
#             "Navigating to the manage tab and selecting the respective document which was sent by the sender")
#         upload.navigateToEnvelope(constants.envelope_delete_test)
#         upload.clickPrimarySignButton()
#         utils.execute_script_with_banner("Completing the Authentication Process after selecting Document")
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         sign = Approve_Envelope(driver)
#         sign.clickContinueBtnForSigning()
#         sign.clickSecondarySignButton(constants.index_one)
#         sign.verifyReasonForSigningPopUpOptions()
#         utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#         sign.e_sign_reason(True)
#         sign.click_continue_btn()
#         sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
#         utils.execute_script_with_banner("Clicking on Finish Button")
#         sign.click_finish_btn()
#         utils.execute_script_with_banner("Logout as Signer")
#         utils.logout()
#         # Login as sender and verify whether document can be deleted
#         time.sleep(2)
#         driver.get(constants.baseUrl)
#         utils.execute_script_with_banner("Login to DocuSign again, this time using the sender credentials", False)
#         login.login_page(constants.sender_email, constants.sender_password)
#         home.validate_home_page()
#         upload.navigateToEnvelope(constants.envelope_delete_test, True)
#         utils.execute_script_with_banner("Clicking on Correct Button")
#         upload.verifyButtonsForSenderInDocumentDetailPage()
#         utils.execute_script_with_banner("Clicking on more option and verifying whether the delete option is Disabled")
#         upload.correctingDocumentDetails()
#         #upload.envelope_correction(constants.envelope_delete_test)
#         upload.restrict_document_del_and_replace()
#         utils.getscreenshot("/4.Delete_and_Replace_button_disabled.png")
#         utils.execute_script_with_banner("Selected the document and verify that the sign document is not allowed to "
#                                          "delete")
#
#
#
