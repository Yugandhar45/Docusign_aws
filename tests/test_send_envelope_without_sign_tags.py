# from pages.addSignTagPage import Add_Sign_Tags
# from pages.homePage import Home_Page
# from pages.loginPage import Login_Page
# from pages.uploadPage import Upload_Page
# import pytest
# from testData import constants as constants
# from utilities.utils import Util_Test
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_Send_Env_NoSign_Tags:
#     def test_send_env_NoSign_tags(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         upload = Upload_Page(driver)
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Started Execution for Sending Envelop Without Sign Tag")
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner(
#             "Entering the valid credentials (username and password) to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         # Upload docx envelope file
#         utils.execute_script_with_banner("Home page is Displayed")
#         home.validate_home_page()
#         home.click_start_button()
#         utils.execute_script_with_banner("Clicking on start button to send the envelope")
#         home.send_envelope()
#         utils.execute_script_with_banner("Uploading the Document as a sender")
#         upload.upload_envelope_documents(constants.envelope1_docx, False)
#         utils.execute_script_with_banner("Adding recipient 1 and other details:")
#         upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
#         utils.execute_script_with_banner("Adding recipient 2 and other details:")
#         upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
#         upload.click_next_btn()
#         sign = Add_Sign_Tags(driver)
#         utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
#         sign.addSignatureTag(350)
#         utils.execute_script_with_banner("Not allowed to send a Document without adding sign tag for Signer 2")
#         sign.send_envelop_without_sign_tags()
#         utils.getscreenshot('/1.Error_msg_reg_21_CFR_Part_11.png')
