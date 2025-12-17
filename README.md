# 📈 Fidelity Fund NAV Scraper

Script en Python que **extrae automáticamente el NAV (valor liquidativo) y la fecha** de un fondo de Fidelity (ISIN `IE00BYX5NX33`) desde fuentes oficiales, los **normaliza al formato europeo** y los **almacena en un Excel histórico** sin duplicar registros.

# ✨ Funcionalidades

* Obtiene el *NAV y fecha* desde la API oficial de Fidelity.
* Formatea:
  * Fecha → DD/MM/YYYY
  * Precio → coma decimal 12,4299
* Inserta el nuevo dato en la *primera fila* del Excel.
* Evita **duplicados por fecha**.
* Ideal para seguimiento histórico diario.

⏱️ Automatización diaria

El proyecto incluye un archivo .bat que permite ejecutar el script de Python automáticamente cada día a las 08:00, pensado para su uso con el Programador de tareas de Windows.
Esto permite:
* Actualizar el NAV sin intervención manual.
* Mantener el Excel histórico siempre al día.
* Integración sencilla en entornos Windows.

# 🛠️ Tecnologías

* Python
* requests
* pandas
* datetime
* Excel
* bat
* CMD

  
# 📂 Resultado
Archivo `Historical_NAVs_IE00BYX5NX33.xlsx` con histórico ordenado y actualizado automáticamente.


