import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomepageData
from pageObjects.HomePage import Homepage
from utilities.Baseclass import Baseclass


class TestHomePage(Baseclass):
    def test_FormSubmission(self, getData):
        log = self.getLogger()
        home = Homepage(self.driver)
        log.info("Name: " + getData["name"])
        home.getName().send_keys(getData["name"])
        log.info("Email: " + getData["email"])
        home.getEmail().send_keys(getData["email"])
        log.info("Password: " + getData["password"])
        home.getPassword().send_keys(getData["password"])
        home.checkIcecream().click()
        log.info("Gender: " + getData["gender"])
        self.SelectOptionByText(home.genderSelection(), getData["gender"])
        home.submitButton().click()
        alert = home.getAlert().text
        assert "Success!" in alert
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.getTestData("t1"))
    def getData(self, request):
        return request.param
