import os

from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.uploadPage import Upload_Page
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Change_Sign_Tag_Size:
    def test_change_sign_size(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        utils = Util_Test(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        #utils.create_directory(request.node.name)
        utils.execute_script_with_banner("Started the Execution for changing the Signature Tag size")
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        home.validate_home_page()
        home.click_start_button()
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Document as a sender")
        upload.upload_envelope_documents()
        utils.execute_script_with_banner("Adding first recipients and other details:")
        upload.clickSetSigningOrderCheckbox()
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Adding second recipients and other details:")
        upload.addRecipient(constants.signer2_name, constants.signer2_email,constants.index_two)
        upload.click_next_btn()
        add_sign = Add_Sign_Tags(driver)
        utils.execute_script_with_banner("Changing the size of Signature Tag")
        add_sign.addSignatureTag(350)
        Util_Test.getscreenshot('/1.Before_changing_Signature_Tag_size_100%_resolution.png')
        add_sign.validateOptionsUnderSignature()
        add_sign.change_sign_tag_size()
        Util_Test.getscreenshot('/2.After_Changing_signature_Tag_size_200%_resolution.png')
        add_sign.select_signer(constants.index_two)
        add_sign.addSignatureTag(650)
        add_sign.change_sign_tag_size()
        # add_sign.click_send_btn()
        # utils.execute_script_with_banner("Logout as Sender, After changing the size of sign tag")
        # utils.logout()



