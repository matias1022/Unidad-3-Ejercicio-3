from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
import numpy as np
from ClaseTallerCapacitacion import TallerCapacitacion
import csv


#talleres = np.empty(3, dtype=TallerCapacitacion)
#print(puntos)
class ManejadorTalleres:
    __talleres=None
    __i=0

    def __init__(self,dimension=5):
        self.__talleres= np.empty(dimension, dtype=TallerCapacitacion)
    
    def agregarTaller(self):
        archivo = open('talleres.csv')
        leer = csv.reader(archivo,delimiter=',')
        for fila in leer:
            idt=int(fila[0])
            nombre=fila[1]
            vacante=int(fila[2])
            monto=int(fila[3]) 
            unTaller = TallerCapacitacion(idt,nombre,vacante,monto)
            self.__talleres[self.__i]=unTaller
            self.__i+=1
            #print(unTaller)
        archivo.close()
    def inscrip(self,listaInscripcion):
        print("----Datos----")
        nombre=input("Ingresar Nombre:")    
        direccion=input("Ingresar Direccion:")
        dni=input("Ingresar DNI:")
        unaPersona=Persona(nombre,direccion,dni)  
        print(unaPersona)
        fecha=input("Ingresar Fecha de Inscripcion:")
        numeroTaller=int(input("Ingresar Numero de el taller:"))
        #SiONo=input("Ingresar si Pago(Si o No):")
        pago=False
        '''while pago==None:
              if SiONo=="si" or SiONo=="Si":
                 pago=True
                 print("Hola1")
              elif SiONo=="No" or SiONo=="no":
                  pago=False
                  print("Hola2")
              else:
                   print("La respuesta dada no es correcta") 
                   SiONo=(input("Pruebe nuevamente"))'''
        
        controlResta=self.restar(numeroTaller)
 
        if controlResta==True:
             i=self.validarNum(numeroTaller)
             unaInscripcion=Inscripcion(fecha,pago ,unaPersona,self.__talleres[i])
             #print(unaInscripcion)
             listaInscripcion.agregarInscripcion(unaInscripcion)
        else: print("El Numero de taller ha sido ingresado de forma incorrecta")

    def restar(self,num):
        band=False
        i=self.validarNum(num)
        if i!=None:
            self.__talleres[i].restVacante()
            print("Se ha restado el numero de talleres correctamente")
            band=True
        return band
    def validarNum(self,xnum):
        i=0
        print(xnum)
        encontrado=True
        while encontrado==True and i<len(self.__talleres):
            x=self.__talleres[i].getNumero()
            if x==xnum:
                encontrado=False
            i+=1
        if encontrado==False:
            i=i-1
            return i    
    




    def __str__(self):
        s=""
        for TallerCapacitacion in self.__talleres:
           s+=TallerCapacitacion.__str__() + '\n'
        return s 
    def mostrarTalleres(self):
        for i in range (len(self.__talleres)):
         #    self.__talleres[i].mostrarDatos() 
              print(self.__talleres[i])