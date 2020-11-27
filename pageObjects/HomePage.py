from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage:

    def __init__ (self,driver):
        self.driver = driver


    shop = (By.XPATH, "//*[text()='Shop']")
    nameBox = (By.NAME, "name")
    emailBox = (By.NAME, "email")
    passwordBox = (By.ID, "exampleInputPassword1")
    dateBox = (By.XPATH, "//*[@name='bday']")
    submitBtn = (By.XPATH, "//*[@type='submit']")
    genderBox = (By.ID, "exampleFormControlSelect1")


    def shopItems(self):
       return  self.driver.find_element(*HomePage.shop)  #driver.find_element_by_xpath("//*[text()='Shop']").click()


    def getName(self):
        return self.driver.find_element(*HomePage.nameBox)

    def getEmail(self):
        return self.driver.find_element(*HomePage.emailBox)


    def getPassword(self):
        return self.driver.find_element(*HomePage.passwordBox)


    def getDate(self):
        return self.driver.find_element(*HomePage.dateBox)



    def submitCredentials(self):
        return self.driver.find_element(*HomePage.submitBtn)


    def getGender(self):
        return self.driver.find_element(*HomePage.genderBox)







