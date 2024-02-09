from os import system
from modules.validate import noValid
import modules.campers as campers
import modules.trainers as trainers
import modules.rutas as rutas
import modules.asignacion as asignacion
import modules.registerPrueba as prueba
import modules.calificarPrueba as calificarprueba
import modules.reportes as reportes

system("clear")
while True:
    print("\33[0;32m"+"""
     ____  ____  ____       __    ___   __   ____  ____  _  _  __  ___  __  
    (    \(  __)(  _ \     / _\  / __) / _\ (    \(  __)( \/ )(  )/ __)/  \ 
     ) D ( ) _)  ) __/_   /    \( (__ /    \ ) D ( ) _) / \/ \ )(( (__(  O )
    (____/(____)(__) (_)  \_/\_/ \___)\_/\_/(____/(____)\_)(_/(__)\___)\__/ 
    """+"\33[0;m")
    print("\t1. Campers 🚀\n\t2. Trainers 🖥️\n\t3. Asignacion ✍️\n\t4. Rutas de aprendizaje y modulos 🗺️\n\t5. Registro de prueba de admision 🧾\n\t6. Calificar modulo a camper 📝\n\t7. Reportes 📋\n\t0. Salir 🚪")
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
            case 3:
                system("clear")
                asignacion.menu()
            case 4:
                system("clear")
                rutas.menu()
            case 5:
                system("clear")
                prueba.menu()
            case 6:
                system("clear")
                calificarprueba.menu()
            case 7:
                system("clear")
                reportes.menu()
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                noValid(opc)
    except ValueError:
        system("clear")
        noValid(opc)

print("""
  ____  _  _  __  ____  ____  ____    ____  _  _   ___  ___  ____  ____  ____  _  _  __    __    _  _ 
 (  __)( \/ )(  )(_  _)(  __)(    \  / ___)/ )( \ / __)/ __)(  __)/ ___)(  __)/ )( \(  )  (  )  ( \/ )
  ) _)  )  (  )(   )(   ) _)  ) D (  \___ \) \/ (( (__( (__  ) _) \___ \ ) _) ) \/ (/ (_/\/ (_/\ )  / 
 (____)(_/\_)(__) (__) (____)(____/  (____/\____/ \___)\___)(____)(____/(__)  \____/\____/\____/(__/  
""")