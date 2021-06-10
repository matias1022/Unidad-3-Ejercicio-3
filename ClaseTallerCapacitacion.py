from numpy.core.numeric import identity


class TallerCapacitacion:
    idTaller=0
    nombre=""
    vacantes=0
    montoInscripcion=0
    #cantidad=0
    def __init__(self,idTaller=0,nombre="",vacantes=0,montoInscripcion=0):
        self.__idTaller=idTaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=montoInscripcion
    
    def restVacante(self):
        self.__vacantes= self.__vacantes-1
    def getNumero(self):
        return self.__idTaller
    def getMont(self):
        return self.__montoInscripcion
    def getNombre(self):
        return self.__nombre
    def getID(self):
        return self.__idTaller
    def __str__(self):
        return f"{self.__idTaller},{self.__nombre},{self.__vacantes},{self.__montoInscripcion}"
    def mostrarDatos(self):
       print (f"{self.__idTaller},{self.__nombre},{self.__vacantes},{self.__montoInscripcion}")