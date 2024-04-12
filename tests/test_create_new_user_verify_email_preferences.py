from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.verifyData import Envelope_History
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_Verify_Email_Preferences:
    def test_verify_email_preferences(self, request):
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        utils = Util_Test(driver)
        utils.execute_script_with_banner("Started the Execution for creating new user and verify email preferences")
        utils.execute_script_with_banner(
            "Entering the valid credentials (username and password) to log in as the sender")
        utils.create_directory(request.node.name)
        login.login_page(constants.sender_email, constants.sender_password)
        # Create an user
        utils.execute_script_with_banner("Home page is launch")
        home.validate_home_page()
        user = Envelope_History(driver)
        utils.execute_script_with_banner("Creating the new user",False)
        user.creating_user()
        utils.execute_script_with_banner("Filling all the Required fields and saving the changes")
        user.click_email_preferences()
        user.validatingOptionsUnderEmailPreferences()
        user.verifying_email_prefs_header()
        user.updating_email_preferences(True)
        # Changing defaulting setting back by checking all preferences
        utils.execute_script_with_banner("Changing the default settings")
        user.verifying_email_prefs_header()
        user.updating_email_preferences()
        utils.execute_script_with_banner("Logout as a User after making the changes")
        utils.logout()
