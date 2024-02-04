from os import system
from .validate import noValid
import json

campersList = []

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]

def menu():
    while True:
        print("""     _______________________________________
    |                                       |
    |                CAMPERS                |
    |_______________________________________|
    """)
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
                    searchMenu()
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
        "Estado": "Preinscrito"
    }
    for camp in campersList:
        if info.get("ID") == camp.get("ID"):
            return system("clear"), print("Este camper ya esta registrado.")
    campersList.append(info)
    baseDeDatos['campers']=campersList

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Camper Guardado.")


def searchMenu():
        while True:
            print("""     _______________________________________
    |                                       |
    |           LISTA DE CAMPERS            |
    |_______________________________________|""")
            print("""
        1. Ver todos los Campers
        2. Ver Campers segun estado
        3. Ver Campers segun ruta
        4. Ver Campers segun trainer
        5. Ver Campers segun horario y salon
        0. Salir""")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        search()
                    case 2:
                        system("clear")
                        # TODO: Esto me deberia mostrar los campers segun estado
                    case 3:
                        system("clear")
                        # TODO: Esto me deberia mostrar los campers segun ruta 
                    case 4:
                        system("clear")
                        # TODO: Esto me deberia mostrar los cmapers segun trainer
                    case 5:
                        system("clear")
                        # TODO: Esto me deberia mostrar los campers segun horario y salon
                    case 0:
                        system("clear")
                        break
                    case _:
                        system("clear")
                        noValid(opc)
            except ValueError:
                system("clear")
                noValid(opc)


def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |            LISTA DE CAMPERS           |
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
            """)
            print("¿Esta seguro que este es el camper que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        campersList[cod]["ID"] = input("N° de identificacion: ")
                        campersList[cod]["Nombre"] = input("Nombres: ")
                        campersList[cod]["Apellido"] = input("Apellidos: ")
                        campersList[cod]["Direccion"] = input("Direccion: ")
                        campersList[cod]["Acudiente"]["Nombre"] = input("(Acudiente) Nombre completo: ")
                        campersList[cod]["Acudiente"]["ID"] = input("(Acudiente) N° de identificacion: ")
                        campersList[cod]["Celular"] = input("Celular: ")
                        campersList[cod]["Telefono_Fijo"] = input("Telefono fijo: ")
                        campersList[cod]["Estado"] = "Preinscrito"

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
            Nombres: {campersList[cod].get("Nombres")}
            Apellidos: {campersList[cod].get("Apellidos")}
            Direccion: {campersList[cod].get("Direccion")}
            Acudiente: {campersList[cod].get("Acudiente").get("Nombre")}
            ID Acudiente: {campersList[cod].get("Acudiente").get("ID")}
            Celular: {campersList[cod].get("Celular")}
            Telefono fijo: {campersList[cod].get("Telefono_Fijo")}
            Estado: {campersList[cod].get("Estado")}
            """)
            print("¿Esta seguro que este es el camper que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                match(opc):
                    case 1:
                        system("clear")
                        campersList.pop(cod)

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