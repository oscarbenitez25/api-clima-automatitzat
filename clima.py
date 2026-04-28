import requests
import json
from datetime import datetime

# a. Obtenir dades de l'API (Barcelona: lat 41.38, lon 2.15)
url = "https://api.open-meteo.com/v1/forecast?latitude=41.3888&longitude=2.159&hourly=temperature_2m"
response = requests.get(url)
dades = response.json()

# Obtenim la llista de temperatures de les darreres 24 hores
temperatures = dades['hourly']['temperature_2m'][:24]

# b. Càlculs manuals (NO usar l'API per a això)
temp_max = max(temperatures)
temp_min = min(temperatures)
temp_mitjana = sum(temperatures) / len(temperatures)

# c. Exportar a JSON amb la data actual
data_avui = datetime.now().strftime("%Y%m%d")
nom_fitxer = f"temp_{data_avui}.json"

resultats = {
    "data": datetime.now().strftime("%Y-%m-%d"),
    "maxima": temp_max,
    "minima": temp_min,
    "mitjana": round(temp_mitjana, 2)
}

with open(nom_fitxer, 'w') as f:
    json.dump(resultats, f, indent=4)

print(f"Fitxer {nom_fitxer} creat correctament.")