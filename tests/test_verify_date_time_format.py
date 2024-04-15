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
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         settings = Settings_Page(driver)
#         utils = Util_Test(driver)
#         utils.create_directory(request.node.name)
#         login.login_page(constants.sender_email, constants.sender_password)
#         home.validate_home_page()
#         # pre-requisite for this scenario --- checking the Allow user check box
#         settings.selectCheckboxForAllowUserTimeZoneAndDateFormat()
#         # User can change date/time format
#         home.click_userprofile_and_preferences()
#         settings.allowUserToChangeDateTimeFormat()
#         settings.unSelectCheckboxForAllowUserTimeZoneAndDateFormat()
#         utils.logout()
#         driver.get(constants.baseUrl)
#         login.login_page(constants.signer1_email, constants.signer1_password)
#         home.validate_home_page()
#         # User can change date/time format
#         home.click_userprofile_and_preferences()
#         settings.userNotAllowToChangeDateTimeFormat()
#         utils.logout()
