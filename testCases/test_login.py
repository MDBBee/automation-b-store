import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseUrl = ReadConfig.getApplicationUrl()
    user_email = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("*********** Test001Login ************")
        self.logger.info("*********** Verifying HomePage ************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(2)

        actual_title = self.driver.title
        self.driver.close()
        result = actual_title == "Home | B-store"
        if result:
            assert result
            self.logger.info("*********** Verifying HomePage Pass ************")
        else:
            assert result
            self.logger.info("*********** Verifying HomePage Fail ************")

    def test_login(self, setup):
        self.logger.info("*********** Verifying Login Test ************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        time.sleep(3)
        self.lp.setUserName(self.user_email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        wait = WebDriverWait(self.driver, 5)  # up to 5 seconds
        wait.until(
            EC.element_to_be_clickable((By.XPATH, LoginPage.button_usericon_text))
        )
        login_button_letter = self.driver.find_element(By.XPATH, LoginPage.button_usericon_text)
        # print("🐳🐳LB", login_button_letter)
        # print("🐳🐳LB-LETTER", login_button_letter.text)
        # "Sign-in"
        if login_button_letter.text == self.user_email[0].upper():
            assert True
            self.driver.close()
            self.logger.info("*********** Login Verification Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Login Verification Failed ************")
            assert False
