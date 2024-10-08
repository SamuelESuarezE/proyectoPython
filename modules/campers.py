from os import system
from .validate import noValid
import json

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]
    salasList = baseDeDatos["salas"]
    trainersList = baseDeDatos["trainers"]

def menu():
    while True:
        print("\33[0;34m"+"""
      ___   __   _  _  ____  ____  ____  ____ 
     / __) / _\ ( \/ )(  _ \(  __)(  _ \/ ___)
    ( (__ /    \/ \/ \ ) __/ ) _)  )   /\___ \\
     \___)\_/\_/\_)(_/(__)  (____)(__\_)(____/\n"""+"\33[0;m")
        print("\t1. Registrar Camper\n\t2. Lista de Campers\n\t3. Editar Camper\n\t4. Eliminar Camper\n\t0. Salir")
        opc = input()

        try:
            opc = int(opc)
            match(opc):
                case 1:
                    system("clear")
                    save()
                case 2:
                    system("clear")
                    search()
                case 3:
                    system("clear")
                    edit()
                case 4:
                    system("clear")
                    delete()
                case 0:
                    system("clear")
                    break
                case _:
                    system("clear")
                    noValid(opc)
        except ValueError:
            system("clear")
            noValid(opc)

def save():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |           REGISTRO DE CAMPER          |
    |_______________________________________|
    """)
    info = {
        "ID": input("N° de identificacion: "),
        "Nombres": input("Nombres: "),
        "Apellidos": input("Apellidos: "),
        "Direccion": input("Direccion: "),
        "Acudiente": {
            "Nombre": input("(Acudiente) Nombre completo: "),
            "ID": input("(Acudiente) N° de identificacion: ")
        },
        "Celular": input("Celular: "),
        "Telefono_Fijo": input("Telefono fijo: "),
        "Estado": "Preinscrito",
        "Ruta": "Ninguna"
    }
    for camp in campersList:
        if info.get("ID") == camp.get("ID"):
            return system("clear"), print("Este camper ya esta registrado.")
        
    campersList.append(info)

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Camper Guardado.")

def search():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]

    print("""     _______________________________________
    |                                       |
    |           LISTA DE CAMPERS            |
    |_______________________________________|""")
    for camp in campersList:
        print(f"""
        ID: {camp.get("ID")}
        Nombres: {camp.get("Nombres")}
        Apellidos: {camp.get("Apellidos")}
        Direccion: {camp.get("Direccion")}
        Acudiente: {camp.get("Acudiente").get("Nombre")}
        ID Acudiente: {camp.get("Acudiente").get("ID")}
        Celular: {camp.get("Celular")}
        Telefono fijo: {camp.get("Telefono_Fijo")}
        Estado: {camp.get("Estado")}
        Ruta: {camp.get("Ruta")}
        Sala: {camp.get("Sala")}
        Trainer: {camp.get("Trainer")}
        Horario: {camp.get("Horario")}
        """)

def edit():
    while True:
        print("""     _______________________________________
    |                                       |
    |           EDITAR UN CAMPER            |
    |_______________________________________|
    """)
        
        id_camper = input("Ingrese el id del camper que desea editar: ")

        try:
            cod = next(index for index, camper in enumerate(campersList) if camper.get("ID") == id_camper)
            print(f"""
            ID: {campersList[cod].get("ID")}
            Nombres: {campersList[cod].get("Nombres")}
            Apellidos: {campersList[cod].get("Apellidos")}
            Direccion: {campersList[cod].get("Direccion")}
            Acudiente: {campersList[cod].get("Acudiente").get("Nombre")}
            ID Acudiente: {campersList[cod].get("Acudiente").get("ID")}
            Celular: {campersList[cod].get("Celular")}
            Telefono fijo: {campersList[cod].get("Telefono_Fijo")}
            Estado: {campersList[cod].get("Estado")}
            Ruta: {campersList[cod].get("Ruta")}
            Sala: {campersList[cod].get("Sala")}
            Trainer: {campersList[cod].get("Trainer")}
            Horario: {campersList[cod].get("Horario")}
            """)
            print("¿Esta seguro que este es el camper que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        campersList[cod]["ID"] = input("N° de identificacion: ")
                        campersList[cod]["Nombres"] = input("Nombres: ")
                        campersList[cod]["Apellidos"] = input("Apellidos: ")
                        campersList[cod]["Direccion"] = input("Direccion: ")
                        campersList[cod]["Acudiente"]["Nombre"] = input("(Acudiente) Nombre completo: ")
                        campersList[cod]["Acudiente"]["ID"] = input("(Acudiente) N° de identificacion: ")
                        campersList[cod]["Celular"] = input("Celular: ")
                        campersList[cod]["Telefono_Fijo"] = input("Telefono fijo: ")

                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Camper editado.")
                        break
                    case 2:
                        system("clear")
                    case 0:
                        system("clear")
                        break
            except ValueError:
                system("clear")
                noValid(opc)
        except StopIteration:
            system("clear")
            print("Error: Camper no encontrado.")
    
def delete():
    while True:
        print("""     _______________________________________
    |                                       |
    |          ELIMINAR UN CAMPER           |
    |_______________________________________|
    """)
        
        id_camper = input("Ingrese el id del camper que desea eliminar: ")

        try:
            cod = next(index for index, camper in enumerate(campersList) if camper.get("ID") == id_camper)
            print(f"""
            ID: {campersList[cod].get("ID")}
            Nombres: {campersList[cod].get("Nombre")}
            Apellidos: {campersList[cod].get("Apellido")}
            Direccion: {campersList[cod].get("Direccion")}
            Acudiente: {campersList[cod].get("Acudiente").get("Nombre")}
            ID Acudiente: {campersList[cod].get("Acudiente").get("ID")}
            Celular: {campersList[cod].get("Celular")}
            Telefono fijo: {campersList[cod].get("Telefono_Fijo")}
            Estado: {campersList[cod].get("Estado")}
            Ruta: {campersList[cod].get("Ruta")}
            Sala: {campersList[cod].get("Sala")}
            Trainer: {campersList[cod].get("Trainer")}
            Horario: {campersList[cod].get("Horario")}
            """)
            print("¿Esta seguro que este es el camper que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        for sala in salasList:
                            if (campersList[cod].get("ID") in sala["estudiantes1"]):
                                sala["estudiantes1"].remove(id_camper)
                            if (campersList[cod].get("ID") in sala["estudiantes2"]):
                                sala["estudiantes2"].remove(id_camper)
                            if (campersList[cod].get("ID") in sala["estudiantes3"]):
                                sala["estudiantes3"].remove(id_camper)
                            if (campersList[cod].get("ID") in sala["estudiantes4"]):
                                sala["estudiantes4"].remove(id_camper)
                        for trainer in trainersList:
                            for i, camper in enumerate(trainer["Campers"]):
                                if (campersList[cod].get("ID")) == camper.get("ID"):
                                    trainer["Campers"].pop(i)
                        campersList.pop(cod)

                        # for trainer in trainersList:
                        #     if (campersList[cod]).get("ID") in trainer[""]
                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Camper eliminado.")
                        break
                    case 2:
                        system("clear")
                    case 0:
                        system("clear")
                        break
            except ValueError:
                system("clear")
                noValid(opc)
        except StopIteration:
            system("clear")
            print("Error: Camper no encontrado.")