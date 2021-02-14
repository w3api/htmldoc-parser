import requests, os
from bs4 import BeautifulSoup
from elementos import ElementoHTML
import writer, json

URLBASE = "https://html.spec.whatwg.org/multipage/indices.html"
URLVERSIONES = "https://raw.githubusercontent.com/w3c/elements-of-html/master/elements.json"

def limpiar(cadena):
    return " ".join(cadena.split())

def get_versiones(versiones,nombre):

    for elemento in versiones:
        if nombre in elemento["element"]:
            return elemento["specs"]
    
    return ""


def todos_los_elementos():

    page = requests.get(URLBASE)
    soup = BeautifulSoup(page.content, 'html5lib')
    versiones_html = json.loads(requests.get(URLVERSIONES).text)


    ## Elementos y Atributos
    h3 = soup.find("h3", id="elements-3")    
    tabla_elementos = h3.find_next_sibling("table")
    cuerpo_elementos = tabla_elementos.find_next("tbody")
    elementos = cuerpo_elementos.find_all("tr")
    
    print ("Hay " + str(len(elementos)) + " HTML")
    for elemento in elementos:
        
        # Extraemos los datos
        nombre =  elemento.find("code").text
        atributos = limpiar(elemento.find_all("td")[4].text.replace("*","")).split(";")
        versiones = get_versiones(versiones_html,nombre)

        # Creamos el elemento HTML
        e = ElementoHTML()
        e.nombre = nombre
        
        for version in versiones:
            if 'X' in version:
                e.add_version(version.replace("X","xhtml "))
            else:
                e.add_version("html " + version)

        for atributo in atributos:
            if atributo != "globals":
                if not atributo.strip().startswith("on"):
                    e.add_atributo(atributo.strip())
                else:
                    e.add_evento(atributo.strip())
            else:
                e.activeGlobals()

        e.toString()

        writer.doc_elementoHTML(e)
        writer.doc_atributosHTML_generales()
    

    ## Eventos
    tabla_eventos = soup.find("table", id="ix-event-handlers")    
    cuerpo_elementos = tabla_eventos.find_next("tbody")
    eventos = cuerpo_elementos.find_all("th")
    
    print ("Hay " + str(len(eventos)) + " Eventos")

    for evento in eventos:        
        tipo_evento = limpiar(evento.find_next("td").text)
        if tipo_evento != "body":
            print (limpiar(evento.text))


print ("Analizando la documentación HTML")
todos_los_elementos()




