from pages.addSignTagPage import Add_Sign_Tags
from pages.homePage import Home_Page
from pages.loginPage import Login_Page
from pages.uploadPage import Upload_Page
import pytest
from testData import constants as constants
from utilities.utils import Util_Test


@pytest.mark.usefixtures("test_setup")
class Test_Send_Env_NoSign_Tags:
    def test_send_envelope_With_NoSign_tags(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Started Execution for Sending Envelop Without Sign Tag")
        utils.create_directory(request.node.name)
        logger = Util_Test.initialize_logger('Send envelop without sign tag')
        try:
            utils.execute_script_with_banner(
                "Entering the valid credentials (username and password) to log in as the sender")
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            # Upload docx envelope file
            utils.execute_script_with_banner("Home page is Displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page")
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on start button to send the envelope")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the Document as a sender")
            upload.upload_envelope_documents(constants.envelope1_docx, False)
            Util_Test.write_custom_logs(logger, "Uploaded the document as a sender")
            utils.execute_script_with_banner("Adding recipient 1 and other details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            utils.execute_script_with_banner("Adding recipient 2 and other details:")
            upload.addRecipient(constants.signer2_name, constants.signer2_email, constants.index_two)
            Util_Test.write_custom_logs(logger, "Added the recipient 2 details.")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            sign = Add_Sign_Tags(driver)
            utils.execute_script_with_banner("Adding Signature Tag for Recipient 1")
            sign.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.execute_script_with_banner("Not allowed to send a Document without adding sign tag for Signer 2")
            sign.send_envelop_without_sign_tags()
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            utils.getscreenshot('/1.Error_msg_WithOut_SignTags.png')
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()
        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()
            pytest.fail()
