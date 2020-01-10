from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


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
        # clic qur "regarder une pub
        time.sleep(2)
        elem.find_element_by_class_name("support-btn-container").click()
        # elem.find_element_by_class_name("support-btn support-btn").click()
        elem.find_element_by_class_name("close-modal-cross").click()
        # clic qur la croix pour fermer la page de pub
        # clic qur "passer a la pub suivante"
        # S'il est sur youtube, apres avoir regarde le nbexec de video il relance une recherche utip jusqu'a la fin de la liste
        elem.find_element_by_class_name("yellow-btn button-no-style")  # clic sur terminer la session
        # une fois que le bot a fini de regarder le nbexec il clic sur terminer ma session puis recherche le youtubeur suivant jusqu'a la fin de la liste
        
        for i in range(0, self.Number_loop):
            time.sleep(5)
            # Rechargement page
            self.driver.refresh()

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
        # clic sur l'onglet video
        # clic sur la derniere video et la regarde nbexec fois
        # relance la recherche du bot sur utip jusqu'a la ifn de la liste

        # Il faut faire attendre le sleep autant que la durée de la vidéo
        # time.sleep(5)
        # refresh la page nbexec fois puis close

        # Il faut faire attendre le sleep autant que la durée de la vidéo avant de fermer
        # time.sleep(5)
        # fermeture de la fenetre apres nbexec vue

        for i in range(0, self.Number_loop):
            time.sleep(5)
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
