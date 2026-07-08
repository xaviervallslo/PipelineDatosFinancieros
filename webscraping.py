# %%
import pandas as pd
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from bs4 import BeautifulSoup

import os
import pandas as pd
import requests

# %%

url = 'https://markets.ft.com/data/funds/tearsheet/summary?s=IE00BYX5NX33:EUR'
headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

# Valor NAV
valor = soup.find('span', class_='mod-ui-data-list__value').text.strip()

# Fecha NAV desde el disclaimer
disclaimer = soup.find('div', class_='mod-disclaimer').text.strip()
# Extraer la fecha después de "as of "
fecha = disclaimer.split('as of')[-1].strip() if 'as of' in disclaimer else 'No disponible'

# Reemplazar punto por coma
valor = str(valor).replace('.', ',')

#modificar fecha
from datetime import datetime

# Eliminar punto final si existe
fecha = fecha.strip().rstrip(".")

# Diccionario para traducir meses abreviados del español al inglés
meses_es_en = {
    "Ene": "Jan", "Feb": "Feb", "Mar": "Mar", "Abr": "Apr",
    "May": "May", "Jun": "Jun", "Jul": "Jul", "Ago": "Aug",
    "Sep": "Sep", "Oct": "Oct", "Nov": "Nov", "Dic": "Dec"
}

# Separar la fecha y traducir el mes si es necesario
partes = fecha.split()
mes = partes[0]
if mes in meses_es_en:
    partes[0] = meses_es_en[mes]

# Reconstruir la fecha en inglés
fecha_en = " ".join(partes)

# Convertir a datetime y formatear
fecha_dt = datetime.strptime(fecha_en, "%b %d %Y")
fecha_formateada = fecha_dt.strftime("%d/%m/%Y")


print(valor)
print(fecha)
print(fecha_formateada)

# %%

url = "https://www.fondosfidelity.es/api/ce/fdh/FundData.json?id=IE00BYX5NX33&countries=es&country=es&languages=es%2Cen&language=es&channels=ce.private-investor%2Cce.professional-investor&channel=ce.professional-investor&r=1761898675699"
headers = {"User-Agent": "Mozilla/5.0"}

# Solicitud
response = requests.get(url, headers=headers)
data = response.json()


# Extraer valor NAV
nav_value = data['IE00BYX5NX33']['priceData']['nav']['value']
nav_date = data['IE00BYX5NX33']['priceData']['nav']['date']

# Reemplazar punto por coma
nav_value = str(nav_value).replace('.', ',')

#modificar fecha
from datetime import datetime
fecha_dt = datetime.strptime(nav_date, "%Y-%m-%d")
fecha_formateada = fecha_dt.strftime("%d/%m/%Y")


#print 
print(nav_value)
print(nav_date)
print(fecha_formateada)



# %%


# %%

#captura datos del excel 
#archivo = r"C:\Users\d93150\Desktop\master\webscraping\IE00BYX5NX33.xlsx"
archivo = r"C:\Users\d93150\OneDrive - Mutuam\IE00BYX5NX33.xlsx"

df = pd.read_excel(archivo)

# Comprobar si la fecha ya existe
if fecha_formateada not in df['Fecha'].values:
    nueva_fila = {"Fecha": fecha_formateada, "Precio (EUR)": nav_value}
    df = pd.concat([pd.DataFrame([nueva_fila]), df]).reset_index(drop=True)


# Guardar
df.to_excel(archivo, index=False)


#pantalla
print(df)



