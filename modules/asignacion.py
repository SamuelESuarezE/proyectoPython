from os import system
from .validate import noValid
import json


with open("modules/storage/data.json", "r") as f:
    baseDeDatos = json.loads(f.read())
    campersList = baseDeDatos["campers"]
    trainersList = baseDeDatos["trainers"]
    rutasList = baseDeDatos["rutas"]
    modulosList = baseDeDatos["modulos"]

