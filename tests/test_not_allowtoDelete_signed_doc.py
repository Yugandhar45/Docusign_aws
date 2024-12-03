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
# class Test_Verify_SignedDoc_NoDeletionOrReplacement:
#     def test_NoDeletionOrReplacement_on_SignedDoc(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Started the execution for Not Allowed to delete signed document")
#         utils.create_directory(request.node.name)
#         logger = Util_Test.initialize_logger('Not allow to delete signed document')
#         Util_Test.write_custom_logs(logger, "not allow to delete sign document script execution - Started")
#         try:
#             utils.execute_script_with_banner("Entering the valid credentials to log in as the sender")
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
#             # Upload envelope file
#             utils.execute_script_with_banner("Home page is Displayed")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page")
#             home.click_start_button()
#             utils.execute_script_with_banner("Clicking on start button to send an envelope")
#             home.send_envelope()
#             utils.execute_script_with_banner("Uploading the Document as a sender")
#             upload.upload_envelope_documents(constants.testEnvelope_delete, False)
#             Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
#             utils.execute_script_with_banner("Adding recipient 1 and other details:")
#             upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#             Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
#             utils.execute_script_with_banner("Adding recipient 2 and other details:")
#             upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
#             Util_Test.write_custom_logs(logger, "Added the recipient 2 details.")
#             upload.click_next_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the next button")
#             sign = Add_Sign_Tags(driver)
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#             sign.addSignatureTag(350)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
#             utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
#             sign.select_signer(constants.index_two)
#             Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
#             sign.addSignatureTag(650)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2 ")
#             utils.execute_script_with_banner("Sending Document to Signer")
#             sign.click_send_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the send button to send the document.")
#             utils.execute_script_with_banner("Logout as Sender, After sending Document")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Logged out from the sender after sending the document.")
#
#
#             # Login as approver1 and complete e-sign
#             time.sleep(2)
#             driver.get(constants.baseUrl)
#             utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#             login.login_page(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page.")
#             utils.execute_script_with_banner(
#                 "Navigating to the manage tab and selecting the respective document which was sent by the sender")
#             upload.navigateToEnvelope(constants.envelope_delete_test)
#             Util_Test.write_custom_logs(logger, "Navigated to the document that was sent by the sender.")
#             upload.clickPrimarySignButton()
#             Util_Test.write_custom_logs(logger, "Clicked on the sign button.")
#             utils.execute_script_with_banner("Completing the Authentication Process after selecting Document")
#             login.login_page(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Completed the authentication before signing.")
#             sign = Approve_Envelope(driver)
#             #sign.clickContinueBtnForSigning()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for signing and validated that the button was displayed.")
#             sign.clickSecondarySignButton(constants.index_one)
#             Util_Test.write_custom_logs(logger, "Clicked on the signing tag button.")
#             sign.verifyReasonForSigningPopUpOptions()
#             Util_Test.write_custom_logs(logger, "Validated the options under reason for signing.")
#             utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#             sign.e_sign_reason(True)
#             Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
#             sign.click_continue_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for completing the sign.")
#             sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Completed the final authentication step before signing.")
#             utils.execute_script_with_banner("Clicking on Finish Button")
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button.")
#             sign.click_finish_btn()
#             utils.getscreenshot('/1.Recipient_1_signed_on_document.png')
#             utils.execute_script_with_banner("Logout as Signer")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Logged out from the signer 1 after completing the process.")
#             # Login as sender and verify whether document can be deleted
#             time.sleep(2)
#             driver.get(constants.baseUrl)
#             utils.execute_script_with_banner("Login to DocuSign again, this time using the sender credentials", False)
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page.")
#             upload.navigateToEnvelope(constants.envelope_delete_test, True)
#             Util_Test.write_custom_logs(logger, "Navigated to the document that was sent by the sender.")
#             utils.execute_script_with_banner("Clicking on Correct Button")
#             upload.verifyButtonsForSenderInDocumentDetailPage()
#             Util_Test.write_custom_logs(logger, "Validated the options under document details page.")
#             utils.execute_script_with_banner("Clicking on more option and verifying whether the delete option is Disabled")
#             upload.correctingDocumentDetails()
#             Util_Test.write_custom_logs(logger, "Clicked on the correct button.")
#             utils.execute_script_with_banner("Selected the document and verify that the sign document is not allowed to "
#                                              "delete")
#             upload.restrict_document_del_and_replace()
#             Util_Test.write_custom_logs(logger, "Validated the options i.e Replace, Delete and lock buttons are disable.")
#             utils.getscreenshot("/2.Delete_and_Replace_button_disabled.png")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()
#
#
#
