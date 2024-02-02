from os import system
import json
from modules.validate import noValid
from modules.data import baseDeDatos
import modules.campers as campers
import modules.trainers as trainers

system("clear")

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())

while True:

    print("""     _______________________________________
    |                                       |
    |   CRUD de Departamento Academico      |
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
            trainers.menu()
        case 0:
            system("clear")
            break
        case _:
            system("clear")
            noValid(opc)