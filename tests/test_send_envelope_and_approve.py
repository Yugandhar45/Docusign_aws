# import time
# from pages.outlookPage import Outlook_Page
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from pages.uploadPage import Upload_Page
# from testData import constants as constants
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.approveDocument import Approve_Envelope
# from utilities.utils import Util_Test
# from pages.downloads_page import Download_Page
# import pytest
#
# logger = Util_Test.initialize_logger('Send Envelop and Approve')
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_SendEnvelope_Approve:
#     @pytest.mark.dependency()
#     def test_send_envelope_approve(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         add_sign = Add_Sign_Tags(driver)
#         utils = Util_Test(driver)
#         utils.create_directory(request.node.name)
#         Util_Test.write_custom_logs(logger, "Send envelop and approve script execution - Started")
#         utils.execute_script_with_banner("Entering the valid credentials to log in as the sender")
#         try:
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
#             utils.execute_script_with_banner("Home page is Displayed")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page")
#             home.click_start_button()
#             Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
#             utils.execute_script_with_banner("Clicking on the start button to send the document")
#             home.send_envelope()
#             utils.execute_script_with_banner("Uploading the 2 Documents as a sender")
#             upload.upload_envelope_documents(constants.envelope1_docx, False)
#             Util_Test.write_custom_logs(logger, "Uploaded the document-1 as a sender")
#             upload.upload_envelope_documents(constants.envelope2_pdf, False)
#             utils.getscreenshot('/1.Upload_one_or_more_documents.png')
#             Util_Test.write_custom_logs(logger, "Uploaded the document-2 as a sender")
#             utils.execute_script_with_banner("Adding recepient 1 and other details:")
#             upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#             Util_Test.write_custom_logs(logger, "Adding recipient-1 and other details")
#             utils.execute_script_with_banner("Adding recepient 2 and other details:")
#             upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
#             Util_Test.write_custom_logs(logger, "Adding recipient-2 and other details")
#             utils.execute_script_with_banner("Clicking the next button")
#             upload.click_next_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the next button")
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#             add_sign.addSignatureTag(350)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
#             utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
#             add_sign.select_signer(constants.index_two)
#             Util_Test.write_custom_logs(logger, "Selected the Recipient-2 from drop down")
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
#             add_sign.addSignatureTag(650)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2")
#             utils.execute_script_with_banner("Selecting the second document to add the Sign tags")
#             add_sign.scroll_to_next_envelope()
#             Util_Test.write_custom_logs(logger, "Scrolled down to the next envelop")
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#             add_sign.select_signer(constants.index_one)
#             Util_Test.write_custom_logs(logger, "Selected the Recipient 1 from the drop down")
#             add_sign.addSignatureTag(350)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
#             utils.execute_script_with_banner("Selecting Recipient 2 To add the Signature Tag")
#             add_sign.select_signer(constants.index_two)
#             Util_Test.write_custom_logs(logger, "Selected the Recipient2 from the drop down")
#             utils.execute_script_with_banner("Adding Signature Tag for Recipient 2")
#             add_sign.addSignatureTag(650)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 2")
#             add_sign.click_send_btn()
#             Util_Test.write_custom_logs(logger, "clicked on the send button")
#             # Change signature routing order
#             upload.navigateToEnvelope(constants.select_2envelopes, True)
#             Util_Test.write_custom_logs(logger, "Navigated to the document")
#             upload.verifyButtonsForSenderInDocumentDetailPage()
#             Util_Test.write_custom_logs(logger,
#                                         "Validated the buttons i.e correct, move, resend and more options are displayed")
#             utils.execute_script_with_banner("Clicking on the correct button")
#             upload.correctingDocumentDetails()
#             Util_Test.write_custom_logs(logger, "Clicked on the correct button")
#             # upload.envelope_correction(constants.select_2envelopes)
#             upload.clickSetSigningOrderCheckbox()
#             Util_Test.write_custom_logs(logger, "Clicked on the set signing order checkbox")
#             utils.execute_script_with_banner("Change the signing order of signer1 as 2 and signer2 as 1 to sign the "
#                                              "envelopes")
#             upload.set_routing_order(constants.index_one, constants.index_two)
#             Util_Test.write_custom_logs(logger, "Changed the Routing order")
#             utils.getscreenshot('/2.Assigning_Signing_order.png')
#             upload.click_next_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the next button")
#             add_sign.clickCorrectToResendDocument()
#             Util_Test.write_custom_logs(logger, "Clicked on the correct button to Resend the document")
#             upload.navigateToEnvelope(constants.select_2envelopes, True)
#             Util_Test.write_custom_logs(logger, "Navigated to the envelope")
#             upload.verifyCorrectedRoutedOrder(constants.select_2envelopes)
#             Util_Test.write_custom_logs(logger, "Validated the recipients Routed order")
#             utils.execute_script_with_banner("Logout as Sender, After sending Document")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "The sender is Logged out from the application")
#
#             # Login as approver2 and complete e-sign
#             time.sleep(5)
#             driver.get(constants.baseUrl)
#             approve = Approve_Envelope(driver)
#             utils.execute_script_with_banner("Login as Signer", False)
#             login.login_page(constants.signer2_email, constants.signer2_password)
#             Util_Test.write_custom_logs(logger, "Recipient-2 logged into the application")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page.")
#             utils.execute_script_with_banner("Navigating to the manage tab and selecting the respective document which "
#                                              "was sent by the sender")
#             upload.navigateToEnvelope(constants.select_2envelopes)
#             Util_Test.write_custom_logs(logger, "Navigated to the document")
#             upload.clickPrimarySignButton()
#             Util_Test.write_custom_logs(logger, "Clicked on the Primary sign button")
#             login.login_page(constants.signer2_email, constants.signer2_password)
#             Util_Test.write_custom_logs(logger, "Completed the authentication for signing")
#             #approve.clickContinueBtnForSigning()
#             Util_Test.write_custom_logs(logger, "Validated and Clicked on the 'Continue' button for signing")
#             utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#             approve.clickSecondarySignButton(constants.index_one)
#             Util_Test.write_custom_logs(logger, "Clicked on the signing tag in first document.")
#             approve.e_sign_reason(False, True)
#             Util_Test.write_custom_logs(logger, "Selected signing reason from drop down")
#             approve.click_continue_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for completing the sign")
#             approve.switchToNewTab(constants.signer2_email, constants.signer2_password)
#             Util_Test.write_custom_logs(logger, "Completed the final authentication process and signing.")
#             approve.clickSecondarySignButton(constants.index_two)
#             Util_Test.write_custom_logs(logger, "Clicked on the signing tag in second document")
#             approve.verifyReasonForSigningPopUpOptions()
#             Util_Test.write_custom_logs(logger, "Validated the options under reason for signing.")
#             approve.e_sign_reason()
#             Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
#             approve.switchToNewTab(constants.signer2_email, constants.signer2_password,True)  # updated for capturing the screenshot
#             utils.getscreenshot('/3.3_E_Signature.png')
#             utils.execute_script_with_banner("Clicking on Finish Button")
#             Util_Test.write_custom_logs(logger, "Completed the final authentication process and signing")
#             approve.click_finish_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button.")
#             utils.execute_script_with_banner("Logout as Signer after completing the process")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Recipient-2 is logged out form the application")
#
#             # Login as approver1 and complete e-sign
#             time.sleep(5)
#             driver.get(constants.baseUrl)
#             utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#             login.login_page(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Recipient-1 logged in to the application")
#             home.validate_home_page()
#             utils.execute_script_with_banner("Selecting the assign task Document")
#             upload.navigateToEnvelope(constants.select_2envelopes)
#             Util_Test.write_custom_logs(logger, "Navigated to the document")
#             upload.clickPrimarySignButton()
#             Util_Test.write_custom_logs(logger, "Clicked on the primary Sign button")
#             #approve.clickContinueBtnForSigning()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for signing")
#             utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#             approve.clickSecondarySignButton(constants.index_one)
#             Util_Test.write_custom_logs(logger, "Clicked on the Sign Tag in first document.")
#             approve.e_sign_reason()
#             Util_Test.write_custom_logs(logger, "Provided the Signing reason")
#             utils.execute_script_with_banner("Clicking on the continue button")  # added
#             approve.click_continue_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the continue button")
#             approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Completed the authentication process and signing")
#             approve.clickSecondarySignButton(constants.index_two)
#             Util_Test.write_custom_logs(logger, "Clicked on the Sign Tag in Second document")
#             approve.e_sign_reason()
#             Util_Test.write_custom_logs(logger, "Provided the signing reason")
#             approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Completed the Authentication process and signing")
#             utils.execute_script_with_banner("Clicking on the finish button")  # added
#             approve.click_finish_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the 'Finish' button.")
#             utils.execute_script_with_banner("Logout as Signer1 after completing the process")
#             utils.logout()
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             Util_Test.write_custom_logs(logger, "Recipient-1 logged out from the application")
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()
#
#     @pytest.mark.dependency(depends=["Test_SendEnvelope_Approve::test_send_envelope_approve"])
#     def test_envelope_completion_notification(self, request):
#         driver = request.cls.driver
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Logging to the outlook to check the completed notification")
#         driver.get(constants.outlook_url)
#         Util_Test.write_custom_logs(logger, "Opened the Outlook URL.")
#         outlook = Outlook_Page(driver)
#         utils.create_directory(request.node.name)
#         time.sleep(5)
#         utils.execute_script_with_banner("Entering the sender outlook credentials")
#         try:
#             outlook.loginToOutlook(constants.sender_email, constants.sender_password_outlook)
#             Util_Test.write_custom_logs(logger, "THe sender logged into OutLook")
#             # outlook.clickOtherFieldTab()
#             utils.execute_script_with_banner("Clicking on the recent completed text mail")
#             outlook.clickRecentEmail(constants.recent_mail_completed_envelope)
#             Util_Test.write_custom_logs(logger, "Found and opened the desired mail")
#             utils.execute_script_with_banner("Verifying the completed envelope notification")
#             outlook.verifyCompletedEnvelope()
#             Util_Test.write_custom_logs(logger, "Verified the completed envelope notification")
#             utils.getscreenshot('/4.Envelope_completed_notification.png')
#             Util_Test.write_custom_logs(logger, "Send envelop and approve script execution - Completed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()
#
#     # Combine and download all docs
#     @pytest.mark.dependency(depends=["Test_SendEnvelope_Approve::test_send_envelope_approve"])
#     def test_download_allDocuments(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         utils = Util_Test(driver)
#         utils.create_directory(request.node.name)
#         try:
#             utils.execute_script_with_banner("Entering the username and password to log in as the sender")
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Sender Logged into the application")
#             # Navigate to document for download
#             download = Download_Page(driver)
#             utils.execute_script_with_banner("Navigate to the Document download option")
#             download.navigate_to_document_download(constants.select_2envelopes)
#             Util_Test.write_custom_logs(logger, "Navigated to the Envelope")
#             utils.execute_script_with_banner("Deleting the Existing document from the folder")
#             Download_Page.delete_existing_doc(constants.pdf_file_path)
#             envelope_id_text = download.getting_envelope_id()
#             envelope_id_text = envelope_id_text.upper()
#             #envelope_id_text2 = envelope_id_text.replace("-", "")
#             print("Envelope_id from Test method = ", envelope_id_text)
#             # Combine and download the all PDFs into one
#             utils.execute_script_with_banner("Downloading the Envelopes by combining in one pdf")
#             download.combine_download(True)
#             Util_Test.write_custom_logs(logger, "Downloaded completed document with completion certificate")
#             file_contents = [constants.pdf_file_path, envelope_id_text, constants.coc_text]
#             utils.execute_script_with_banner("Validating and Verifying the Downloaded document")
#             Util_Test.validate_pdf_data(file_contents)
#             Util_Test.write_custom_logs(logger, "Validated the pdf data")
#             utils.execute_script_with_banner("Logout as Sender after completing the process")
#             utils.logout()
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             Util_Test.write_custom_logs(logger, "The sender Logged out from the application")
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()