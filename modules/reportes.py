from os import system
from .validate import noValid
import json
from .trainers import search as searchTrainers
def menu():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
        modulosList = baseDeDatos["modulos"]
    while True:
        system("clear")
        print("\33[0;34m"+"""
     ____ ____ ____  __ ____ ____ ____ ____ 
    (  _ (  __|  _ \/  (  _ (_  _|  __) ___)
     )   /) _) ) __(  O )   / )(  ) _)\___ \\
    (__\_|____|__)  \__(__\_)(__)(____|____/
        """+"\33[0;m")
        print("\t1. Campers preinscritos.\n\t2. Campers inscritos.\n\t3. Campers aprobados\n\t4. Campers en riesgo.\n\t5. Campers filtrados\n\t6. Lista de Trainers\n\t7. Campers y trainers segun ruta de entrenamiento.\n\t8. Ver notas de modulos\n\t0. Salir")
        opc = input()

        try:
            opc = int(opc)
            match(opc):
                case 1:
                    system("clear")
                    campersPreinscritos()
                case 2:
                    system("clear")
                    campersInscritos()
                case 3:
                    system("clear")
                    campersAprobados()
                case 4:
                    system("clear")
                    campersRiesgo()
                case 5:
                    system("clear")
                    campersFiltrados()
                case 6:
                    system("clear")
                    searchTrainers()
                case 7:
                    system("clear")
                    verPersonasSegunRuta()
                case 8:
                    system("clear")
                    ver_notas()
                case 0:
                    system("clear")
                    break
                case _:
                    system("clear")
                    noValid(opc)
        except ValueError:
            system("clear")
            noValid(opc)
def campersFiltrados():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |           CAMPERS FILTRADOS           |
    |_______________________________________|
    """)
    for camp in campersList:
        if camp.get("Estado") == "Filtrado":
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
    
    input("Presione enter para continuar...")

def campersAprobados():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |           CAMPERS APROBADOS           |
    |_______________________________________|
    """)
    for camp in campersList:
        if camp.get("Estado") == "Aprobado":
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
    
    input("Presione enter para continuar...")
def campersInscritos():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |           CAMPERS INSCRITOS           |
    |_______________________________________|
    """)
    for camp in campersList:
        if camp.get("Estado") == "Inscrito":
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
    
    input("Presione enter para continuar...")

def campersPreinscritos():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |         CAMPERS PREINSCRITOS          |
    |_______________________________________|
    """)
    for camp in campersList:
        if camp.get("Estado") == "Preinscrito":
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
    
    input("Presione enter para continuar...")

def campersRiesgo():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""     _______________________________________
    |                                       |
    |           CAMPERS EN RIESGO           |
    |_______________________________________|
    """)
    for camp in campersList:
        if camp.get("Estado") == "En riesgo":
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
    
    input("Presione enter para continuar...")
def ver_notas():
    print("""     _______________________________________
    |                                       |
    |         VER NOTAS POR MODULO          |
    |_______________________________________|
    """)
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        modulosList = baseDeDatos["modulos"]
    for modulo in modulosList:
        print(f"{modulo.get('Codigo')}. {modulo.get('Nombre')}")
    print("")
    codigo_modulo = input("Ingrese el codigo del modulo que desea ver las notas: ")
    aprobados = 0
    noAprobado = 0
    for modulo in modulosList:
        if modulo.get("Codigo") == codigo_modulo:
            for camper in modulo.get("Notas"):
                print(f"""
        ID: {camper.get('ID')}
        Nombre: {camper.get('Nombre')}
        Total: {camper.get('Total')}
        Resultado: {camper.get('Resultado')}
        """)    
                if camper.get('Resultado') == "Aprobado":
                    aprobados+=1
                if camper.get('Resultado') == "Reprobado":
                    noAprobado+=1
    print(f"{aprobados} aprobaron {noAprobado} no aprobaron.")
    input("Presione enter para continuar...")
    system("clear")

def verPersonasSegunRuta():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        rutasList = baseDeDatos["rutas"]
        trainersList = baseDeDatos["trainers"]
        campersList = baseDeDatos["campers"]
    while True:
        print("""         _______________________________________
        |                                       |
        |          PERSONAS SEGUN RUTA          |
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
    
        print("""         _______________________________________
        |                                       |
        |     LISTA DE TRAINERS SEGUN RUTA      |
        |_______________________________________|
        """)
    
        for x, trainer in enumerate(trainersList):
            for ruta in rutasList:
                if cod == ruta.get("Codigo") and (ruta.get("Nombre") in trainer.get("Ruta")):
                    print(f"""
            ID: {trainersList[x].get("ID")}
            Nombre: {trainersList[x].get("Nombre")}
            Horario: {trainersList[x].get("Horario")}
            Ruta: {trainersList[x].get("Ruta")}
            """)

        print("""         _______________________________________
        |                                       |
        |      LISTA DE CAMPERS SEGUN RUTA      |
        |_______________________________________|
        """)
  
        for x, camper in enumerate(campersList):
            for ruta in rutasList:
                if cod == ruta.get("Codigo") and (ruta.get("Nombre") in camper.get("Ruta")):
                    print(f"""
            ID: {campersList[x].get("ID")}
            Nombre: {campersList[x].get("Nombres")} {campersList[x].get("Apellidos")}
            Horario: {campersList[x].get("Horario")}
            Ruta: {campersList[x].get("Ruta")}
            """)
        
        input("Presione enter para continuar...")
        system("clear")