from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Configuration Selenium
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Mode sans interface
chrome_service = Service("C:/chromedriver.exe")  # Mets ton chemin ici
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL de recherche d'emploi
search_url = "https://www.welcometothejungle.com/fr/jobs?query=python%20developer"
driver.get(search_url)

# Attente explicite pour que les résultats de recherche soient chargés
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.sc-hyBbbR.bFHmuL.ais-Hits-list"))
    )
    print("Page chargée avec succès.")
except Exception as e:
    print("Erreur lors du chargement de la page:", e)
    driver.quit()

# Récupération des offres
job_list = driver.find_elements(By.CSS_SELECTOR, "ul.sc-hyBbbR.bFHmuL.ais-Hits-list")

jobs = []
for job in job_list:
    try:
        title = job.find_element(By.CSS_SELECTOR, "div.sc-bXCLTC.sc-gMZepy.clOcbg").text
        # Affiche les informations extraites pour vérification
        print(f"Titre: {title}")
        
        jobs.append({"Titre": title})
    except Exception as e:
        print("Erreur lors de l'extraction d'une offre:", e)
        continue

driver.quit()

# Sauvegarde des offres en CSV
df = pd.DataFrame(jobs)
df.to_csv("offres.csv", index=False)
print("Scraping terminé, offres enregistrées dans 'offres.csv' !")
