from os import system
from modules.validate import noValid
import modules.campers as campers

system("clear")
while True:

    print("""     _______________________________________
    |                                       |
    |   CRUM de Departamento Academico      |
    |_______________________________________|
    """)
    print("\t1. Campers\n\t2. Trainers\n\t0. Salir")
    opc = int(input())

    match(opc):
        case 1:
            system("clear")
            campers.menu()
        case 2:
            system("clear")
            print("\nTRAINERS")
            # TODO: This should redirect to the trainers CRUM
        case 0:
            system("clear")
            break
        case _:
            system("clear")
            noValid(opc)