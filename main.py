from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Configuration Selenium
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Mode sans interface
chrome_service = Service("C:/chromedriver.exe")  # Mets ton chemin ici
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL de recherche d'emploi
search_url = "https://www.welcometothejungle.com/fr/jobs?query=python%20developer"
driver.get(search_url)

# Attente explicite pour que la liste complète des offres soit chargée
try:
    job_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.sc-hyBbbR.ais-Hits-list"))
    )
    print("Page chargée avec succès.")
except Exception as e:
    print("Erreur lors du chargement de la page:", e)
    driver.quit()

# Récupération de tous les éléments <li> dans la liste
jobs_elements = job_list.find_elements(By.TAG_NAME, "li")
print("li récupérés")

jobs = []
for job in jobs_elements:
    try:
        title_element = job.find_element(By.CSS_SELECTOR, "div.sc-bXCLTC.sc-gMZepy.clOcbg")
        title = title_element.text if title_element else "Titre non disponible"
        entreprise_element = job.find_element(By.CSS_SELECTOR, "span.sc-fThUAz.jAWJFn.sc-fqbHDX.jsDoJd.wui-text")
        entreprise = entreprise_element.text if entreprise_element else "Entreprise non disponible"
        lieu_element = job.find_element(By.CSS_SELECTOR, "span.sc-cKccrX.fgMjGS")
        lieu = lieu_element.text if lieu_element else "Lieu non disponible"

        # Affichage des résultats pour vérifier
        print(f"Titre: {title}, Entreprise: {entreprise}, Lieu: {lieu}")
        
        jobs.append({"Titre": title,  "Entreprise": entreprise, "Lieu": lieu})
    except Exception as e:
        print("Erreur lors de l'extraction d'une offre:", e)
        continue

driver.quit()

# Sauvegarde des offres en CSV
df = pd.DataFrame(jobs)
df.to_csv("offres.csv", index=False, encoding='utf-8')
print("Scraping terminé, offres enregistrées dans 'offres.csv' !")
