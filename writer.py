from datetime import datetime
import os, html, json


__OUT__ = "/Users/victor/GitHub/w3api-dev/_posts/html/"
__OUTJSON__ = "/Users/victor/GitHub/w3api-dev/_data/HTML/"
__atributosGlobales__ = ['accesskey','autocapitalize','autofocus','contenteditable','dir','draggable','enterkeyhint','hidden','inputmode','is','itemid','itemprop','itemref','itemscope','itemtype','lang','nonce','spellcheck','style','tabindex','title','translate']

def doc_JSON(elemento):

    basepath = elemento.nombre

    if not os.path.exists(__OUTJSON__ + elemento.nombre[0]):
        os.makedirs(__OUTJSON__ + elemento.nombre[0])

    # Clases como AbstractDocument.AttributeContext se generan en un directorio
    f = open(__OUTJSON__ + elemento.nombre[0] + "/" + basepath + ".json","w")

    data_json = {}
    data_json["description"] = ""
    data_json["code"] = ""
    data_json["ldc"] = []

    if elemento.atributos:
        a = []
        for atributo in elemento.atributos:
            atributo_json = {}
            atributo_json["nombre"] = atributo
            atributo_json["description"] = ""
            atributo_json["code"] = ""
            atributo_json["ldc"] = []
            a.append(atributo_json)
        data_json["atributos"] = a

    if elemento.eventos:
        ev = []
        for atributo in elemento.eventos:
            evento_json = {}
            evento_json["nombre"] = atributo
            evento_json["description"] = ""
            evento_json["code"] = ""
            evento_json["ldc"] = []
            ev.append(evento_json)
        data_json["eventos"] = ev

    f.write(json.dumps(data_json,indent=4))
    f.close()

def doc_JSON_Globales(nombre):

    basepath = nombre

    if not os.path.exists(__OUTJSON__ + nombre[0]):
        os.makedirs(__OUTJSON__ + nombre[0])

    # Clases como AbstractDocument.AttributeContext se generan en un directorio
    f = open(__OUTJSON__ + nombre[0] + "/" + basepath + ".json","w")

    data_json = {}
    data_json["description"] = ""
    data_json["code"] = ""
    data_json["ldc"] = []

    f.write(json.dumps(data_json,indent=4))
    f.close()

## Genera los ficheros desde una clase
def gen_cabecera(nombre,path,clave,tags):

    c = ["---" + "\n",
                "title: " + nombre + "\n",
                "permalink: " + path + "\n",
                "date: " + str(datetime.now()) + "\n",
                "key: " + clave + "\n",
                "category: html" + "\n",
                "tags: " + str(tags) + "\n",
                "sidebar: " + "\n",
                "  nav: html" + "\n",
                "---" + "\n\n"]
    return c

def gen_cabecera_tag(tipo, nombre, titulo):

    c = ["---" + "\n",
                "title: \"" + titulo + " " + nombre + "\"\n",
                "layout: tag\n",
                "permalink: /html/tag/" + nombre + "/\n",
                "date: " + str(datetime.now()) + "\n",
                "key: " + tipo + nombre + "\n",
                "sidebar: " + "\n",
                "  nav: java" + "\n",
                "aside: " + "\n",
                "  toc: true" + "\n",
                "pagination: " + "\n",
                "  enabled: true" + "\n",
                "  tag: \"" + nombre + "\"\n",
                "  permalink: /:num/" + "\n",
                "---" + "\n\n"]
    return c

def gen_sintaxis(sintaxis):

    s = ["## Sintaxis\n",
          "~~~html\n"]
    for sin in sintaxis:
         s.append(sin + "\n")
    s.append("~~~\n\n")
    return s

def gen_ldc(clave):
    ldc = ["## Artículos\n",
           "<ul>\n",
            "{%- for _ldc in " + clave + ".ldc -%}\n",
            "   <li>\n",
                "       <a href=\"{{_ldc['url'] }}\">{{ _ldc['nombre'] }}</a>\n",
            "   </li>\n",
            "{%- endfor -%}\n",
          "</ul>\n"]
    return ldc

