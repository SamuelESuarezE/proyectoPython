from os import system
from .validate import noValid
import json

campersList = []

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]

def menu():
    while True:
        print("""         _______________________________________
        |                                       |
        |                CAMPERS                |
        |_______________________________________|
        """)
        print("\t1. Registrar Camper\n\t2. Lista de Campers\n\t3. Editar Camper\n\t4. Eliminar Camper\n\t0. Salir")
        opc = int(input())

        match(opc):
            case 1:
                system("clear")
                save()
            case 2:
                system("clear")
                search()
                # TODO: This should let me see the list of campers
            case 3:
                system("clear")
                print("\nEditar Camper")
                # TODO: This should let me edit a camper
            case 4:
                system("clear")
                print("\nEliminar Camper")
                # TODO: This should let me delete a camper
            case 0:
                system("clear")
                break
            case _:
                system("clear")
                noValid(opc)

def save():
    print("""         _______________________________________
        |                                       |
        |          REGISTRO DE CAMPER           |
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
        "Estado": "Preinscrito"
    }

    print(baseDeDatos)
    campersList.append(info)
    baseDeDatos['campers']=campersList

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Camper Guardado.")

def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |           LISTA DE CAMPERS            |
    |_______________________________________|
    """)
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

        """)

def edit():
    print(3)

def delete():
    print(4)

