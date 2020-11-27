import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setUp")
class TestOne(BaseClass):

 def test_e2e(self):
     log = self.getLogger()

     homePage = HomePage(self.driver)
     homePage.shopItems().click()
     #self.driver.get_screenshot_as_file("rahul.png")
     checkOutPage = CheckOutPage(self.driver)
     products = checkOutPage.getProducts()



     # //*[@class='card h-100']/div/h4/a
     for product in products:
         productName = product.find_element_by_xpath("//*[@class='card h-100']/div/h4/a").text

         log.info("Product name ==> "+productName)

         if productName == "Blackberry":
             product.find_element_by_xpath("//*[@class='card h-100']/div[2]/button").click()
     self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
     self.driver.find_element_by_xpath("//*[contains(text(),'Checkout')]").click()
     log.info("Typing a country name")


     self.driver.find_element_by_id("country").send_keys("Turkey")
     #wait = WebDriverWait(self.driver, 10)
     #wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='suggestions']//li/a")))

     self.webDriverWait(10,(By.XPATH, "//*[@class='suggestions']//li/a"))

     # time.sleep(10)
     self.driver.find_element_by_xpath("//*[@class='suggestions']//li/a").click()
     self.driver.find_element_by_xpath("//*[contains(text(),'agree with')]").click()




     self.driver.find_element_by_xpath("//*[@type='submit']").click()




     message = self.driver.find_element_by_xpath("//*[contains(@class,'alert-dismissible')]").text

     log.info("The alert message ==> "+message)



     assert "Thank dfghgjyou!" in message