def gen_ejemplo(base):

    e = ["## Ejemplo\n"
         "~~~java\n",
         "{{ " + base + ".code}}\n",
         "~~~\n\n",
         ]
    return e

def gen_descripcion(base):
    d = ["## Descripción\n",
         "{{" + base + ".description }}\n\n"
         ]
    return d

def gen_atributos(atributos,nombre):
    a = ["## Atributos\n"]
    for atributo in atributos:
        a.append("* [" + atributo + "](/html/" + nombre + "/" + atributo + "/)\n")
    a.append("\n")
    return a

def gen_atributos_globales(): 
    a = ["## Atributos Globales\n"]
    for atributo in __atributosGlobales__:
        a.append("* [" + atributo + "](/html/" + atributo + "/)\n")
    a.append("\n")
    return a

def gen_eventos(eventos,nombre):
    e = ["## Eventos\n"]
    for evento in eventos:
        e.append("* [" + evento + "](/html/" + nombre + "/" + evento + "/)\n")
    e.append("\n")
    return e


def gen_clasepadre(nombre,path):
    cp = ["## Elemento Padre\n",
          "[" + nombre + "](/html/"+ path.replace(".","/") + "/)\n\n"]

    return cp

def gen_infometodo(clave,tipo,valor):
    bm = ["{% include w3api/datos.html clase=site.data." + clave + "." + tipo + " valor=\"" + valor +"\" %}\n\n"]
    return bm

