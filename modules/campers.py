from os import system
from modules.validate import noValid

def menu():
    while True:
        print("""         _______________________________________
        |                                       |
        |                CAMPERS                |
        |_______________________________________|
        """)
        print("\t1. Registrar Camper\n\t2. Lista de Campers\n\t3. Editar Camper\n\t4. Eliminar Camper\n\t0. Salir")
        opc = int(input())

        match(opc):
            case 1:
                system("clear")
                print("\nRegistro de camper")
                # TODO: This should let me register a camper
            case 2:
                system("clear")
                print("\nLista de campers")
                # TODO: This should let me see the list of campers
            case 3:
                system("clear")
                print("\nEditar Camper")
                # TODO: This should let me edit a camper
            case 4:
                system("clear")
                print("\nEliminar Camper")
                # TODO: This should let me delete a camper
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                noValid(opc)