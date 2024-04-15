# from pages.approveDocument import Approve_Envelope
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from pages.uploadPage import Upload_Page
# from testData import constants as constants
# from pages.addSignTagPage import Add_Sign_Tags
# from pages.templatesPage import Templates_Page
# from utilities.utils import Util_Test
# from pages.outlookPage import Outlook_Page
# import pytest
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_SendTemplate_Approve:
#     def test_sendTemplate_approve(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         temp = Templates_Page(driver)
#         signtag = Add_Sign_Tags(driver)
#         utils = Util_Test(driver)
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner(
#             "Entering the username and password to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         utils.execute_script_with_banner("Home page is launch")
#         home.click_start_button()
#         home.send_envelope()
#         utils.execute_script_with_banner("Uploading the Template-1 as a sender")
#         upload.upload_envelope_documents(constants.template1, False)
#         temp.matching_templates_popup()
#         utils.execute_script_with_banner("Uploading the Template-2 as a sender")
#         upload.upload_envelope_documents(constants.template2, False)
#         temp.matching_templates_popup()
#         utils.execute_script_with_banner("Adding recipients and other details:")
#         # home.addRecipient1(constants.signerName, constants.my_email)
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         upload.click_next_btn()
#         # verifying actions under action Dropdown and also saving and close the template
#         signtag.saveAndCloseTemplateWithActionButton()
#         utils.execute_script_with_banner("Selecting the Template and saving it")
#         # still document is in draft State
#         upload.navigateToEnvelope(constants.template_test)
#         # Verifying actions under more while saving the template
#         temp.save_as_template()
#         upload.navigateToTemplate(constants.template_name)
#         temp.click_use_button()
#         utils.execute_script_with_banner("Adding two recipients and other details:")
#         # home.addRecipient1(constants.signerName, constants.my_email)
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         upload.click_next_btn()
#         utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#         signtag.addSignatureTag(350)
#         signtag.scroll_to_next_envelope()
#         utils.execute_script_with_banner("Adding Signature Tag for 2nd enveloe")
#         signtag.addSignatureTag(350)
#         signtag.click_send_btn()
#         utils.execute_script_with_banner("Logout as Sender after completing the process")
#         utils.logout()
#
#         driver.get(constants.outlook_url)
#         outlook = Outlook_Page(driver)
#         outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
#         outlook.clickOtherFieldTab()
#         outlook.clickRecentEmail(constants.recent_mail_for_review_envelope)
#         outlook.review_Document()
#         current_window = driver.current_window_handle
#         windows = driver.window_handles
#         new_window = [w for w in windows if w != current_window][0]
#         driver.switch_to.window(new_window)
#
#         # Login as a signer complete signature
#         utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         sign = Approve_Envelope(driver)
#         sign.clickContinueBtnForSigning()
#         utils.execute_script_with_banner("Signer adding the Signature 1 for pending document")
#         sign.clickSecondarySignButton(constants.index_one)
#         sign.e_sign_reason()
#         sign.click_continue_btn()
#         sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
#         utils.execute_script_with_banner("Signer adding the Signature 2 for pending document")
#         sign.clickSecondarySignButton(constants.index_two)
#         sign.e_sign_reason()
#         sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
#         sign.click_finish_btn()
#         utils.execute_script_with_banner("Logout as Signer after completing the process")
#         utils.logout()
#
#
#
#