def doc_atributosHTML(e):

    basepath = e.nombre

    for atributo in e.atributos:

            f = open(__OUT__ + e.nombre[0] + "/" + basepath + "/2021-01-01-" + e.nombre + "." + atributo + ".md","w")
            clave = "HTML."+e.nombre[0]+"."+basepath + "." + atributo
            path = "/html/"+basepath.replace(".","/") + "/" + atributo + "/"
            jsonsource = "HTML."+e.nombre[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
            nombre = e.nombre + "." + atributo

            tags = []
            tags.append("atributo html")

            #for version in e.versiones:
            #    tags.append(version)
            
            cabecera = gen_cabecera(nombre,path,clave,tags)
            f.writelines(cabecera)

            info_metodo = gen_infometodo(jsonsource,"atributos",atributo)
            f.writelines(info_metodo)

            descripcion = gen_descripcion("_dato")
            f.writelines(descripcion)

            sintaxis = gen_sintaxis("")
            f.writelines(sintaxis)

            clase_padre = gen_clasepadre(e.nombre,basepath)
            f.writelines(clase_padre)

            ejemplo = gen_ejemplo("_dato")
            f.writelines(ejemplo)

            ldc = gen_ldc("_dato")
            f.writelines(ldc)

            f.close()

def doc_eventosHTML(e):

    basepath = e.nombre

    for evento in e.eventos:

            f = open(__OUT__ + e.nombre[0] + "/" + basepath + "/2021-01-01-" + e.nombre + "." + evento + ".md","w")
            clave = "HTML."+e.nombre[0]+"."+basepath + "." + evento
            path = "/html/"+basepath.replace(".","/") + "/" + evento + "/"
            jsonsource = "HTML."+e.nombre[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
            nombre = e.nombre + "." + evento

            tags = []
            tags.append("evento html")

            #for version in e.versiones:
            #    tags.append(version)
            
            cabecera = gen_cabecera(nombre,path,clave,tags)
            f.writelines(cabecera)

            info_metodo = gen_infometodo(jsonsource,"eventos",evento)
            f.writelines(info_metodo)

            descripcion = gen_descripcion("_dato")
            f.writelines(descripcion)

            sintaxis = gen_sintaxis("")
            f.writelines(sintaxis)

            clase_padre = gen_clasepadre(e.nombre,basepath)
            f.writelines(clase_padre)

            ejemplo = gen_ejemplo("_dato")
            f.writelines(ejemplo)

            ldc = gen_ldc("_dato")
            f.writelines(ldc)

            f.close()

def doc_atributosHTML_generales():

    for atributo in __atributosGlobales__:

            basepath = atributo

            if not os.path.exists(__OUT__ + basepath[0] + "/" + basepath + "/"):
                os.makedirs(__OUT__ + basepath[0] + "/" + basepath + "/")

            f = open(__OUT__ + basepath[0] + "/" + basepath + "/2021-01-01-" + basepath + ".md","w")
            clave = "HTML."+basepath[0]+"."+basepath 
            path = "/html/"+basepath.replace(".","/") + "/" 
            jsonsource = "HTML."+basepath[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
            nombre = basepath

            tags = []
            tags.append("atributo html")
            
            cabecera = gen_cabecera(nombre,path,clave,tags)
            f.writelines(cabecera)

            descripcion = gen_descripcion("site.data." + jsonsource)
            f.writelines(descripcion)

            sintaxis = gen_sintaxis("")
            f.writelines(sintaxis)

            ejemplo = gen_ejemplo("site.data." + jsonsource)
            f.writelines(ejemplo)

            ldc = gen_ldc("site.data." + jsonsource)
            f.writelines(ldc)

            f.close()

            doc_JSON_Globales(atributo)

def doc_eventosHTML_generales(eventos):

    for evento in eventos:

            basepath = evento

            if not os.path.exists(__OUT__ + basepath[0] + "/" + basepath + "/"):
                os.makedirs(__OUT__ + basepath[0] + "/" + basepath + "/")

            f = open(__OUT__ + basepath[0] + "/" + basepath + "/2021-01-01-" + basepath + ".md","w")
            clave = "HTML."+basepath[0]+"."+basepath 
            path = "/html/"+basepath.replace(".","/") + "/" 
            jsonsource = "HTML."+basepath[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
            nombre = basepath

            tags = []
            tags.append("evento html")
            
            cabecera = gen_cabecera(nombre,path,clave,tags)
            f.writelines(cabecera)

            descripcion = gen_descripcion("site.data." + jsonsource)
            f.writelines(descripcion)

            sintaxis = gen_sintaxis("")
            f.writelines(sintaxis)

            ejemplo = gen_ejemplo("site.data." + jsonsource)
            f.writelines(ejemplo)

            ldc = gen_ldc("site.data." + jsonsource)
            f.writelines(ldc)

            f.close()

            doc_JSON_Globales(evento)


def doc_elementoHTML(e):


    basepath = e.nombre

    if not os.path.exists(__OUT__ + e.nombre[0] + "/" + basepath + "/"):
        os.makedirs(__OUT__ + e.nombre[0] + "/" + basepath + "/")

    f = open(__OUT__ + e.nombre[0] + "/" + basepath + "/2021-01-01-" + e.nombre + ".md","w")
    clave = "HTML."+e.nombre[0]+"."+basepath
    jsonsource = "HTML."+e.nombre[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
    path = "/html/"+basepath.replace(".","/")+"/"

    tags = []
    tags.append("elemento html")
     
    for version in e.versiones:
        tags.append(version)

    cabecera = gen_cabecera(e.nombre,path,clave, tags)
    f.writelines(cabecera)

    descripcion = gen_descripcion("site.data." + jsonsource)
    f.writelines(descripcion)

    sintaxis = gen_sintaxis(e.sintaxis)
    f.writelines(sintaxis)

    if e.atributos:
        atributos = gen_atributos(e.atributos,basepath)
        f.writelines(atributos)

    if e.atributosGlobals:
        atributosGlobales = gen_atributos_globales()
        f.writelines(atributosGlobales)

    if e.eventos:
        eventos = gen_eventos(e.eventos,basepath)
        f.writelines(eventos)

    ejemplo = gen_ejemplo("site.data." + jsonsource)
    f.writelines(ejemplo)

    ldc = gen_ldc("site.data." + jsonsource)
    f.writelines(ldc)


    f.close()

    if e.atributos:
        doc_atributosHTML(e)

    if e.eventos:
        doc_eventosHTML(e)

    doc_JSON(e)