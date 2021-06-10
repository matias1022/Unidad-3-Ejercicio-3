from ClaseInscripcion import Inscripcion
import numpy as np
import csv

class ManejadorInscripcion:
   __inscripciones=None
   __i=0
   def __init__(self,dimension=1):
        self.__inscripciones= np.empty(dimension, dtype=Inscripcion)
    
   def agregarInscripcion(self,inscripcion):
            self.__inscripciones[self.__i]=inscripcion
            self.__i+=1
            #print(unTaller)

   def buscarDNI(self):
        DNIbuscar=input("Ingresar DNI a buscar:")
        self.validarDNI(DNIbuscar)

   def validarDNI(self,dni):
        i=0
        encontrado=True
        while encontrado==True and i<len(self.__inscripciones):
            if self.__inscripciones[i].getDNI()==dni:
                print(self.__inscripciones[i].getNombreT())
                print(self.__inscripciones[i].getMonto())
                encontrado=False
            i+=1
        if encontrado==False:
            i=i-1
            return i            
   def listarDatos(self):
       Id=int(input("Ingresar Identificador de ID a buscar"))
       self.validarNum2(Id)


   def validarNum2(self,xnum):
        i=0
        s=""
        print("-----Inscriptos-----")
        while i<len(self.__inscripciones):
            if self.__inscripciones[i].getID()==xnum:
    
                    s+=self.__inscripciones[i].__str__() + '\n'
                
            i+=1
        print(s)      


   def pagar(self):
        dni=input("Ingresar DNI:")
        self.Pago(dni)


   def Pago(self,dni):
        i=0
        encontrado=True
        print(dni)
        while encontrado==True and i<len(self.__inscripciones):
            print(self.__inscripciones[i])
            if self.__inscripciones[i].getDNI()==dni:       
                 
                 self.__inscripciones[i].cambiarPago()
                 encontrado=False
                 print("El Pago fue hecho de forma correcta")
        i+=1

   def guardar(self):
        with open ("Inscripciones.csv","w",newline="") as ins:
             writer = csv.writer(ins,delimiter=",")
             for Inscripcion in self.__inscripciones:
                  if Inscripcion is not None:
                      writer.writerow([Inscripcion.getDNI(), Inscripcion.getID(),Inscripcion.getFecha(),Inscripcion.getPago()])



   def __str__(self):
        s=""
        for Inscripcion in self.__inscripciones:
           s+=Inscripcion.__str__() + '\n'
        return s 
   def mostrarInscripciones(self):
        for i in range (len(self.__inscripciones)):
         #    self.__talleres[i].mostrarDatos() 
              print(self.__inscripciones[i])