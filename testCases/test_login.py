import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage


class Test001Login:
    baseUrl = "https://b-store-three.vercel.app/"
    username = "max@mail.com"
    password = "12345678"

    # def test_home_page_title(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     actual_title = self.driver.title
    #     self.driver.close()
    #     assert actual_title == "Home | B-store"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.lp.clickLoginLink()
        time.sleep(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        wait = WebDriverWait(self.driver, 5)  # up to 5 seconds
        wait.until(
            EC.element_to_be_clickable((By.XPATH, LoginPage.link_logout_linktext))
        )
        login_button_letter = self.driver.find_element(By.XPATH, LoginPage.link_logout_linktext)

        if login_button_letter != "Sign-in":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
