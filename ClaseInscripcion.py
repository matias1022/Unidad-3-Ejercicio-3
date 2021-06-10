from ClasePersona import Persona
import datetime

class Inscripcion:
    __fechaInscripcion= None
    __pago:bool
    __persona=None
    __taller=None

    def __init__(self,fechaInscripcion=None,pago=False,persona=None,taller=None):
        self.__fechaInscripcion=fechaInscripcion
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller
    def cambiarPago(self):
        self.__pago=True
    def getPago(self):
        return self.__pago
    def getDNI(self):
        dni=self.__persona.getdni()
        return dni
    def getNombreT(self):
        nombre=self.__taller.getNombre()
        return nombre
    def getMonto(self):
        monto=self.__taller.getMont()
        return monto
    def getID(self):
        id=self.__taller.getID()
        return id
    def getFecha(self):
        return self.__fechaInscripcion
    def __str__(self):
        if self.__pago:
            pago="Si"
        else:
            pago='No'

        s=f'{self.__fechaInscripcion},{pago},{self.__taller}'
        s+= "\nPersona:"+ self.__persona.__str__()
        return s