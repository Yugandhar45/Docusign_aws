# import time
# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from testData import constants as constants
# from pages.settingsPage import Settings_Page
# from utilities.utils import Util_Test
# import pytest
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_Date_Time_Format:
#     def test_verify_date_time_format(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Started the Execution for Verify date and time format")
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         settings = Settings_Page(driver)
#         utils.create_directory(request.node.name)
#         utils.execute_script_with_banner(
#             "Entering the valid credentials to log in as the sender")
#         login.login_page(constants.sender_email, constants.sender_password)
#         utils.execute_script_with_banner("Home page is Displayed")
#         home.validate_home_page()
#         utils.execute_script_with_banner(
#             "pre-requisite for this scenario --- checking the Allow user check box is selected")
#         # pre-requisite for this scenario --- checking the Allow user check box
#         settings.selectCheckboxForAllowUserTimeZoneAndDateFormat()
#         # User can change date/time format
#         utils.execute_script_with_banner("click userprofile icon and my preferences")
#         home.click_userprofile_and_preferences()
#         utils.execute_script_with_banner("user can change date/time format")
#         settings.allowUserToChangeDateTimeFormat()
#         utils.execute_script_with_banner("click Setting Tab and regional settings to unselect Allow User Check Box")
#         settings.unSelectCheckboxForAllowUserTimeZoneAndDateFormat()
#         utils.execute_script_with_banner("logout as the sender")
#         utils.logout()
#         driver.get(constants.baseUrl)
#         utils.execute_script_with_banner("Entering the valid credentials to log in as the signer")
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         utils.execute_script_with_banner("Home page is displayed")
#         home.validate_home_page()
#         # User can change date/time format
#         utils.execute_script_with_banner("click userprofile and my preferences")
#         home.click_userprofile_and_preferences()
#         utils.execute_script_with_banner(
#             "user not allowed to change date/time format as Allow User check box is unselected")
#         settings.userNotAllowToChangeDateTimeFormat()
#         utils.execute_script_with_banner("Logout as signer")
#         utils.logout()
