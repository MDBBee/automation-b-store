import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from typing import Optional


class Test002DataDrivenLoginTests:
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_data_driven(self, setup):
        self.logger.info("*********** Test002DataDrivenLoginTests ************")
        self.logger.info("*********** Verifying Login Test Data Driven ************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        # self.driver.maximize_window()
        #
        self.lp = LoginPage(self.driver)
        # self.lp.clickLoginLink()
        # time.sleep(2)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print(f"😎ROWS😎EXCEL {self.rows}")

        test_status = []
        for r in range(2, self.rows + 1):
            self.lp.clickLoginLink()
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, self.lp.textbox_email_id))
            )

            self.user_email = XLUtils.readData(self.path, "Sheet1", r, 1)
            raw_password = XLUtils.readData(self.path, "Sheet1", r, 2)
            if str(raw_password).split(".")[0]:
                self.password = str(raw_password).split(".")[0]
            else:
                self.password = raw_password
            self.expected_result = XLUtils.readData(self.path, "Sheet1", r, 3)

            print("😎😎😎🐳🐳", self.password, self.user_email)

            self.lp.setUserName(self.user_email)
            self.lp.setPassword(self.password)
            self.lp.clickLoginButton()

            wait = WebDriverWait(self.driver, 5)
            login_button: Optional[WebElement] = None
            invalid_login_text: Optional[WebElement] = None
            try:
                # Wait for success indicator
                wait.until(
                    EC.element_to_be_clickable((By.ID, LoginPage.button_usericon_text))
                )
                login_button = self.driver.find_element(By.ID, LoginPage.button_usericon_text)

            except TimeoutException:
                # If success didn't appear, check for failure message
                login_button = None
                try:
                    login_failed_div = wait.until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='text-center text-destructive']"))
                    )
                    invalid_login_text = login_failed_div.text

                except TimeoutException:
                    # Neither success nor failure appeared → unexpected condition
                    invalid_login_text = None
                    self.logger.error("No login status element found")

            print("😎BUTTONS😎", login_button, "INVALID-BTN:", invalid_login_text, "#", self.user_email[0].upper())
            if login_button and login_button.text == self.user_email[0].upper():
                if self.expected_result == "Pass":
                    self.logger.info("*********** Passed ************")
                    print("IN THE FIRST IF---->")
                    wait.until(
                        EC.element_to_be_clickable((By.ID, LoginPage.button_usericon_text))
                    )
                    self.lp.clickUserIcon()
                    time.sleep(1)
                    self.lp.clickLogout()
                    test_status.append("Pass")
                    time.sleep(2)
                    # break
                elif self.expected_result == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    test_status.append("Fail")
                    time.sleep(5)
            elif invalid_login_text and invalid_login_text == "Invalid email or password":
                if self.expected_result == "Pass":
                    self.logger.info("*********** Failed ************")
                    test_status.append("Fail")
                elif self.expected_result == "Fail":
                    self.driver.back()
                    time.sleep(2)
                    # self.lp.clickLogout()
                    test_status.append("Pass")
            else:
                print("IN THE LAST ELSE---->")
                time.sleep(3)
                self.lp.clickUserIcon()
                time.sleep(2)
                self.lp.clickLogout()
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
