from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

list_chaine = ["Squeezie","Zerator","Cyprien"] #a faire en dynamique
print("Liste des youtubeur")
for value in list_chaine :
    print(value)


def Testbot():
    driver = webdriver.Chrome(r"..\drivers\chromedriver.exe")

    # driver.set_page_load_timeout(10)
    # driver.get("https://www.google.fr/") #Aller chercher google.fr
    # driver.find_element_by_name("q").send_keys("Youtube")  # q = barre de recherche
    # driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  # btnK = bouton rechercher / faire l'action appuyer sur entrée
    # driver.find_element_by_class_name("S3Uucc").click()

    driver.get("https://www.youtube.com/?hl=fr&gl=FR")
    #driver.maximize_window()
    driver.find_element_by_name("search_query").send_keys("Zerator")
    driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
    time.sleep(2)
    elem = driver.find_element_by_id("channel-section").click()

    # elem[151].click()
    # for index,value in enumerate (elem) :
    #     print (str(index)+", "+value.text)
    #elem[0].click()
    #ActionChains(driver).move_to_element(elem[0]).click(button_sub).perform()
    #content = driver.find_element_by_css_selector('a.yt-simple-endpoint').click()

    print("Test completed succesfully")
