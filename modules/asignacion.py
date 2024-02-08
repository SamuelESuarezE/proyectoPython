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
        salasList = baseDeDatos["salas"]
    print("""
      __   ____  __  ___  __ _   __    ___  __  __   __ _ 
     / _\ / ___)(  )/ __)(  ( \ / _\  / __)(  )/  \ (  ( \\
    /    \\\___ \ )(( (_ \/    //    \( (__  )((  O )/    /
    \_/\_/(____/(__)\___/\_)__)\_/\_/ \___)(__)\__/ \_)__)
    """)
    while True:
        id = input("Ingrese el documento del camper que desea asignar: ")
        for camper in campersList:
            if camper.get("ID") == id:
                if camper["Estado"] == "Aprobado":
                    info = {
                        "CodigoRuta": mostrarRutas(),
                        "CodigoSala": input("Digite el codigo de la sala:\n\t1. Sputnik\n\t2. Apolo\n\t3. Artemis\n"),
                        "ID-trainer": input("Digite ID del trainer: "),
                        "fechaInicio": input("Fecha inicio: "),
                        "fechaFin": input("Fecha fin: "),
                        "Horario": input("Digite codigo de horario:\n\t1. Mañana: 6 am a 10 am\n\t2. Mañana: 10 am a 2 pm\n\t3. Tarde: 2 pm a 6 pm\n\t4. Tarde: 6 pm a 10 pm\n"),
                    }

                    camper["fechaInicio"]=info.get("fechaInicio")
                    camper["fechaFin"]=info.get("fechaFin")
                    camper["Horario"]=info.get("Horario")

                    for ruta in rutasList:
                        if info.get("CodigoRuta") == ruta.get("Codigo"):
                            camper["Ruta"] = ruta.get("Nombre")

                    for sala in salasList:
                        if (camper.get("ID") in sala["estudiantes1"]) or (camper.get("ID") in sala["estudiantes2"]) or (camper.get("ID") in sala["estudiantes3"]) or (camper.get("ID") in sala["estudiantes4"]):
                            print("\n- El camper ya esta registrado en una sala de entrenamiento.")
                            print("- Si desea cambiar la sala, debe hacer el registro del camper nuevamente.")
                            break
                        else:
                            if sala.get("Codigo") == info.get("CodigoSala"):
                                match(info.get("Horario")):
                                    case "1":
                                        if len(sala["estudiantes1"]) < sala.get("Capacidad"):
                                                camper["Sala"] = sala.get("Nombre")
                                                sala["estudiantes1"].append(id)
                                        else:
                                            print("Error: la sala asignada se encuentra llena.")
                                            break
                                    case "2":
                                        if len(sala["estudiantes2"]) < sala.get("Capacidad"):
                                                camper["Sala"] = sala.get("Nombre")
                                                sala["estudiantes2"].append(id)
                                        else:
                                            print("Error: la sala asignada se encuentra llena.")
                                            break
                                    case "3":
                                        if len(sala["estudiantes3"]) < sala.get("Capacidad"):
                                                camper["Sala"] = sala.get("Nombre")
                                                sala["estudiantes3"].append(id)
                                        else:
                                            print("Error: la sala asignada se encuentra llena.")
                                            break
                                    case "4":
                                        if len(sala["estudiantes4"]) < sala.get("Capacidad"):
                                                camper["Sala"] = sala.get("Nombre")
                                                sala["estudiantes4"].append(id)
                                        else:
                                            print("Error: la sala asignada se encuentra llena.")
                                            break

                    for trainer in trainersList:
                        if info.get("ID-trainer") == trainer.get("ID"):
                            camper["Trainer"] = trainer.get("Nombre")
                            info = {
                                "ID": camper.get("ID"),
                                "Nombre": (f"{camper.get('Nombres')} {camper.get('Apellidos')}")
                            }
                            trainer["Campers"] = []
                            trainer["Campers"].append(info) 
                    

                    
                    with open("modules/storage/data.json", "w") as f:
                        data = json.dumps(baseDeDatos, indent=4)
                        f.write(data)

                    print("\nCamper matriculado correctamente.")
                else:
                    print("\n- El camper no esta aprobado.")
        
        print("\n- Si el sistema no permite asignar al camper, es porque el camper no esta registrado.")
        input("Presione enter para continuar...")
        break

    