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

query = input("Entrez la query pour la recherche d'emploi (par exemple, 'python developer'): ")
lieu = input("Entrez le lieu pour la recherche d'emploi (par exemple, 'Paris'): ")
radius = input("Entrez le rayon de recherche (par exemple, '10km'): ")
contract = input("Entrez le type de contrat (par exemple, 'internship=stage, apprenticeship=alternance, full_time=CDI'): ")
search_url = f"https://www.welcometothejungle.com/fr/jobs?query={query.replace(' ', '%20')}&refinementList%5Boffices.country_code%5D%5B%5D=FR&page=1&aroundLatLng=44.84044%2C-0.5805&contract_type%5D%5B%5D={contract.replace(' ', '%20')}&aroundRadius={radius.replace(' ', '%20')}&aroundQuery={lieu.replace(' ', '%20')}"
#search_url = f"https://www.welcometothejungle.com/fr/jobs?query={query.replace(' ', '%20')}"
#search_url = "https://www.welcometothejungle.com/fr/jobs?query=python%20developer"
driver.get(search_url)

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
        lien_element = job.find_element(By.CSS_SELECTOR, "a.sc-dnvZjJ.dhlcJw")
        lien = lien_element.get_attribute("href") if lien_element else "Lien non disponible"

        # Affichage des résultats pour vérifier
        print(f"Titre: {title}, Entreprise: {entreprise}, Lieu: {lieu}, Lien: {lien}")
        
        jobs.append({"Titre": title,  "Entreprise": entreprise, "Lieu": lieu, "Lien": lien})
    except Exception as e:
        print("Erreur lors de l'extraction d'une offre:", e)
        continue

driver.quit()

# Sauvegarde des offres en CSV
df = pd.DataFrame(jobs)
df.to_csv("offres.csv", index=False, encoding='utf-8')
print("Scraping terminé, offres enregistrées dans 'offres.csv' !")
