from os import system
from .validate import noValid
import json

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]
    trainersList = baseDeDatos["trainers"]
    rutasList = baseDeDatos["rutas"]
    modulosList = baseDeDatos["modulos"]

def menu():
    print("""
      __   ____  __  ___  __ _   __    ___  __  __   __ _ 
     / _\ / ___)(  )/ __)(  ( \ / _\  / __)(  )/  \ (  ( \\
    /    \\\___ \ )(( (_ \/    //    \( (__  )((  O )/    /
    \_/\_/(____/(__)\___/\_)__)\_/\_/ \___)(__)\__/ \_)__)
    """)
    print("\t1. Registrar prueba de admision\n\t2. Matricula\n\t0. Salir")
    opc = input()

    try:
        opc = int(opc)
        match(opc):
            case 1:
                system("clear")
                pruebaDeAdmision()
            case 2:
                system("clear")
    except ValueError:
        noValid(opc)

def pruebaDeAdmision():
    print("""     _______________________________________
    |                                       |
    |          PRUEBA DE ADMISION           |
    |_______________________________________|
    """)
