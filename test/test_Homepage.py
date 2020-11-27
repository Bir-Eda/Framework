import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):
    def test_homepage(self,getData,getData2):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.info("first name is " + getData[0])

        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getPassword().send_keys(getData[2])
        time.sleep(2)


        self.selectByText(homepage.getGender(),getData2["gender"])

        homepage.getDate().send_keys(getData2["date"])
        time.sleep(2)

        log.info("Sending credentials")
        homepage.submitCredentials().click()
        time.sleep(2)
        self.driver.refresh()


    @pytest.fixture(params= HomePageData.test_getData)
    def getData(self,request):
        return request.param

    @pytest.fixture(params=HomePageData.test_getData2)
    def getData2(self, request):
        return request.param


