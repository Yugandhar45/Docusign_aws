import time
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.settingsPage import Settings_Page
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Date_Time_Format:
    def test_verify_date_time_format(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Started the Execution for Verify date and time format")
        login = Login_Page(driver)
        home = Home_Page(driver)
        settings = Settings_Page(driver)
        utils.create_directory(request.node.name)
        logger = Util_Test.initialize_logger('Verify date time format')
        utils.execute_script_with_banner(
            "Entering the valid credentials to log in as the sender")
        try:
            login.login_page(constants.sender_email, constants.sender_password)
            Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
            utils.execute_script_with_banner("Home page is Displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page")
            utils.execute_script_with_banner(
                "pre-requisite for this scenario --- checking the Allow user check box is selected")
            # pre-requisite for this scenario --- checking the Allow user check box
            settings.selectCheckboxForAllowUserTimeZoneAndDateFormat()
            Util_Test.write_custom_logs(logger, "Navigated to the setting tag and clicked on Regional setting to select the checkbox of time zone")

            # User can change date/time format
            utils.execute_script_with_banner("click userprofile icon and my preferences")
            home.click_userprofile_and_preferences()
            Util_Test.write_custom_logs(logger, "Navigated to profile icon and clicked on 'my preference' option")
            utils.execute_script_with_banner("user can change date/time format")
            settings.allowUserToChangeDateTimeFormat()
            Util_Test.write_custom_logs(logger, "Verified that the user is able to change the time and date format")
            utils.execute_script_with_banner("click Setting Tab and regional settings to unselect Allow User Check Box")
            settings.unSelectCheckboxForAllowUserTimeZoneAndDateFormat()
            Util_Test.write_custom_logs(logger, "Unchecked the time zone after navigating to the settings tag and clicking on the regional tab.")
            utils.execute_script_with_banner("logout as the sender")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the sender.")
            driver.get(constants.baseUrl)
            utils.execute_script_with_banner("Entering the valid credentials to log in as the signer")
            login.login_page(constants.signer1_email, constants.signer1_password)
            Util_Test.write_custom_logs(logger, "Logged in as the recipient 1, i.e., signer 1.")
            utils.execute_script_with_banner("Home page is displayed")
            home.validate_home_page()
            Util_Test.write_custom_logs(logger, "Validated the home page.")
            # User can change date/time format
            utils.execute_script_with_banner("click userprofile and my preferences")
            home.click_userprofile_and_preferences()
            Util_Test.write_custom_logs(logger, "Navigated to profile icon and clicked on 'my preference' option")
            utils.execute_script_with_banner(
                "user not allowed to change date/time format as Allow User check box is unselected")
            settings.userNotAllowToChangeDateTimeFormat()
            Util_Test.write_custom_logs(logger, "Validated that user is not able to change the time date format.")
            utils.execute_script_with_banner("Logout as signer")
            utils.logout()
            Util_Test.write_custom_logs(logger, "Logged out from the signer.")
        except:
            # Log the exception and mark the test as failed
            Util_Test.write_custom_logs(logger, f"Test  case failed")
            pytest.fail()

