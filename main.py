from os import system
from modules.validate import noValid
import modules.campers as campers
import modules.trainers as trainers
import modules.rutas as rutas

while True:
    system("clear")
    print("""     _______________________________________
    |                                       |
    |   CRUD de Departamento Academico      |
    |_______________________________________|
    """)
    print("\t1. Campers\n\t2. Trainers\n\t3. Asignacion\n\t4. Rutas de aprendizaje y modulos\n\t5. Planillas academicas\n\t0. Salir")
    opc = input()
 
    try:
        opc = int(opc)
        match(opc):
            case 1:
                system("clear")
                campers.menu()
            case 2:
                system("clear")
                trainers.menu()
            case 4:
                system("clear")
                rutas.menu()
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                noValid(opc)
    except ValueError:
        system("clear")
        noValid(opc)