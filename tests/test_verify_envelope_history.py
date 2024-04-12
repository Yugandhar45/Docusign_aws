import time
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from testData import constants as constants
from pages.auditLogs import Audit_Logs
from pages.verifyData import Envelope_History
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class Test_EnvelopeHistory:
    def test_verify_envelopeHistory_auditLogs(self, request):
        # Verify data:
        driver = request.cls.driver
        driver.get(constants.baseUrl)
        login = Login_Page(driver)
        home = Home_Page(driver)
        utils = Util_Test(driver)
        utils.create_directory(request.node.name)
        utils.execute_script_with_banner("Started the Execution for verifying envelop history")
        utils.execute_script_with_banner(
            "Entering the valid credentials (username and password) to log in as the sender")
        login.login_page(constants.sender_email, constants.sender_password)
        home.validate_home_page()
        utils.execute_script_with_banner("Home page is launch")
        data = Envelope_History(driver)
        utils.execute_script_with_banner("Uploading the document for check the Date Format")
        data.verify_dateFormat(constants.envelope_file_docx)

        # Verify Envelope history
        data = Envelope_History(driver)
        data.verify_envelope_history()

        # Verify Audit logs
        logs = Audit_Logs(driver)
        utils.execute_script_with_banner("Verifying the Audit logs data")
        logs.verify_auditLogs()
        utils.read_data_from_csv(constants.csv_envelope_report)
        utils.execute_script_with_banner("Logout as a Sender after verifying the Audit_log Document")
        utils.logout()
