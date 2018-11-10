from __future__ import print_function

from send import enviar
 
from client import Service

from client.ttypes import  Usuario

import os


# Acciones para cada opcion.
def getNombreUsuarioFromId():
    valido = False
    seleccion = 0
    while valido == False:
        try:
            seleccion = eval(raw_input("\nIngrese id a buscar: "))
            valido = True
        except:
            print('Id debe ser numerio')

    respuesta = enviar(Service.Client.getNombreUsuarioFromId, seleccion)

    if respuesta != None:
        print('Nombtre de usuario: ', respuesta)

    wait()
    
def crearUsuario():

    u = Usuario()
    
    u.nombre = raw_input("\nNombre: ")
    u.apellido =  raw_input("\nApellido: ")
    u.calle =  raw_input("\nCalle: ")
    
    valido = False
    while valido == False:
        try:
            altura = eval(raw_input("\nAltura: "))
            valido = True
        except:
            print('Altura debe ser numerio')

    u.altura = altura 

    valido = False
    while valido == False:
        try:
            localidad = eval(raw_input("\nLocalidad Id: "))
            valido = True
        except:
            print('Localidad debe ser numerio')
    u.localidad =  localidad
    u.telefono =  raw_input("\nTelefono: ")
    u.email =  raw_input("\nEmail: ")
    u.fechaNAcimiento =  raw_input("\nFecha Nacimiento: ")
    u.usuario =  raw_input("\nUsuario: ")
    u.clave =  raw_input("\nClave: ")

    respuesta = enviar(Service.Client.crearUsuario, u)
    if respuesta != None:
        print(respuesta)

    wait()
    
def buscarFiliales():
    respuesta = enviar(Service.Client.buscarFiliales)

    if respuesta != None:
        print("|   id    |    Nombre          |   Calle   |   Altura   |")
        map(lambda filial: print("|   ",filial.id,"|   ",filial.nombre,"   |   ",filial.calle,"   |   ",filial.altura,"   |"),respuesta)
    wait()

def buscarDeporteByFilialId():
    valido = False
    seleccion = 0

    while valido == False:
        try:
            seleccion = eval(raw_input("\nIngrese id a buscar: "))
            valido = True
        except:
            print('Id debe ser numerio')
    
    respuesta = enviar(Service.Client.buscarDeporteByFilialId, seleccion)

    if respuesta != None:
        
        print("|   id |    codigo |   descripcion   |")
        map(lambda deporte: print("|   ",deporte.id,"|   ",deporte.codigo,"|   ",deporte.descripcion,"   |"),respuesta)

    wait()

def getFilialById():
    valido = False
    seleccion = 0

    while valido == False:
        try:
            seleccion = eval(raw_input("\nIngrese id a buscar: "))
            valido = True
        except:
            print('Id debe ser numerio')
    
    respuesta = enviar(Service.Client.getFilialById, seleccion)

    if respuesta != None:
        
        print("\nId: ",respuesta.id,"\nNombre: ",respuesta.nombre,"\nCalle: ",respuesta.calle,"\nAltura: ", respuesta.altura)

    wait()

def getDeporteById():
    valido = False
    seleccion = 0

    while valido == False:
        try:
            seleccion = eval(raw_input("\nIngrese id a buscar: "))
            valido = True
        except:
            print('Id debe ser numerio')
    
    respuesta = enviar(Service.Client.getDeporteById, seleccion)

    if respuesta != None:
        
        print("\nId: ",respuesta.id,"\nCodigo: ",respuesta.codigo,"\nDescripcion: ",respuesta.descripcion)

    wait()

def wait():
    raw_input("Presione cualquier tecla para continuar...")

#Opciones de menu
def menu(argument):
    switcher = {
        '1': getNombreUsuarioFromId,
        '2': crearUsuario,
        '3': buscarFiliales,
        '4': buscarDeporteByFilialId,
        '5': getFilialById,
        '6': getDeporteById
    }
    # Obtengo opcion seleccionada, si no es ninguna arroja mensaje Opcion invalida
    func = switcher.get(argument, lambda: "Opcion Invalida")
    # Ejecuto Funcion
    func()

def main():
    
    

    seleccion = ''

    while seleccion != 'q':

        os.system('cls')  # on windows
        os.system('clear') #Linux
        print("\nQue Desea Hacer?")
        # Seleccion de opciones.
        print("\n[1] getNombreUsuarioFromId")
        print("[2] crearUsuario")
        print("[3] buscarFiliales")
        print("[4] buscarDeporteByFilialId")
        print("[5] getFilialById")
        print("[6] getDeporteById")
        print("[q] Salir.")
        
        # Elijo opcion de menu
        seleccion = raw_input("\nSeleccionar: ")
        if seleccion != 'q':
            menu(seleccion)
    
    os.system('cls')  # on windows
    os.system('clear') #Linux
    # Fin de la App
    print("Aplicacion Cerrada.")

if __name__ == "__main__":
    main()