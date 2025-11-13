from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    textbox_email_id = "email"
    textbox_password_id = "password"
    link_login_xpath = "//a[normalize-space()='sign-in']"
    button_login_main = "//button[normalize-space(text())='Sign In']"
    link_logout_linktext = "//button[normalize-space(text())='M']"
    logout_button = "button.hover\\:bg-accent.hover\\:text-accent-foreground"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setUserName(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLoginLink(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_main).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
