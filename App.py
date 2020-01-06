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
        elem.find_element_by_class_name("support-btn-img").click() #clic qur "regarder une pub
        elem.find_element_by_class_name("close-modal-cross").click() #clic qur la croix pour fermer la page de pub
        elem.find_element_by_class_name("banner-container").click()  #clic qur "passer a la pub suivante"
        # Si il est sur youtube, apres avoir regarde le nbexec de video il relance une recherche utip jusqu'a la fin de la liste
        elem.find_element_by_class_name("yellow-btn button-no-style") #clic sur terminer la session 
        # une fois que le bot a fini de regarder le nbexec il clic sur terminer ma session puis recherche le youtubeur suivant jusqu'a la fin de la liste

    def execYtb(self):
        self.driver.get(self.urlYtb)
        self.driver.find_element_by_name("search_query").send_keys(self.listYtb[0])
        self.driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
        time.sleep(7)
        elem = self.driver.find_element_by_id("channel-section").click()
        # clic sur l'onglet video
        # clic sur la derniere video et la regarde nbexec fois
        # relance la recherche du bot sur utip jusqu'a la ifn de la liste

    def execute(self):
        self.driver.get(self.urlUtip)
        elem = self.driver.find_element_by_class_name("ncs-input-container")
        elem = elem.find_element_by_css_selector("input")
        elem.send_keys(self.listYtb[0])
        time.sleep(7)
        elem = self.driver.find_elements_by_class_name("redirect-feed")
        if len(elem) > 0:
            self.execUtip(elem[0])
        else :
            self.execYtb()
