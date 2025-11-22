import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test002DataDrivenLoginTests:
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData/Login_Test_Data.xlsx"
    logger = LogGen.loggen()

    def test_login_data_driven(self, setup):
        self.logger.info("*********** Test002DataDrivenLoginTests ************")
        self.logger.info("*********** Verifying Login Test Data Driven ************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        time.sleep(2)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")

        for r in range(2, self.rows + 1):
            self.useremail = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.expected_result = XLUtils.readData(self.path, "Sheet1", r, 3)

            # print("😎😎", self.password, self.useremail)
            self.lp.setUserName(self.useremail)
            time.sleep(10)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()

            wait = WebDriverWait(self.driver, 5)  # up to 5 seconds
            wait.until(
                EC.element_to_be_clickable((By.XPATH, LoginPage.link_usericon_linktext))
            )
            login_button_letter = self.driver.find_element(By.XPATH, LoginPage.link_usericon_linktext)

            test_status = []
            if login_button_letter != "Sign-in":
                if self.expected_result == "Pass":
                    self.driver.close()
                    self.logger.info("*********** Passed ************")
                    self.lp.clickUserIcon()
                    self.lp.clickLogout()
                    test_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    test_status.append("Fail")
            elif login_button_letter == "Sign-in":
                if self.expected_result == "Pass":
                    self.driver.close()
                    self.logger.info("*********** Failed ************")
                    test_status.append("Fail")
                elif self.expected_result == "Fail":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    test_status.append("Pass")
            if "Fail" not in test_status:
                self.logger.info("*** Login DDT test Passed ***")
                self.driver.close()
                assert True
            else:
                self.logger.info("*** Login DDT test Failed ***")
                self.driver.close()
                assert False

        self.logger.info("*** End of Login DDT test ***")
        self.logger.info("*** Completed Test002DataDrivenLoginTests ***")
