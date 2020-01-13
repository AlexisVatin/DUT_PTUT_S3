from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import datetime


class Bot():
    urlYtb = "https://www.youtube.com/"
    urlUtip = "https://utip.io/"

    def __init__(self, listYtb, driverUrl, NumberLoop):
        self.listYtb = listYtb
        self.driver = webdriver.Chrome(driverUrl)
        self.Number_loop = NumberLoop
        # nbexec a passer en argument lors de l'instanciation du bot (comme liste)

    def execUtip(self, elem):
        # clic sur le lien dans la barre de recherche utip
        elem.click()
        # clic qur regarder une pub
        time.sleep(5)
        self.driver.find_element_by_class_name("support-btn-img").click()
        i = 0
        for i in range(0, int(self.Number_loop)):
            while True: #i < int(self.Number_loop):
                try:
                    banner = self.driver.find_element_by_class_name("banner-container")
                    if banner:
                        banner.click()
                        i = i + 1
                        time.sleep(5)
                        break
                except:
                    time.sleep(1)

    def execYtb(self, name):
        self.driver.get(self.urlYtb)
        # Recherche le nom de la chaine dans la barre de recherche et appuie sur ENTER
        self.driver.find_element_by_name("search_query").send_keys(name)
        self.driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
        # Attente car certaines connexions sont plus lentes que d'autres
        time.sleep(2)
        # clic sur la chaine Youtube
        elem = self.driver.find_element_by_id("channel-section").click()
        time.sleep(5)
        # clic sur la derniere video de la chaine
        elem = self.driver.find_element_by_class_name("style-scope ytd-grid-video-renderer").click()
        for i in range(0, int(self.Number_loop)):
            time.sleep(324)
            # Rechargement page
            self.driver.refresh()

    def execute(self):
        for name in self.listYtb:
            self.driver.get(self.urlUtip)
            elem = self.driver.find_element_by_class_name("ncs-input-container")
            elem = elem.find_element_by_css_selector("input")
            elem.send_keys(name)
            time.sleep(5)
            elem = self.driver.find_elements_by_class_name("redirect-feed")
            if len(elem) > 0:
                self.execUtip(elem[0])
            else:
                self.execYtb(name)

        self.stop()

    def stop(self):
        self.driver.close()
