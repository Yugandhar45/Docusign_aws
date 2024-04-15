# from pages.outlookPage import Outlook_Page
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from pages.uploadPage import Upload_Page
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.downloads_page import Download_Page
# from pages.approveDocument import Approve_Envelope
# from testData import constants as constants
# import pytest
# from utilities.utils import Util_Test
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_ReceiverReceivesEnvelope:
#     envelope_id = ''
#
#     def testReceiverReceivesEnvelope(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         download = Download_Page(driver)
#         approve = Approve_Envelope(driver)
#         utils = Util_Test(driver)
#         signTags = Add_Sign_Tags(driver)
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner("Started the Execution for verify receiver receives envelop")
#         utils.execute_script_with_banner(
#             "Entering the valid credentials (username and password) to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         # Upload docx envelope file
#         home.click_start_button()
#         home.send_envelope()
#         utils.execute_script_with_banner("Uploading the Document as a sender")
#         upload.upload_envelope_documents(constants.envelope1_docx, False)
#         upload.clickSetSigningOrderCheckbox()
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
#         upload.SelectRecipientAction()
#         utils.getscreenshot('/1.Signer1_and_Signer2_Action-types.png')
#         upload.click_next_btn()
#         signTags.addSignatureTag(350)
#         signTags.click_send_btn()
#         utils.getscreenshot('/2.Envelope_sent_successfully.png')
#         utils.execute_script_with_banner("Verify whether the Receiver receives a Envelope")
#         upload.navigateToEnvelope(constants.envelope_file_docx, True)
#         upload.verifyRecipientActionInDocumentDetailPage(constants.signer2_name, constants.recipient_status)
#         envelope_id_text = download.getting_envelope_id()
#         envelope_id_text = envelope_id_text.upper()
#         envelope_id_text2 = envelope_id_text.replace("-", "")
#         Test_ReceiverReceivesEnvelope.envelope_id = envelope_id_text2
#         print("Envelope_id from Test method = ", envelope_id_text2)
#         utils.logout()
#         driver.get(constants.baseUrl)
#         utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         utils.execute_script_with_banner("Selecting the assign task Document")
#         home.validate_home_page()
#         upload.navigateToEnvelope(constants.envelope_file_docx)
#         upload.clickPrimarySignButton()
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         approve.clickContinueBtnForSigning()
#         utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#         approve.clickSecondarySignButton(constants.index_one)
#         approve.e_sign_reason()
#         approve.click_continue_btn()
#         approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
#         approve.click_finish_btn()
#         utils.logout()
#
#     def test_verify_receiver_receives_copy(self, request):
#         driver = request.cls.driver
#         outlook = Outlook_Page(driver)
#         download = Download_Page(driver)
#         utils = Util_Test(driver)
#         driver.get(constants.outlook_url)
#         outlook.loginToOutlook(constants.signer2_email, constants.signer2_password)
#         outlook.clickOtherFieldTab()
#         outlook.clickRecentEmail(constants.recent_mail_completed_envelope)
#         download.delete_existing_doc(constants.downloaded_summary_file)
#         outlook.download_Envelope_summary_pdf()
#         Util_Test.validate_pdf_data(
#             filecontents=[constants.downloaded_summary_file, Test_ReceiverReceivesEnvelope.envelope_id],
#             first_page=True)
