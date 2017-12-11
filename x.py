# -*- coding: utf-8 -*-
"""
Decodificar y Codificar en un solo script usando base64 en python
"""
import base64 # Importamos la librería base64 de python

# Paso de la decodificación

with open("1.png", "rb") as f: # Leemos la imagen que vamos a decodificar.
    data = f.read()
    data1 = data.encode("base64") # Decodificamos a base64 la imagen.
    print data1 # cadena de texto ASCII que es la imagen decodificada para visualizarla.

    # Paso de la codificación

    imgdata = base64.b64decode(data1) # Codificamos la cadena de caracteres.
    filename = '2.png' # Imagen codificada a partir de la cadena de texto ASCII que es la imagen decodificada.
    with open(filename, 'wb') as f: # Asignamos un nombre a la nueva imagen.
        f.write(imgdata) # Creamos la imagen y la guardamos en el directorio del script.
