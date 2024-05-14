# import os
# import time
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from testData import constants as constants
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.approveDocument import Approve_Envelope
# from utilities.utils import Util_Test
# import pytest
# from pages.downloads_page import Download_Page
# from pages.uploadPage import Upload_Page
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_Verify_Comment_Field:
#     def test_verify_comment_field(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         utils = Util_Test(driver)
#         sign = Add_Sign_Tags(driver)
#         approve = Approve_Envelope(driver)
#         download = Download_Page(driver)
#         utils.execute_script_with_banner("Started the Execution for verifying the comment field")
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner(
#             "Entering the valid credentials (username and password) to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         utils.execute_script_with_banner("Home page is Displayed")
#         home.validate_home_page()
#         utils.execute_script_with_banner("Uploading the Document as a sender")
#         home.click_start_button()
#         utils.execute_script_with_banner("Clicking on start to send the envelope")
#         home.send_envelope()
#         upload.upload_envelope_documents(constants.testEnvelope_VerifyComment, False)
#         utils.execute_script_with_banner("Adding recipients and other details:")
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         upload.click_next_btn()
#         utils.execute_script_with_banner("Adding Signature Tag and comment tag as a sender")
#         sign.addSignatureTag(350)
#         sign.add_comment_field()
#         utils.getscreenshot('/1.signatureTags_with_comment_text_box.png')
#         # utils.execute_script_with_banner("Sending Document to Signer")
#         # sign.click_send_btn()
#         # utils.execute_script_with_banner("Logout as Sender, After sending Document")
#         # utils.logout()
#         # # Login as approver1 and complete e-sign and comment
#         # driver.get(constants.baseUrl)
#         # utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#         # login.login_page(constants.signer1_email, constants.signer1_password)
#         # home.validate_home_page()
#         # utils.execute_script_with_banner("Clicking on Manage Tab and Send Button to select respective envelope")
#         # upload.navigateToEnvelope(constants.envelope_Envelope_VerifyComment)
#         # utils.getscreenshot('/2.EnabledSignButtonForEnvelopeSigning.png')
#         # upload.clickPrimarySignButton()
#         # login.login_page(constants.signer1_email, constants.signer1_password)
#         # approve.clickContinueBtnForSigning()
#         # utils.execute_script_with_banner("Recipient 1 adding the Signature for pending document")
#         # approve.clickSecondarySignButton(constants.index_one)
#         # approve.e_sign_reason()
#         # approve.click_continue_btn()
#         # approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
#         # utils.execute_script_with_banner("without comment unable to finish the process")
#         # approve.click_finish_btn()
#         # utils.execute_script_with_banner("required popup is displayed")
#         # approve.verify_required_message()
#         # utils.getscreenshot('/3.comment_Required.png')
#         # approve.add_comment()
#         # utils.getscreenshot('/4.signers_comment.png')
#         # approve.click_finish_btn()
#         # utils.execute_script_with_banner("Logout as Signer")
#         # utils.logout()
#         # driver.get(constants.baseUrl)
#         # # Login as Sender and verify signature and comment
#         # utils.execute_script_with_banner("Login to DocuSign again, this time using the sender credentials", False)
#         # login.login_page(constants.sender_email, constants.sender_password)
#         # home.validate_home_page()
#         # upload.navigateToEnvelope(constants.envelope_Envelope_VerifyComment, True)
#         # try:
#         #     os.remove(constants.pdf_file_path1)
#         # except:
#         #     print("downloads folder is empty")
#         #
#         # print("complete")
#         # utils.execute_script_with_banner("Verifying the signature and comment Fields as a sender ")
#         # download.combine_download()
#         # Util_Test.validate_pdf_data(filecontents=[constants.pdf_file_path1, constants.comment_field], first_page=True)