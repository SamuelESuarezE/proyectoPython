from os import system
from modules.validate import noValid

def menu():
    while True:
        print("""         _______________________________________
        |                                       |
        |               TRAINERS                |
        |_______________________________________|
        """)
        print("\t1. Registrar Trainer\n\t2. Lista de Trainers\n\t3. Editar Trainer\n\t4. Eliminar Trainer\n\t0. Salir")
        opc = int(input())

        match(opc):
            case 1:
                system("clear")
                print("\nRegistro de Trainer")
                # TODO: This should let me register a Trainer
            case 2:
                system("clear")
                print("\nLista de Trainers")
                # TODO: This should let me see the list of Trainers
            case 3:
                system("clear")
                print("\nEditar Trainer")
                # TODO: This should let me edit a Trainer
            case 4:
                system("clear")
                print("\nEliminar Trainer")
                # TODO: This should let me delete a Trainer
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                noValid(opc)