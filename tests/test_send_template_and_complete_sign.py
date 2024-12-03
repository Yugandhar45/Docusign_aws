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
        logger = Util_Test.initialize_logger('Send template and complete')
        utils.execute_script_with_banner(
            "Entering the username and password to log in as the sender")
        try:
            Util_Test.write_custom_logs(logger, "Send template and sign script execution - Started")
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            utils.execute_script_with_banner("Home page is Displayed")
            time.sleep(10)
            home.click_start_button()
            Util_Test.write_custom_logs(logger, "Clicked on the start button to open the upload envelop section.")
            utils.execute_script_with_banner("Clicking on the start button to send the Templates")
            home.send_envelope()
            utils.execute_script_with_banner("Uploading the Template-1 as a sender")
            upload.upload_envelope_documents(constants.template1, False)
            Util_Test.write_custom_logs(logger, "Uploaded the template-1 as a sender")
            temp.matching_templates_popup()
            Util_Test.write_custom_logs(logger, "Clicked on the canceled button for matching template popup")
            utils.execute_script_with_banner("Uploading the Template-2 as a sender")
            upload.upload_envelope_documents(constants.template2, False)
            Util_Test.write_custom_logs(logger, "Uploaded the template-2 as a sender")
            temp.matching_templates_popup()
            Util_Test.write_custom_logs(logger, "Clicked on the canceled button for matching template popup")

            utils.execute_script_with_banner("Adding recipient1 and other details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            utils.execute_script_with_banner("Clicking on the next button")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            # verifying actions under action Dropdown and also saving and close the template
            utils.execute_script_with_banner("Clicking on the Actions dropdown and click on the Save and Close option")
            signtag.saveAndCloseTemplateWithActionButton()
            Util_Test.write_custom_logs(logger, "Validated the option and click on the save and close button")
            utils.execute_script_with_banner("Navigating to the manage tab,clicking on the Drafts section to select the "
                                             "respective Templates")
            # still document is in draft State
            upload.navigateToEnvelope(constants.template_test)
            Util_Test.write_custom_logs(logger, "Navigated to the template")
            # Verifying actions under more while saving the template
            utils.execute_script_with_banner("Clicking on the More dropdown and click on the Save as Template option")
            temp.save_as_template()
            Util_Test.write_custom_logs(logger, "Clicked on save as template button")
            upload.navigateToTemplate(constants.template_name)
            Util_Test.write_custom_logs(logger, "Again navigated to the template")
            utils.execute_script_with_banner("Clicking on the use button")
            temp.click_use_button()
            Util_Test.write_custom_logs(logger, "Clicked on use button")
            utils.execute_script_with_banner("Adding Recipient1 details:")
            upload.addRecipient(constants.signer1_name, constants.signer1_email, constants.index_one)
            Util_Test.write_custom_logs(logger, "Added the recipient 1 details.")
            upload.click_next_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the next button")
            utils.execute_script_with_banner("Adding Signature Tag for Recipient1 to the Template1")
            signtag.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            signtag.scroll_to_next_envelope()
            Util_Test.write_custom_logs(logger, "Scrolled to the next envelop")
            utils.execute_script_with_banner("Adding Signature Tag for Recipient1 to the Template2")
            signtag.addSignatureTag(350)
            Util_Test.write_custom_logs(logger, "Dragged and dropped the signature tag for recipient 1")
            signtag.click_send_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the send button to send the document.")
            utils.execute_script_with_banner("Logout as Sender after completing the process")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the sender.")

            utils.execute_script_with_banner("logging into the outlook to sign the Templates through the outlook by "
                                             "selecting the respective Templates which was sent by sender")
            driver.get(constants.outlook_url)
            outlook = Outlook_Page(driver)
            Util_Test.write_custom_logs(logger, "Navigated to the Outlook URL.")
            time.sleep(5)
            utils.execute_script_with_banner("Entering the outlook credentials of signer1")
            outlook.loginToOutlook(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the login task into the Outlook account.")
            # outlook.clickOtherFieldTab()
            utils.execute_script_with_banner("Clicking on the allocated mail which was sent by the Sender")
            outlook.clickRecentEmail(constants.recent_mail_for_review_envelope)
            Util_Test.write_custom_logs(logger, "Found and opened the desired mail.")
            # utils.execute_script_with_banner("Clicking on the Review Documents button to review the Documents")
            outlook.review_Document(True)
            Util_Test.write_custom_logs(logger, "Reviewing the document after opening the desired mail.")
            current_window = driver.current_window_handle
            windows = driver.window_handles
            new_window = [w for w in windows if w != current_window][0]
            driver.close()
            driver.switch_to.window(new_window)
            #utils.getscreenshot('/4.Docusign_Login_through_Outlook.png')
            # Login as a signer complete signature
            utils.execute_script_with_banner("Login to DocuSign again, this time using the signer credentials", False)
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
            sign = Approve_Envelope(driver)
            utils.execute_script_with_banner("Clicking on the continue button")
            #sign.clickContinueBtnForSigning()
            sign.clickSecondarySignButton(constants.index_one)
            Util_Test.write_custom_logs(logger, "Clicked on the signing tag button.")
            utils.execute_script_with_banner("Selecting the esign reason for the Template1")
            sign.e_sign_reason(False,True)
            Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
            utils.execute_script_with_banner("Clicking on the Continue button to sign the Templates")
            sign.click_continue_btn()
            Util_Test.write_custom_logs(logger, "Clicked on the 'Continue' button for signing and validated that the button was displayed.")
            sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Completed the final authentication step before signing.")
            sign.clickSecondarySignButton(constants.index_two)
            Util_Test.write_custom_logs(logger, "Clicked on the second signing tag button.")
            sign.e_sign_reason()
            Util_Test.write_custom_logs(logger, "Selected the reason for signing from the dropdown.")
            sign.switchToNewTab(constants.signer1_email, constants.signer1_password)
            utils.getscreenshot('/4.Completed_signing.png')
            Util_Test.write_custom_logs(logger, "Completed the final authentication step before signing.")
            utils.execute_script_with_banner("Clicking on Finish Button")
            sign.click_finish_btn()
            Util_Test.write_custom_logs(logger, "Clicked on Finish button")
            utils.execute_script_with_banner("Logout as Signer after completing the process")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the sender")
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()

        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            Util_Test.add_test_name_to_doc(request.node.name)
            Util_Test.add_screenshots_to_doc()
            pytest.fail()
