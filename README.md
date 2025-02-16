# 🚀 Job Scraper - Scraper d'offres d'emploi avec Selenium par Tom Leclercq

Un script Python permettant de scraper les offres d'emploi de **Welcome to the Jungle** en utilisant **Selenium** et **pandas**. 📊  

🔍 **Fonctionnalités :**  
✔️ Scrape **toutes les annonces disponibles** sur une recherche spécifique  
✔️ Extraction du **titre du poste, nom de l'entreprise, lieu, lien vers l'annonce** et sauvegarde en CSV  
✔️ Attente dynamique pour un **scraping plus robuste**  
✔️ 📂 Fichier CSV exporté : `offres.csv`, possibilité de l'intégrer dans Excel, Google Sheets 

---

## 📌 Installation & Prérequis  

### 1️⃣ **Cloner le repo**  
```bash
git clone https://github.com/Tominouu/job-scraper.git
cd job-scraper
```

### 2️⃣ **Créer un environnement virtuel** (optionnel)  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Installer les dépendances**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Télécharger ChromeDriver** (compatible avec ta version de Chrome)  
- Vérifie ta version Chrome :  
  👉 **`chrome://settings/help`** dans la barre d’URL  
- Télécharge le bon `chromedriver.exe` ici :  
  👉 [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)  
- Place-le dans le dossier du script et ajuste le chemin dans `main.py`  

---

## ⚡️ Utilisation  
Lance le script avec :  
```bash
python main.py
```
Les offres seront extraites et enregistrées dans **`offres.csv`** 📄

Pour plus de confort je te conseilles de le lancer depuis le terminal🚀

Penses bien à te rendre dans le bon dossier, puis exécute le programme
```bash
cd C:/Exemple/leNomDeTonDossier
```
```bash
python main.py
```

---

## 🛠️ Configuration  
Suis les questions que te poses le programme après exécution  

---

## 📊 Résultat attendu  
Un fichier CSV avec une structure comme ceci :  

| Titre |
|---------------------------|
| Développeur Python - CDI |
| Ingénieur Back-End Python |
| Lead Developer Python     |

---

## 📌 Améliorations futures 🏗️  
🔹 Ajouter la récupération des entreprises et des liens 🔗  
🔹 Support multi-pages pour scraper plus d'annonces 📄  
🔹 Exportation JSON en plus du CSV  
🔹 Intégration web

---

🚀 *Bon Scraping!*  
🐍 **Fait avec Python & Selenium** ❤️

