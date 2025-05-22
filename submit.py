import requests
import time
import random

# 1) Endpoint-ul de POST (din link-ul tău prefilled înlocuiește /viewform?… cu /formResponse)
url = 'https://docs.google.com/forms/d/e/1FAIpQLScL46YjnXjYfuXajrA3HJNTTB13LHACjylGiTw850Kzcl00kQ/formResponse'

# 2) Listele de opțiuni exact cum apar în Google Form
options_q1 = [
    "În niciun caz (0%)",
    "Foarte rar (≤25%)",
    "Ocazional (26-50%)",
    "Frecvent (51-75%)",
    "Permanent (>75%)"
]

options_q2 = [
    "Niciodată utilă",
    "Rar utilă",
    "Uneori utilă",
    "Foarte utilă",
    "Esențială"
]

options_q3 = [
    "Deloc deranjant",
    "Puțin deranjant",
    "Moderat deranjant",
    "Foarte deranjant",
    "Extrem de deranjant"
]

# 3) Trimit 50 de răspunsuri, fiecare cu valori alese aleator din liste
for i in range(50):
    payload = {
        'entry.952243539': random.choice(options_q1),  # Întrebarea 1
        'entry.536986570': random.choice(options_q2),  # Întrebarea 2
        'entry.1462098614': random.choice(options_q3)  # Întrebarea 3
    }
    r = requests.post(url, data=payload)
    print(f'[{i+1}/50] Status: {r.status_code} — '
          f'Q1="{payload["entry.952243539"]}", '
          f'Q2="{payload["entry.536986570"]}", '
          f'Q3="{payload["entry.1462098614"]}"')
    time.sleep(0.2)
