from os import system
from .validate import noValid
import json

with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    rutasList = baseDeDatos["rutas"]
    modulosList = baseDeDatos["modulos"]

def menu():
    while True:
        print("""     _______________________________________
    |                                       |
    |        RUTAS DE ENTRENAMIENTO         |
    |_______________________________________|
    """)
        print("\t1. Registrar Ruta\n\t2. Lista de Rutas\n\t3. Editar Ruta\n\t4. Eliminar Ruta\n\t5. Modulos\n\t0. Salir")
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
                case 5:
                    system("clear")
                    modulos()
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
    |           REGISTRO DE RUTA            |
    |_______________________________________|
    """)
    info = {
        "Nombre": input("Nombre de ruta: "),
        "Modulos": mostrarModulos(),
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

def mostrarModulos():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        modulosList = baseDeDatos["modulos"]
    
    while True:
        print("Modulos: Digite los codigos que desea incluir separados por comas (',')")
        for modulo in modulosList:
            print(f"\t{modulo.get('Codigo')}. {modulo.get('Nombre')}")
        modulosSeleccionado = input()
        modulosSeleccionado = modulosSeleccionado.split(",")

        modulosDeRuta = []
        
        for x, modulo in zip(range(len(modulosSeleccionado)), modulosList):
            try:
                if modulo.get("Codigo") == modulosSeleccionado[x]:
                    modulosDeRuta.append(modulo.get("Nombre"))
            except IndexError:
                print("Atencion! - Hubo modulo/s no encontrado/s")
        return modulosDeRuta
            
            

def search():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |            LISTA DE RUTAS             |
    |_______________________________________|
    """)
    for ruta in rutasList:
        print(f"""
        Nombre: {ruta.get("Nombre")}
        Modulos: {ruta.get("Modulos")}
        Codigo: {ruta.get("Codigo")}
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
            Nombre: {rutasList[cod].get("Nombre")}
            Modulos: {rutasList[cod].get("Modulos")}
            Codigo: {rutasList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el ruta que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()
            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        rutasList[cod]["Nombre"] = input("Nombre: ")
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
            except ValueError:
                system("clear")
                noValid(opc)
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
        
        codigo_ruta = input("Ingrese el codigo del ruta que desea eliminar: ")

        try:
            cod = next(index for index, ruta in enumerate(rutasList) if ruta.get("Codigo") == codigo_ruta)
            print(f"""
            Nombre: {rutasList[cod].get("Nombre")}
            Modulos: {rutasList[cod].get("Modulos")}
            Codigo: {rutasList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el ruta que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()
            try:
                opc = int(opc)
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
            except ValueError:
                system("clear")
                noValid(opc)
        except StopIteration:
            system("clear")
            print("Error: Ruta no encontrada.")

def modulos():
    while True:
        print("""     _______________________________________
    |                                       |
    |                MODULOS                |
    |_______________________________________|
    """)
        print("\t1. Registrar Modulo\n\t2. Lista de Modulos\n\t3. Editar Modulo\n\t4. Eliminar Modulo\n\t0. Salir")
        opc = input()

        try:
            opc = int(opc)
            match(opc):
                case 1:
                    system("clear")
                    save_modulos()
                case 2:
                    system("clear")
                    search_modules()
                case 3:
                    system("clear")
                    
                case 4:
                    system("clear")
                    delete_modules()
                case 0:
                    system("clear")
                    break
                case _:
                    system("clear")
                    noValid(opc)
        except ValueError:
            system("clear")
            noValid(opc)
    
def save_modulos():
    print("""     _______________________________________
    |                                       |
    |         REGISTRO DE MODULO            |
    |_______________________________________|
    """)
    info = {
        "Nombre": input("Nombre: "),
        "Temario": input("Ingrese los temas de este modulo separados por comas (','): "),
        "Codigo": input("Codigo: ")
    }

    info["Temario"] = info["Temario"].split(",")

    for modulo in modulosList:
        if info.get("Codigo") == modulo.get("Codigo"):
            return system("clear"), print("Este modulo ya esta registrada.")
    modulosList.append(info)

    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
    return system("clear"), print("Modulo Guardado.")

def search_modules():
    system("clear")
    print("""     _______________________________________
    |                                       |
    |           LISTA DE MODULOS            |
    |_______________________________________|
    """)
    for modulo in modulosList:
        print(f"""
        Nombre: {modulo.get("Nombre")}
        Temario: {modulo.get("Temario")}
        Codigo: {modulo.get("Codigo")}
        """)

def delete_modules():
    while True:
        print("""     _______________________________________
    |                                       |
    |          ELIMINAR UN MODULO           |
    |_______________________________________|
    """)
        
        codigo_modulo = input("Ingrese el codigo del modulo que desea eliminar: ")

        try:
            cod = next(index for index, modulo in enumerate(modulosList) if modulo.get("Codigo") == codigo_modulo)
            print(f"""
            Nombre: {modulosList[cod].get("Nombre")}
            Temario: {modulosList[cod].get("Temario")}
            Codigo: {modulosList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el modulo que desea eliminar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        modulosList.pop(cod)

                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Modulo eliminado.")
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
            print("Error: Modulo no encontrado.")

def edit_modules():
     while True:
        print("""     _______________________________________
    |                                       |
    |           EDITAR UN MODULO            |
    |_______________________________________|
    """)
        
        codigo_modulo = input("Ingrese el codigo del modulo que desea editar: ")

        try:
            cod = next(index for index, modulo in enumerate(modulosList) if modulo.get("Codigo") == codigo_modulo)
            print(f"""
            Nombre: {modulosList[cod].get("Nombre")}
            Temario: {modulosList[cod].get("Temario")}
            Codigo: {modulosList[cod].get("Codigo")}
            """)
            print("¿Esta seguro que este es el modulo que desea editar?\n\t1. Si\n\t2. No\n\t0. Salir")
            opc = input()

            try:
                opc = int(opc)
                match(opc):
                    case 1:
                        system("clear")
                        modulosList[cod]["Nombre"] = input("Nombre: ")
                        modulosList[cod]["Temario"] = input("Ingrese los temas de este modulo separados por comas (','): ")
                        modulosList[cod]["Codigo"] = input("Codigo: ")
                        
                        modulosList[cod]["Temario"] = modulosList[cod]["Temario"].split(",")
                        
                        with open("modules/storage/data.json", "w") as f:
                            data = json.dumps(baseDeDatos, indent=4)
                            f.write(data)
                        system("clear")
                        print("Modulo editado.")
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
            print("Error: Modulo no encontrado.")