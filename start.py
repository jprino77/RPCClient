from __future__ import print_function

from send import enviar
 
from client import Service

import os


# Acciones para cada opcion.
def getNombreUsuarioFromId():
    print("\nHere's a bicycle. Have fun!\n")
    wait()
    
def crearUsuario():
    print("\nHere are some running shoes. Run fast!\n")
    wait()
    
def buscarFiliales():
    respuesta = enviar(Service.Client.buscarFiliales)

    if respuesta != None:
        print("|   id    |    Nombre          |   Calle   |   Altura   |")
        map(lambda filial: print("|   ",filial.id,"|   ",filial.nombre,"   |   ",filial.calle,"   |   ",filial.altura,"   |"),respuesta)
    wait()

def buscarDeporteByFilialId():
    print("\nHere's a map. Can you leave a trip plan for us?\n")
    wait()

def getFilialById():
    print("\nHere's a map. Can you leave a trip plan for us?\n")
    wait()

def getDeporteById():
    print("\nHere's a map. Can you leave a trip plan for us?\n")
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