# 📈 Fidelity NAV Tracker — IE00BYX5NX33

Script en Python que extrae automáticamente el NAV (valor liquidativo) del fondo Fidelity con ISIN **IE00BYX5NX33**, lo normaliza al formato europeo y lo almacena en un Excel histórico sin duplicar registros. Incluye automatización diaria y dashboard en Power BI.

---

## ¿Qué hace?

- 🔗 Consulta la **API oficial de Fidelity España** como fuente principal de datos
- 🗓️ Formatea la fecha → `DD/MM/YYYY` con traducción automática de meses
- 💶 Formatea el precio → formato europeo con coma decimal `XX,XXXX €`
- 📥 Inserta el nuevo dato en la **primera fila del Excel**, ordenado de más reciente a más antiguo
- 🔒 **Anti-duplicados**: comprueba si la fecha ya existe antes de insertar
- ⚙️ Se ejecuta automáticamente cada día a las **08:00h** vía `.bat` + Task Scheduler de Windows

---

**Paso a paso:**

1. **Fidelity publica el NAV** cada día hábil con un día de retraso (D-1)
2. **El `.bat` lanza el script** automáticamente a las 08:00h via Task Scheduler
3. **El script llama a la API** de `fondosfidelity.es` y extrae el valor y la fecha
4. **Normaliza los datos** al formato europeo (coma decimal, fecha DD/MM/YYYY)
5. **Comprueba el Excel**: si la fecha no existe, inserta la fila al principio
6. **Guarda el Excel** con el nuevo registro incluido
7. **Power BI** lee el Excel actualizado y refleja el nuevo dato en el dashboard al refrescar

---

## 📂 Estructura del repositorio

| Archivo | Descripción |
|---|---|
| `webscraping.py` | Script principal de scraping y actualización del Excel |
| `webscraping.ipynb` | Notebook de desarrollo y exploración |
| `webscraping.bat` | Automatización diaria con Windows Task Scheduler |
| `IE00BYX5NX33.xlsx` | Histórico de NAV desde 2018 (+1.900 registros) |
| `IE00BYX5NX33.pbix` | Dashboard Power BI |

---

## 📊 Dashboard Power BI

El archivo `.pbix` conecta directamente con el Excel y muestra la evolución histórica del fondo desde 2018.

---

## 🛠️ Stack

`Python 3.12` · `requests` · `BeautifulSoup4` · `pandas` · `openpyxl` · `Excel` · `Power BI` · `Windows Task Scheduler`

---

## 🚀 Uso rápido

Instala las dependencias:

```bash
pip install requests pandas openpyxl beautifulsoup4
```

Edita la ruta del Excel en `webscraping.py`:

```python
archivo = r"C:\tu\ruta\IE00BYX5NX33.xlsx"
```

Ejecuta el script:

```bash
python webscraping.py
```

Para la automatización diaria, importa `webscraping.bat` en el **Programador de tareas de Windows** y configúralo para ejecutarse cada día a las 08:00h.

---

## 📌 Notas

- Los fondos publican el NAV con un día de retraso (D-1), por lo que el script siempre captura el dato del día anterior.
- Si mueves el Excel de ubicación, actualiza la ruta tanto en `webscraping.py` como en el origen de datos del `.pbix`.

