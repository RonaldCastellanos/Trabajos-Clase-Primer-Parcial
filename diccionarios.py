import os 
os.system('cls' if os.name == 'nt' else 'clear')

mi_diccionario = {"curso":"Python TOTAL","clase":"Diccionarios"}
print(mi_diccionario["clase"])
print(mi_diccionario["curso"])

mi_diccionario["recursos"] = ["notas","ejercicios,examenes,proyectos"]