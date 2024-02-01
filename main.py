from os import system
from modules.validate import noValid

while True:

    print("""
     _______________________________________
    |                                       |
    |   CRUM de Departamento Academico      |
    |_______________________________________|
    """)
    print("\t1. Campers\n\t2. Trainers\n\t0. Salir")
    opc = int(input())

    match(opc):
        case 1:
            system("clear")
            print("\nCAMPERS")
            # TODO: This should redirect to the campers CRUM
        case 2:
            system("clear")
            print("\nTRAINERS")
            # TODO: This should redirect to the trainers CRUM
        case 0:
            system("clear")
            break
        case _:
            system("clear")
            noValid()