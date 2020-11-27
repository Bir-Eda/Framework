import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger





    def webDriverWait(self, time, webElementTuple ):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.element_to_be_clickable(webElementTuple)) # (By.XPATH, "value")


    def selectByText(self,webElement, text ):
        sel = Select(webElement)
        sel.select_by_visible_text(text)



    def selectByIndex(self,webElement, index ):
        sel = Select(webElement)
        sel.select_by_index(index)


















