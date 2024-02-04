info = {
    "Nombre": input("Nombre de ruta: "),
    "Temario": input("Ingrese los temas de este modulo separados por comas (','): "),
    "Codigo": input("Codigo de ruta: ")
}

info["Temario"] = info["Temario"].split(",")

for tema in info["Temario"]:
    print(tema)