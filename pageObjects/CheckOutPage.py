from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver
    products = (By.XPATH,"//*[@class='card h-100']")  # products = self.driver.find_elements_by_xpath("//*[@class='card h-100']")



    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)