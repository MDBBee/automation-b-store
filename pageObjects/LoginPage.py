from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    textbox_email_id = "email"
    textbox_password_id = "password"
    link_login_xpath = "//a[normalize-space()='sign-in']"
    button_login_main = "//button[normalize-space(text())='Sign In']"
    button_usericon_text = "//button[@id='user']"
    logout_button = "//button[normalize-space(text())='Sign Out']"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setUserName(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLoginLink(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_login_xpath))
        ).click()

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_main).click()

    def clickUserIcon(self):
        self.driver.find_element(By.XPATH, self.button_usericon_text).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button).click()
