# import time
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from pages.uploadPage import Upload_Page
# from testData import constants as constants
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.approveDocument import Approve_Envelope
# from pages.outlookPage import Outlook_Page
# from utilities.utils import Util_Test
# import pytest
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_Verify_AccessCode:
#     def test_verify_access_code(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         approve = Approve_Envelope(driver)
#         utils = Util_Test(driver)
#         add_sign = Add_Sign_Tags(driver)
#         utils.create_directory(request.node.name)
#         logger = Util_Test.initialize_logger('Access Code')
#         try:
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
#             # Upload docx envelope file
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page")
#             home.click_start_button()
#             Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
#             home.send_envelope()
#             upload.upload_envelope_documents(constants.envelope1_docx, False)
#             Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
#             upload.addRecipient(constants.signer1_name, constants.signer1_email,constants.index_one)
#             Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
#             # added access code
#             generated_access_code = Util_Test.get_random_code()
#             upload.add_access_code(generated_access_code)
#             Util_Test.write_custom_logs(logger, "Generated and added the access code")
#             utils.getscreenshot('/1.Added_Access_Code.png')
#             upload.click_next_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the next button")
#             add_sign.addSignatureTag(350)
#             Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
#             add_sign.click_send_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the send button")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Logout as the sender")
#             driver.get(constants.outlook_url)
#             outlook = Outlook_Page(driver)
#             time.sleep(5)
#             outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Login in to the outlook account")
#             outlook.clickRecentEmail(constants.recent_mail_for_review_envelope)
#             Util_Test.write_custom_logs(logger, "Navigated to the Respective email")
#             outlook.review_Document()
#             Util_Test.write_custom_logs(logger, "Reviewed the document")
#             current_window = driver.current_window_handle
#             windows = driver.window_handles
#             new_window = [w for w in windows if w != current_window][0]
#             driver.close()
#             driver.switch_to.window(new_window)
#             login.login_page(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Log in as the Sender")
#             approve.validate_access_code(generated_access_code)
#             Util_Test.write_custom_logs(logger, "Validated the Access code")
#             #approve.clickContinueBtnForSigning()
#             Util_Test.write_custom_logs(logger, "Clicked on the continue button")
#             approve.clickSecondarySignButton(constants.index_one)
#             Util_Test.write_custom_logs(logger, "Clicked on the Sign Button")
#             approve.e_sign_reason()
#             Util_Test.write_custom_logs(logger, "Selcted the sign reason")
#             approve.click_continue_btn()
#             approve.switchToNewTab(constants.signer1_email, constants.signer1_password)
#             Util_Test.write_custom_logs(logger, "Completed the Authentication")
#             approve.click_finish_btn()
#             Util_Test.write_custom_logs(logger, "Clicked on the Finish button")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Logout as the sender")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()
