import requests
import json
from funcion_html import iteracionHtml
from string import Template

# Este script, al hacerlo correr, genera el archivo avesdechile.html
# Para esto ocupa una función request_get que solicita
# data de una fuente API. Esta información que consiste en una lista
# se guarda en la variable out con formato json. Para limitar los registros
# de la lista, la variable out se filtra para que contengan solo 8 y
# esta nueva información se guarda en la varia photos.
# Al ser una lista, transformo iterando cada registro para que
# se despliegue como un formato de un fragmento de html que se repite.
# Este queda en formato string que se almacena en la variable card.
# Finalmente, creo una plantilla con la página web completa y utilizo 
# la función Template que he importado antes para el contenido de la variable
# del fragmento de las cards guardadas en la variable card se incruste como
# las etiquetas html. Esta accón se completa con el método substitute. Finalmente
# creo un archivo mediante with open. 

url = 'https://aves.ninjas.cl/api/birds'

html_template = Template('''
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title class="text-center">Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1 class="text-center mb-5 mt-5">Aves de Chile</h1>
    <div class="container d-flex justify-content-around flex-wrap">
        $body
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get(url)

photos = out[0:12]

card = iteracionHtml(photos)
    
final = html_template.substitute(body = card)


with open("avesdechile.html", "w", encoding='utf-8') as archivo_html:
    archivo_html.write(final)



