from os import system
from .validate import noValid
import json

rutasList = []

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    rutasList = baseDeDatos["rutas"]

def menu():
    while True:
        print("""     _______________________________________
    |                                       |
    |        RUTAS DE ENTRENAMIENTO         |
    |_______________________________________|
    """)
        print("\t1. Registrar Ruta\n\t2. Lista de Rutas\n\t3. Editar Ruta\n\t4. Eliminar Ruta\n\t0. Salir")
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
    |           REGISTRO DE RUTA            |
    |_______________________________________|
    """)
    info = {
        "Nombre": input("Nombre de ruta: "),
        "Ḿodulos": input("Modulos de ruta: "),
        "Codigo": input("Codigo de ruta: ")
    }
    for ruta in rutasList:
        if info.get("Codigo") == ruta.get("Codigo"):
            return system("clear"), print("Esta ruta ya esta registrada.")
    rutasList.append(info)
    baseDeDatos['rutas']=rutasList

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Ruta Guardada.")

def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |            LISTA DE RUTAS           |
    |_______________________________________|
    """)
    for ruta in rutasList:
        print(f"""
        Nombre de ruta: {ruta.get("Nombre")}
        Modulos de ruta: {ruta.get("Modulos")}
        Codigo de ruta: {ruta.get("Codigo")}
        """)

def edit():
    while True:
        print("""     _______________________________________
    |                                       |
    |           EDITAR UNA RUTA             |
    |_______________________________________|
    """)
        
        codigo_ruta = input("Ingrese el codigo del ruta que desea editar: ")

        try:
            cod = next(index for index, ruta in enumerate(rutasList) if ruta.get("Codigo") == codigo_ruta)
            print(f"""
            Nombre de ruta: {rutasList[cod].get("Nombre")}
            Modulos de ruta: {rutasList[cod].get("Modulos")}
            Codigo de ruta: {rutasList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el ruta que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = int(input())

            match(opc):
                case 1:
                    system("clear")
                    rutasList[cod]["Nombre"] = input("Nombre de ruta: ")
                    rutasList[cod]["Modulos"] = input("Modulos: ")
                    rutasList[cod]["Codigo"] = input("Codigo: ")

                    with open("modules/storage/data.json", "w") as f:
                        data = json.dumps(baseDeDatos, indent=4)
                        f.write(data)
                    system("clear")
                    print("Ruta editada.")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break

        except StopIteration:
            system("clear")
            print("Error: Ruta no encontrada.")
    
def delete():
    while True:
        print("""     _______________________________________
    |                                       |
    |          ELIMINAR UNA RUTA            |
    |_______________________________________|
    """)
        
        codigo_ruta = input("Ingrese el id del ruta que desea eliminar: ")

        try:
            cod = next(index for index, ruta in enumerate(rutasList) if ruta.get("Codigo") == codigo_ruta)
            print(f"""
            Nombre de ruta: {rutasList[cod].get("Nombre")}
            Modulos de ruta: {rutasList[cod].get("Modulos")}
            Codigo de ruta: {rutasList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el ruta que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = int(input())

            match(opc):
                case 1:
                    system("clear")
                    rutasList.pop(cod)

                    with open("modules/storage/data.json", "w") as f:
                        data = json.dumps(baseDeDatos, indent=4)
                        f.write(data)
                    system("clear")
                    print("Ruta eliminada.")
                    break
                case 2:
                    system("clear")
                case 0:
                    system("clear")
                    break

        except StopIteration:
            system("clear")
            print("Error: Ruta no encontrada.")