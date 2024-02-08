from os import system
from .validate import noValid
import json

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    trainersList = baseDeDatos["trainers"]
    rutasList = baseDeDatos["rutas"]

def menu():
    while True:
        print("""
     ____  ____   __   __  __ _  ____  ____  ____ 
    (_  _)(  _ \ / _\ (  )(  ( \(  __)(  _ \/ ___)
      )(   )   //    \ )( /    / ) _)  )   /\___ \\
     (__) (__\_)\_/\_/(__)\_)__)(____)(__\_)(____/
    """)
        print("\t1. Registrar Trainer\n\t2. Lista de Trainers\n\t3. Ver Trainers segun Ruta\n\t4. Editar Trainer\n\t5. Eliminar Trainer\n\t6. Ver campers de un trainer\n\t0. Salir")
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
                    trainersSegunRuta()
                case 4:
                    system("clear")
                    edit()
                case 5:
                    system("clear")
                    delete()
                case 6:
                    system("clear")
                    campersDeUnTrainer()
                case 0:
                    system("clear")
                    break
                case _:
                    system("clear")
                    noValid(opc)
        except ValueError:
            system("clear")
            noValid(opc)

def campersDeUnTrainer():
    with open("modules/storage/data.json","r") as f:
        baseDeDatos = json.loads(f.read())
        trainersList = baseDeDatos["trainers"]
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |      VER CAMPERS DE UN TRAINER        |
    |_______________________________________|
    """)
    for trainer in trainersList:
        print(f"\tID: {trainer.get('ID')} | Nombre: {trainer.get('Nombre')}")
        
    id = input("\nIngrese la ID del trainer: ")
    
    for camper in campersList:
        for trainer in trainersList:
            if id == trainer.get('ID') and trainer.get('Nombre') == camper.get("Trainer"):
                print(f"""
                Documento: {camper.get("ID")}
                Nombre: {camper.get("Nombres")} {camper.get("Apellidos")}
                """)

    input("Presione enter para continuar...")
    system("clear")
def save():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        trainersList = baseDeDatos["trainers"]
        campersList = baseDeDatos["campers"]

    print("""     _______________________________________
    |                                       |
    |           REGISTRO DE TRAINER         |
    |_______________________________________|
    """)
    info = {
        "ID": input("N° de identificacion: "),
        "Nombre": input("Nombre completo: "),
        "Horario": input("Horario:\n\t1. Mañana: 6 am a 10 am\n\t2. Mañana: 10 am a 2 pm\n\t3. Tarde: 2 pm a 6 pm\n\t4. Tarde: 6 pm a 10 pm\nEscriba los numeros de los horarios que maneje: "),
        "Ruta": mostrarRutas()
    }

    for train in trainersList:
        if info.get("ID") == train.get("ID"):
            return system("clear"), print("Este trainer ya esta registrado.")

    trainersList.append(info)

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Trainer Guardado.")

def mostrarRutas():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        rutasList = baseDeDatos["rutas"]
    
    print("Ruta:")
    for ruta in rutasList:
        print(f"\t{ruta.get('Codigo')}. {ruta.get('Nombre')}")
    rutaSeleccionada = input()
    rutaSeleccionada = rutaSeleccionada.split(",")
    
    rutasGuardadas = []

    for ruta in rutasList:
        if ruta.get("Codigo") in rutaSeleccionada:
            rutasGuardadas.append(ruta.get("Nombre"))
    return rutasGuardadas

def trainersSegunRuta():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        rutasList = baseDeDatos["rutas"]
        trainersList = baseDeDatos["trainers"]
    while True:
        print("""         _______________________________________
        |                                       |
        |     LISTA DE TRAINERS SEGUN RUTA      |
        |_______________________________________|
        """)
        for ruta in rutasList:
            print(f"\t{ruta.get('Codigo')}. {ruta.get('Nombre')}")
        print("\t0. Salir")

        cod=input()

        system("clear")

        if cod == "0":
            system("clear")
            break
  
        for x, trainer in enumerate(trainersList):
            for ruta in rutasList:
                if cod == ruta.get("Codigo") and (ruta.get("Nombre") in trainer.get("Ruta")):
                    print(f"""
            ID: {trainersList[x].get("ID")}
            Nombre: {trainersList[x].get("Nombre")}
            Horario: {trainersList[x].get("Horario")}
            Ruta: {trainersList[x].get("Ruta")}
            """)




def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |            LISTA DE TRAINERS          |
    |_______________________________________|
    """)
    for train in trainersList:
        print(f"""
        ID: {train.get("ID")}
        Nombre: {train.get("Nombre")}
        Horario: {train.get("Horario")}
        Ruta: {train.get("Ruta")}
        """)

def edit():
    while True:
        print("""     _______________________________________
    |                                       |
    |           EDITAR UN TRAINER           |
    |_______________________________________|
    """)
        
        id_trainer = input("Ingrese el id del trainer que desea editar: ")

        try:
            cod = next(index for index, trainer in enumerate(trainersList) if trainer.get("ID") == id_trainer)
            print(f"""
            ID: {trainersList[cod].get("ID")}
            Nombre: {trainersList[cod].get("Nombre")}
            Horario: {trainersList[cod].get("Horario")}
            Ruta: {trainersList[cod].get("Ruta")}
            """)
            print("¿Esta seguro que este es el trainer que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        trainersList[cod]["ID"] = input("N° de identificacion: ")
                        trainersList[cod]["Nombre"] = input("Nombre completo: ")
                        trainersList[cod]["Horario"] = input("Horario:\n\t1. Mañana: 6 am a 10 am\n\t2. Mañana: 10 am a 2 pm\n\t3. Tarde: 2 pm a 6 pm\n\t4. Tarde: 6 pm a 10 pm\n")
                        trainersList[cod]["Ruta"] = mostrarRutas()

                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Trainer editado.")
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
            print("Error: Trainer no encontrado.")
    
def delete():
    while True:
        print("""     _______________________________________
    |                                       |
    |          ELIMINAR UN TRAINER          |
    |_______________________________________|
    """)
        
        id_trainer = input("Ingrese el id del trainer que desea eliminar: ")

        try:
            cod = next(index for index, trainer in enumerate(trainersList) if trainer.get("ID") == id_trainer)
            print(f"""
            ID: {trainersList[cod].get("ID")}
            Nombre: {trainersList[cod].get("Nombre")}
            Horario: {trainersList[cod].get("Horario")}
            Ruta: {trainersList[cod].get("Ruta")}
            """)
            print("¿Esta seguro que este es el trainer que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        trainersList.pop(cod)

                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Trainer eliminado.")
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
            print("Error: Trainer no encontrado.")