from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuration Selenium
chrome_options = Options()
chrome_service = Service("C:/chromedriver.exe")  # Mets ton chemin ici
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL de recherche d'emploi
search_url = "https://www.welcometothejungle.com/fr/jobs?query=python%20developer"
driver.get(search_url)
time.sleep(5)  # Attendre que la page charge

job_list = driver.find_elements(By.CSS_SELECTOR, "TON_SELECTEUR_ICI")
print(f"Nombre d'offres trouvées: {len(job_list)}")


driver.quit()
