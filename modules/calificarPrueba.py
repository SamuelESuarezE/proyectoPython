from os import system
from .validate import noValid
import json
def menu():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
        modulosList = baseDeDatos["modulos"]
    print("""
     __ _  __ ____ __  ____    _  _  __ ____  _  _ __    __  ____ 
    (  ( \/  (_  _) _\/ ___)  ( \/ )/  (    \/ )( (  )  /  \/ ___)
    /    (  O ))(/    \___ \  / \/ (  O ) D () \/ ( (_/(  O )___ \\
    \_)__)\__/(__)_/\_(____/  \_)(_/\__(____/\____|____/\__/(____/
    """)
    id = input("Ingrese el documento del camper: ")
    print("")
    for modulo in modulosList:
        print(f"{modulo.get('Codigo')}. {modulo.get('Nombre')}")

    moduloID = input("\nIngrese el codigo del modulo que desea calfiicar:")
    notaProyecto = input("Notas Proyecto (separadas por comas ','): ")
    notaProyecto = notaProyecto.split(",")
    notaExamen = input("Notas Examen (separadas por comas ','): ")
    notaExamen = notaExamen.split(",")
    notaGeneral = input("Notas Generales (separadas por comas ','): ")
    notaGeneral = notaGeneral.split(",")

    try:
        notaProyecto = list(map(int, notaProyecto))
        notaExamen = list(map(int, notaExamen))
        notaGeneral = list(map(int, notaGeneral))

        total = round(((sum(notaProyecto)/len(notaProyecto))*0.6) + ((sum(notaExamen)/len(notaExamen))*0.3) + ((sum(notaGeneral)/len(notaGeneral))*0.1))
        
        
        for camper in campersList:
            if camper.get("ID") == id:
                for modulo in modulosList:
                    if modulo.get('Codigo') == moduloID:
                        if total >= 60:
                            resultado = "Aprobado"
                            if camper["Estado"] == "Inscrito":
                                camper["Estado"] = "Aprobado"
                            elif camper["Estado"] == "Preinscrito":
                                break
                        else:
                            resultado = "Reprobado"
                            if camper["Estado"] == "Aprobado":
                                camper["Estado"] = "En riesgo"
                            elif camper["Estado"] == "En riesgo":
                                camper["Estado"] = "Filtrado"
                            elif camper["Estado"] == "Preinscrito":
                                break
                        info = {
                            "ID": camper.get('ID'),
                            "Nombre": f"{camper.get('Nombres')} {camper.get('Apellidos')}",
                            "Total": total,
                            "Resultado": resultado
                        }
                        modulo["Notas"].append(info)
                        
        
        with open("modules/storage/data.json", "w") as f:
            data = json.dumps(baseDeDatos, indent=4)
            f.write(data)
                    
        input("\nPresione enter para continuar...")
        system("clear")
    except ValueError:
        print("Error, digite notas validas.")
        input("\nPresione enter para continuar...")
        system("clear")
        
                
    