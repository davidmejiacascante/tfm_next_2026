import pandas as pd
import requests
import time
import re
from datetime import datetime
import matplotlib.pyplot as plt

#keys necesarios para conectar con la API
#restriccion de 100 queries por mes

#url para buscar el codigo de la compañia
URL1 = "https://real-time-glassdoor-data.p.rapidapi.com/company-search"

#usaremos el "company_id:9079" que parece ser los headquaters de Google.
URL2 = "https://real-time-glassdoor-data.p.rapidapi.com/company-reviews"

HEADERS = {
	"x-rapidapi-key": "18961711b4mshb03fc723f71d161p11f4e3jsn9c90bfc62775",
	"x-rapidapi-host": "real-time-glassdoor-data.p.rapidapi.com"
}
COMPANIES = [
		['DELOITTE',2763],
		['MICROSOFT',1651],
		['INTEL',1519],
		['CISCO',1425],
		['APPLE',1138],
		['NORTHROP_GRUMMAN',488],
		['LOCKHEED_MARTIN',404],
		['IBM',354],
		['SAP',10471],
		['TP',9779],
		['GOOGLE',9079],
		['ACCENTURE',4138],
		['CAPGEMINI',3803],
		['FIDELITY_INVESTMENTS',2786]
]

BASE_PARAMS_2 = {
    "company_id": "9079",
    "sort": "MOST_RECENT",
    "language": "en",
    "only_current_employees": "false",
    "extended_rating_data": "false",
    "domain": "www.glassdoor.com"
}

BASE_PARAMS = {
    "sort": "MOST_RECENT",
    "language": "en",
    "only_current_employees": "false",
    "extended_rating_data": "false",
    "domain": "www.glassdoor.com"
}
KEY_WORDS = ['burnout','exhaustion','depersonalization','reduced personal accomplishment','negative feedback','stress','excessive workload','work overload','role overload','job demands–resources model','customer-related stressors','emotional labor','difficult client','workplace incivility','abuse','psychosocial','job strain','effort–reward imbalance','employee well-being','work-related mental health','burnout','toxic','miserable','hell','bad']

#Este metodo buscara los reviews de compañias en un maximo de las primeras 10 paginas. Esto debido a la restriccion de la API en la cantidad de llamados.

def fetch_recursive_reviews(company_id, start_page=1, max_pages=10):
    all_reviews = []
    page = start_page

    while page <= max_pages:
        params = {"company_id": str(company_id)} | BASE_PARAMS | {"page": str(page)}
        response2 = requests.get(URL2, headers=HEADERS, params=params)

        if response2.status_code != 200:
          print('Response code: ',response2.status_code)
          break

        tmp2 = response2.json()
        reviews = tmp2.get('data')
        if not reviews:
            break
        all_reviews.extend(reviews['reviews'])
        page += 1

        dft = pd.DataFrame(all_reviews)
        dft.to_csv(f"{str(COMPANIES[page][0])}_reviews.csv", index=False)
        time.sleep(1)

    return pd.DataFrame(all_reviews)

#Este metodo buscara en diferentes compañias los reviews.
def fetch_company_reviews(start_company=0, max_company=10):
    all_reviews = []
    page = start_company
    while page <= max_company:
      fetch_recursive_reviews(COMPANIES[page][1], start_page=1, max_pages=10)
      page += 1
      time.sleep(1)
    return pd.DataFrame(all_reviews)

fetch_company_reviews(start_company=0, max_company=10)