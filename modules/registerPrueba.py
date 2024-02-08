from os import system
from .validate import noValid
import json
def menu():
    with open("modules/storage/data.json", "r") as f:
        baseDeDatos = json.loads(f.read())
        campersList = baseDeDatos["campers"]
    print("""
     ____ ____  _  _ ____ ____  __     ____ ____ 
    (  _ (  _ \/ )( (  __|  _ \/ _\   (    (  __)
     ) __/)   /) \/ () _) ) _ (    \   ) D () _) 
    (__) (__\_)\____(____|____|_/\_/  (____(____)
          __  ____ _  _ __ ____ __ __  __ _ 
         / _\(    ( \/ |  ) ___|  )  \(  ( \
        /    \) D ( \/ \)(\___ \)(  O )    /
        \_/\_(____|_)(_(__|____(__)__/\_)__)

    """)
    
    id = input("Ingrese el documento del camper para registrar su prueba: ")
    for camper in campersList:
        if camper.get("ID") == id:
            notas = [int(input("Ingrese la nota de la prueba teorica: ")), int(input("Ingrese la nota de la prueba practica: "))]
            promedio = sum(notas)/2
                
            if promedio>60:
                camper["Estado"] = "Inscrito"
                print("El camper aprobó la prueba!")
            else:
                print("El camper no aprobó la prueba :(")
    with open("modules/storage/data.json", "w") as f:
        data = json.dumps(baseDeDatos, indent=4)
        f.write(data)
                
    input("Presione enter para continuar...")
        
                
    