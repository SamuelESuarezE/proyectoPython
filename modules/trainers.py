from os import system
from .validate import noValid
import json

trainersList = []

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    trainersList = baseDeDatos["trainers"]

def menu():
    while True:
        print("""     _______________________________________
    |                                       |
    |               TRAINERS                |
    |_______________________________________|
    """)
        print("\t1. Registrar Trainer\n\t2. Lista de Trainers\n\t3. Editar Trainer\n\t4. Eliminar Trainer\n\t0. Salir")
        opc = int(input())

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

def save():
    print("""     _______________________________________
    |                                       |
    |           REGISTRO DE TRAINER          |
    |_______________________________________|
    """)
    info = {
        "ID": input("N° de identificacion: "),
        "Nombre": input("Nombre completo: "),
        "CodigoHorario": input("Codigo horario: "),
        "CodigoRuta:": input("Codigo ruta: "),
    }

    trainersList.append(info)
    baseDeDatos['trainers']=trainersList

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Trainer Guardado.")

def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |            LISTA DE TRAINERS           |
    |_______________________________________|
    """)
    for train in trainersList:
        print(f"""
        ID: {train.get("ID")}
        Nombre: {train.get("Nombre")}
        Codigo horario: {train.get("CodigoHorario")}
        Codigo ruta: {train.get("CodigoRuta")}
        """)

def edit():
    while True:
        print("""     _______________________________________
    |                                       |
    |           EDITAR UN TRAINER            |
    |_______________________________________|
    """)
        
        id_trainer = input("Ingrese el id del trainer que desea editar: ")

        try:
            cod = next(index for index, trainer in enumerate(trainersList) if trainer.get("ID") == id_trainer)
            print(f"""
            ID: {trainersList[cod].get("ID")}
            Nombre: {trainersList[cod].get("Nombre")}
            Codigo horario: {trainersList[cod].get("CodigoHorario")}
            Codigo ruta: {trainersList[cod].get("CodigoRuta")}
            """)
            print("¿Esta seguro que este es el trainer que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = int(input())

            match(opc):
                case 1:
                    system("clear")
                    trainersList[cod]["ID"] = input("N° de identificacion: ")
                    trainersList[cod]["Nombre"] = input("Nombre completo: ")
                    trainersList[cod]["CodigoHorario"] = input("Codigo horario: ")
                    trainersList[cod]["CodigoRuta"] = input("Codigo ruta: ")

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

        except StopIteration:
            system("clear")
            print("Error: Trainer no encontrado.")
    
def delete():
    while True:
        print("""     _______________________________________
    |                                       |
    |          ELIMINAR UN TRAINER           |
    |_______________________________________|
    """)
        
        id_trainer = input("Ingrese el id del trainer que desea eliminar: ")

        try:
            cod = next(index for index, trainer in enumerate(trainersList) if trainer.get("ID") == id_trainer)
            print(f"""
            ID: {trainersList[cod].get("ID")}
            Nombre: {trainersList[cod].get("Nombre")}
            Codigo horario: {trainersList[cod].get("CodigoHorario")}
            Codigo ruta: {trainersList[cod].get("CodigoRuta")}
            """)
            print("¿Esta seguro que este es el trainer que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = int(input())

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

        except StopIteration:
            system("clear")
            print("Error: Trainer no encontrado.")