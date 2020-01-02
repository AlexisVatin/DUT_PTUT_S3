from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Bot():
    urlYtb = "https://www.youtube.com/"
    urlUtip = "https://utip.io/"

    def __init__(self, listYtb, driverUrl):
        self.listYtb = listYtb
        self.driver = webdriver.Chrome(driverUrl)
        # nbexec a passer en argument lors de l'instanciation du bot (comme liste)

    def execUtip(self, elem):
        elem.click()

    def execYtb(self):
        self.driver.get(self.urlYtb)
        self.driver.find_element_by_name("search_query").send_keys(self.listYtb[0])
        self.driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
        time.sleep(2)
        elem = self.driver.find_element_by_id("channel-section").click()

    def execute(self):
        self.driver.get(self.urlUtip)
        elem = self.driver.find_element_by_class_name("ncs-input-container")
        elem = elem.find_element_by_css_selector("input")
        elem.send_keys(self.listYtb[0])
        time.sleep(2)
        elem = self.driver.find_elements_by_class_name("redirect-feed")
        if len(elem) > 0:
            self.execUtip(elem[0])
        else :
            self.execYtb()
