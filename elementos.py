
class ElementoHTML:

    nombre = ""
    atributosGlobals = False
    sintaxis = []
    categorias = []
    versiones = []
    atributos = []
    eventos = []
    
    def __init__(self):
        self.nombre = ""
        self.atributosGlobals = False
        self.sintaxis = []
        self.categorias = []
        self.versiones = []
        self.atributos = []
        self.eventos = []
        

    def nombre(self,nombre):
        self.nombre = nombre
    
    def add_sintaxis(self,sintaxis):
        self.sintaxis.append(sintaxis)

    def add_categoria(self,categoria):
        self.categorias.append(categoria)

    def add_version(self,version):
        self.versiones.append(version)

    def add_atributo(self,atributo):
        self.atributos.append(atributo)

    def add_enumerado(self,enumerado):
        self.enumerados.append(enumerado)

    def add_elemento(self,elemento):
        self.elementos.append(elemento)

    def add_evento(self,evento):
        self.eventos.append(evento)

    def activeGlobals(self):
        self.atributosGlobals = True

    def toString(self):
        print("Nombre: " + self.nombre)
        print("Globals: " + str(self.atributosGlobals))
        print("Atributos: ")
        for atributo in self.atributos:
            print(">> " + atributo)
        print("Eventos: ")
        for evento in self.eventos:
            print(">> " + evento)


    def getGlobals():
        return ["accesskey","autocapitalize","autofocus","contenteditable","dir","draggable","enterkeyhint","hidden","inputmode","is","itemid","itemprop","itemref","itemscope","itemtype","lang","nonce","spellcheck","style","tabindex","title","translate"]