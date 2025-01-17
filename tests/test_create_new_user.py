# from pages.loginPage import Login_Page
# from pages.homePage import Home_Page
# from testData import constants as constants
# from pages.verifyData import Envelope_History
# from utilities.utils import Util_Test
# import pytest
#
#
# @pytest.mark.usefixtures("test_setup")
# class Test_Add_User:
#     def test_create_new_user(self, request):
#         driver = request.cls.driver
#         driver.get(constants.baseUrl)
#         login = Login_Page(driver)
#         home = Home_Page(driver)
#         utils = Util_Test(driver)
#         utils.execute_script_with_banner("Started the Execution for creating new user and verify email preferences")
#         utils.execute_script_with_banner(
#             "Entering the valid credentials to log in as the sender")
#         utils.create_directory(request.node.name)
#         logger = Util_Test.initialize_logger('Create new user')
#
#         try:
#             login.login_page(constants.sender_email, constants.sender_password)
#             Util_Test.write_custom_logs(logger, "Logged in to the DocuSign Application successfully")
#             # Create an user
#             utils.execute_script_with_banner("Home page is Displayed")
#             home.validate_home_page()
#             Util_Test.write_custom_logs(logger, "Validated the home page")
#             user = Envelope_History(driver)
#             utils.execute_script_with_banner("Creating the new user by filling all required fields and save", False)
#             user.creating_user()
#             Util_Test.write_custom_logs(logger, "Created the new user by filling all the details")
#             utils.execute_script_with_banner("Filling all the Required fields and saving the changes")
#             user.click_email_preferences()
#             user.validatingOptionsUnderEmailPreferences()
#             Util_Test.write_custom_logs(logger, "Validated the options under email preferences.")
#             user.verifying_email_prefs_header()
#             user.updating_email_preferences(True)
#             # Changing defaulting setting back by checking all preferences
#             utils.execute_script_with_banner("Changing the default settings")
#             user.verifying_email_prefs_header()
#             user.updating_email_preferences()
#             utils.execute_script_with_banner("Logout as a User after making the changes")
#             utils.logout()
#             Util_Test.write_custom_logs(logger, "Logged out from the sender.")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#
#         except:
#             # Log the exception and mark the test as failed
#             Util_Test.write_custom_logs(logger, f"Test  case failed")
#             Util_Test.add_test_name_to_doc(request.node.name)
#             Util_Test.add_screenshots_to_doc()
#             pytest.fail()
