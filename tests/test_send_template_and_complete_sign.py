import time
from pages.approveDocument import Approve_Envelope
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages.uploadPage import Upload_Page
from testData import constants as constants
from pages.addSignTagPage import Add_Sign_Tags
from pages.templatesPage import Templates_Page
from utilities.utils import Util_Test
from pages.outlookPage import Outlook_Page
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_SendTemplate_Approve:
    def test_sendTemplate_approve(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        upload = Upload_Page(driver)
        temp = Templates_Page(driver)
        signtag = Add_Sign_Tags(driver)
        utils = Util_Test(driver)
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        utils.execute_script_with_banner("Home page is Displayed")
        time.sleep(10)
        home.click_start_button()
        utils.execute_script_with_banner("Clicking on the start button to send the Templates")
        home.send_envelope()
        utils.execute_script_with_banner("Uploading the Template-1 as a sender")
        upload.upload_envelope_documents(constants.template1, False)
        temp.matching_templates_popup()
        utils.execute_script_with_banner("Uploading the Template-2 as a sender")
        upload.upload_envelope_documents(constants.template2, False)
        temp.matching_templates_popup()
        utils.execute_script_with_banner("Adding recipient1 and other details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        utils.execute_script_with_banner("Clicking on the next button")
        upload.click_next_btn()
        # verifying actions under action Dropdown and also saving and close the template
        utils.execute_script_with_banner("Clicking on the Actions dropdown and click on the Save and Close option")
        signtag.saveAndCloseTemplateWithActionButton()
        utils.execute_script_with_banner("Navigating to the manage tab,clicking on the Drafts section to select the respective Templates")
        # still document is in draft State
        upload.navigateToEnvelope(constants.template_test)
        # Verifying actions under more while saving the template
        utils.execute_script_with_banner("Clicking on the More dropdown and click on the Save as Template option")
        temp.save_as_template()
        upload.navigateToTemplate(constants.template_name)
        utils.execute_script_with_banner("Clicking on the use button")
        temp.click_use_button()
        utils.execute_script_with_banner("Adding Recipient1 details:")
        upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
        upload.click_next_btn()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient1 to the Template1")
        signtag.addSignatureTag(350)
        signtag.scroll_to_next_envelope()
        utils.execute_script_with_banner("Adding Signature Tag for Recipient1 to the Template2")
        signtag.addSignatureTag(350)
        signtag.click_send_btn()
        utils.execute_script_with_banner("Logout as Sender after completing the process")
        utils.logout()

        utils.execute_script_with_banner("logging into the outlook to sign the Templates through the outlook by selecting the respective Templates which was sent by sender")
        driver.get(constants.outlook_url)
        outlook = Outlook_Page(driver)
        time.sleep(5)
        utils.execute_script_with_banner("Entering the outlook credentials of signer1")
        outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
        # outlook.clickOtherFieldTab()
        utils.execute_script_with_banner("Clicking on the allocated mail which was sent by the Sender")
        outlook.clickRecentEmail(constants.recent_mail_for_review_envelope)
        # utils.execute_script_with_banner("Clicking on the Review Documents button to review the Documents")
        outlook.review_Document()
        current_window = driver.current_window_handle
        windows = driver.window_handles
        new_window = [w for w in windows if w != current_window][0]
        driver.close()
        driver.switch_to.window(new_window)
        # Login as a signer complete signature
        utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
        login.login_page(constants.signer1_email, constants.signer1_password)
        sign = Approve_Envelope(driver)
        utils.execute_script_with_banner("Clicking on the continue button")
        sign.clickContinueBtnForSigning()
        sign.clickSecondarySignButton(constants.index_one)
        utils.execute_script_with_banner("Selecting the esign reason for the Template1")
        sign.e_sign_reason()
        utils.execute_script_with_banner("Clicking on the Continue button to sign the Templates")
        sign.click_continue_btn()
        sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
        sign.clickSecondarySignButton(constants.index_two)
        sign.e_sign_reason()
        sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
        utils.execute_script_with_banner("Clicking on Finish Button")
        sign.click_finish_btn()
        utils.execute_script_with_banner("Logout as Signer after completing the process")
        utils.logout()





