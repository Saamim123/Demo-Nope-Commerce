
import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    Baseurl=ReadConfig.getApplicationurl()
    username=ReadConfig.getusername()
    password=ReadConfig.password()

    logger=LogGen.loggen()

    def test_HomePageTitle(self,setup):
        self.logger.info('***** Test_001_Login ***')
        self.logger.info('***** Verifying Home Page Title ***')

        self.driver=setup
        self.driver.get(self.Baseurl)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('***** Home Page Title test is pass ***')

        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error('***** Home Page Title test is fail ***')

            assert False

    def test_login(self,setup):
        self.logger.info('***** verifying login test ***')

        self.driver=setup
        self.driver.get(self.Baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info('***** login test passed ***')


        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error('***** login test failed ***')
            assert False
