from os import system
from .validate import noValid
import json

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]
    trainersList = baseDeDatos["trainers"]
    rutasList = baseDeDatos["rutas"]
    modulosList = baseDeDatos["modulos"]
    salasList = baseDeDatos["salas"]

def mostrarRutas():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        rutasList = baseDeDatos["rutas"]
    
    print("Digite codigo de ruta:")
    for ruta in rutasList:
        print(f"\t{ruta.get('Codigo')}. {ruta.get('Nombre')}")
    rutaSeleccionada = input()

    for ruta in rutasList:
        if ruta.get("Codigo") == rutaSeleccionada:
            return ruta.get("Codigo")

def menu():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
        trainersList = baseDeDatos["trainers"]
        rutasList = baseDeDatos["rutas"]
        modulosList = baseDeDatos["modulos"]
        salasList = baseDeDatos["salas"]
    print("""
      __   ____  __  ___  __ _   __    ___  __  __   __ _ 
     / _\ / ___)(  )/ __)(  ( \ / _\  / __)(  )/  \ (  ( \\
    /    \\\___ \ )(( (_ \/    //    \( (__  )((  O )/    /
    \_/\_/(____/(__)\___/\_)__)\_/\_/ \___)(__)\__/ \_)__)
    """)
    
    id = input("Ingrese el documento del camper que desea asignar: ")
    
    for camper in campersList:
        if camper.get("ID") == id:
            info = {
                "CodigoRuta": mostrarRutas(),
                "CodigoSala": input("Digite el codigo de la sala:\n\t1. Sputnik\n\t2. Apolo\n\t3. Artemis\nEscriba el codigo de la sala:"),
                "ID-trainer": input("Digite ID del trainer: "),
                "fechaInicio": input("Fecha inicio: "),
                "fechaFin": input("Fecha fin: "),
                "Horario": input("Horario:\n\t1. Mañana: 6 am a 10 am\n\t2. Mañana: 10 am a 2 pm\n\t3. Tarde: 2 pm a 6 pm\n\t4. Tarde: 6 pm a 10 pm\nEscriba el codigo del horario: "),
            }

            for ruta in rutasList:
                if info.get("CodigoRuta") == ruta.get("Codigo"):
                    camper["Ruta"] = ruta.get("Nombre")
    
    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)

    