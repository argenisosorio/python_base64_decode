# -*- coding: utf-8 -*-
"""
Codificar y Decodificar en un solo script usando base64 en python
"""
import base64 # Importamos la librería base64 de python

# Paso de la codificación

with open("1.png", "rb") as f: # Leemos la imagen que vamos a codificar.
    data = f.read()
    data1 = data.encode("base64") # Codificamos a base64 la imagen.
    print data1 # Cadena de texto ASCII que es la imagen codificada, imprimimos por pantalla para ver la cadena de caracteres.

    # Paso de la decodificación

    imgdata = base64.b64decode(data1) # Decodificamos la cadena de caracteres.
    filename = '2.png' # Imagen decodificada a partir de la cadena de texto ASCII que es la imagen codificada.
    with open(filename, 'wb') as f: # Asignamos un nombre a la nueva imagen.
        f.write(imgdata) # Creamos la imagen y la guardamos en el directorio del script.
