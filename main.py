from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Configuration Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Mode sans interface
chrome_service = Service("chemin/vers/chromedriver")  # Mets ton chemin ici
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL de recherche d'emploi
search_url = "https://www.welcometothejungle.com/fr/jobs?query=python%20developer"
driver.get(search_url)
time.sleep(5)  # Attendre le chargement de la page

# Récupération des offres
job_list = driver.find_elements(By.CSS_SELECTOR, "div.sc-1kkiraj-0")

jobs = []
for job in job_list:
    try:
        title = job.find_element(By.CSS_SELECTOR, "h3").text
        company = job.find_element(By.CSS_SELECTOR, "span.sc-16r5pdw-0").text
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        jobs.append({"Titre": title, "Entreprise": company, "Lien": link})
    except:
        continue

driver.quit()

# Sauvegarde des offres en CSV
df = pd.DataFrame(jobs)
df.to_csv("offres.csv", index=False)
print("Scraping terminé, offres enregistrées !")
