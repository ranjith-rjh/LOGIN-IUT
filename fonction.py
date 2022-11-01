from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import dictionnaire as d
from time import sleep

# WEB DRIVER PATH
driver = webdriver.Chrome("chromedriver.exe")

def get_file_content(filename) :
    with open (filename, "r") as f :
        data = f.read().split('\n')
        return data

# READ DATA FROM GIVEN FILE 
data = get_file_content("login.txt")

def openUSMB(lien) :
    driver.get(lien)
    driver.maximize_window()

    # ENTRER LE USER ID 
    labelUtilisateur = driver.find_element(By.NAME, d.dict_USMB["labelUtilisateur"])
    labelUtilisateur.send_keys(data[1])

    # ENTRER LE MDP 
    labelMPD = driver.find_element(By.NAME, d.dict_USMB["labelMDP"]) 
    labelMPD.send_keys(data[2])

    # CLIQUER SUR LE BOUTON CONNEXION
    bouttonConnexion = driver.find_element(By.CLASS_NAME, d.dict_USMB["bouttonConnexion"])
    bouttonConnexion.click()

    # CLIQUER SUR LE BOUTON MESSAGERIE
    bouttonMessagerie = driver.find_element(By.LINK_TEXT, d.dict_USMB["boutonMessagerie"])
    bouttonMessagerie.click()

    # CLIQUER SUR LE BOUTON PLANNING
    boutonPlanning = driver.find_element(By.LINK_TEXT, d.dict_USMB["boutonPlanning"])
    boutonPlanning.click()

    driver.switch_to.window(driver.window_handles[1])

    sleep (10)

    # ENTRER DU TEXTE DANS LE LABEL PLANNING
    labelPlanning = driver.find_element(By.ID, d.dict_USMB["labelPlanning"])
    labelPlanning.send_keys("2-INFO-4")
    sleep(3)
    labelPlanning.sendKeys(Keys.ENTER)
