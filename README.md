# prompts_generatorProject Prompt Generator
========================

Descripción:
------------
Este proyecto es una aplicación de escritorio desarrollada en Python que permite generar prompts 
para crear o modificar un software informático. La aplicación utiliza Tkinter y ttkbootstrap para su 
interfaz gráfica, y permite ingresar datos como contexto, objetivo, restricciones y formato de salida. 
Además, se puede seleccionar una carpeta de proyecto para generar y mostrar su estructura y código en el prompt.

Características:
----------------
- Interfaz gráfica amigable y personalizable.
- Permite ingresar varios parámetros para la generación de prompts.
- Opción para seleccionar una carpeta de proyecto para incluir su estructura y código en el prompt.
- Funcionalidades para copiar el prompt al portapapeles y guardarlo en un archivo.

Requisitos:
-----------
- Python 3.9 o superior (se ha probado con Python 3.13).
- Tkinter (incluido en la mayoría de las instalaciones de Python).
- ttkbootstrap (para la mejora de la interfaz).
- Pillow (PIL) para manejo de imágenes.

Para instalar las dependencias necesarias, ejecuta:
    pip install ttkbootstrap Pillow

Estructura del Proyecto:
------------------------
- main.py             : Archivo de entrada de la aplicación.
- gui/
    - app.py          : Código principal de la interfaz de usuario.
- config.py           : Configuración de constantes (nombre de la aplicación, dimensiones, colores, etc.).
- utils/
    - md_generator.py : Funciones para generar el reporte del proyecto y guardar el reporte.
- assets/
    - icons/
        - logo.png    : Logo personalizado que se utiliza en la aplicación, reemplazando el ícono por defecto de Tkinter.

Uso:
----
1. Ejecuta el archivo main.py:
       python main.py

2. En la ventana de la aplicación, ingresa los datos solicitados:
   - Contexto: Describe la situación o problema.
   - Objetivo: Define lo que se desea lograr.
   - Restricciones: Especifica las limitaciones o tecnologías a utilizar.
   - Formato de salida: Indica el formato deseado (por ejemplo, código, explicación, JSON, etc.).

3. (Opcional) Usa el botón "Seleccionar carpeta del proyecto" para elegir una carpeta. 
   La aplicación generará la estructura y el código del proyecto para incluirlo en el prompt.

4. Haz clic en "Generar Prompt" para crear el prompt final que integra todos los datos.
5. Usa el botón "Copiar" para copiar el prompt al portapapeles o "Guardar" para almacenarlo en un archivo.

Personalización:
-----------------
- Puedes modificar los parámetros de configuración (tamaño de ventana, color de fondo, etc.) en el archivo config.py.
- Para cambiar el logo, reemplaza el archivo "assets/icons/logo.png" por tu imagen preferida.

Licencia:
---------
Este proyecto se proporciona "tal cual" para fines educativos y de demostración. 
Puedes modificar y distribuir el código según tus necesidades.

Autor:
------
Desarrollado por Andrei Buga

Contacto: bugaandrei1@gmail.com
---------
Para cualquier consulta o sugerencia, puedes contactar a bugaandrei1@gmail.com.

¡Disfruta usando la aplicación y siéntete libre de contribuir!