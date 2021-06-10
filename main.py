

from ClaseManejadorInscripcion import ManejadorInscripcion
from ClaseManejadorTalleres import ManejadorTalleres


if __name__ == '__main__':

      unManejadorTalleres=ManejadorTalleres()
      unManejadorTalleres.agregarTaller()#1
      unManejadorTalleres.mostrarTalleres()
      #print(ManejadorTalleres)
      cantidad=int(input("Ingresar la cantidad de inscriptos:"))
      listaInscripcion=ManejadorInscripcion(cantidad)
      for i in range(cantidad):
           unManejadorTalleres.inscrip(listaInscripcion)#2
      print(listaInscripcion)
      listaInscripcion.buscarDNI()#3
      listaInscripcion.listarDatos()#4
      listaInscripcion.pagar()#5
     # print(listaInscripcion)
      listaInscripcion.guardar()#6