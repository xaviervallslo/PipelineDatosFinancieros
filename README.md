# 📈 Fidelity Fund NAV Scraper

Script en Python que extrae automáticamente el NAV (valor liquidativo) y la fecha de un fondo de Fidelity ISIN IE00BYX5NX33 desde fuentes oficiales mediante webscraping , los normaliza al formato europeo y los almacena en un Excel histórico sin duplicar registros.

# ✨ Funcionalidades

* Obtiene el NAV y fecha desde la API oficial de Fidelity.
* Formatea:
  * Fecha → DD/MM/YYYY
  * Precio → coma decimal YY,YYYY
* Inserta el nuevo dato en la primera fila* del Excel.
* Evita duplicados por fecha. 
* Ideal para seguimiento histórico diario.

# ⏱️ Automatización diaria

Incluye un archivo .bat que permite ejecutar el script de Python automáticamente cada día a las 08:00, usando el programador de tareas de Windows (Task Scheduler).
Esto permite:
* Actualizar el NAV sin intervención manual.
* Mantener el Excel histórico siempre al día.
* Integración entornos Windows.

# 🛠️ Tecnologías
* Python
* requests
* pandas
* datetime
* Excel
* bat
* CMD

  
# 📂 Resultado
Archivo IE00BYX5NX33.xlsx con histórico ordenado y actualizado automáticamente.


