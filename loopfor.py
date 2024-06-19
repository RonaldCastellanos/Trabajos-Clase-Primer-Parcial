import os 
os.system('cls' if os.name == 'nt' else 'clear')

#ciclo For



#for i in range(1,20,2):
# -----print(i)

#ciclo for en lista

#lista=["uno","dos","tres","cuatro","cinco"]

#for item in lista:
  #  print(item)

#ciclo for  con tuolas

#tupla=("uno","dos","tres","cuatro","cinco")
#for item in tupla:
   # print(item)

#ciclo for con diccionario

#diccionario= {
#    "curso":"Python TOTAL",
 #   "clase":"Diccionarios",
 #   "tema":"For",
 #   "duracion":"30 dias",
  #  "profesor":"Ronald"
#}

#print(diccionario)
#for llave in diccionario:
#   print(llave,":",diccionario[llave])

#for llave in reversed(diccionario):
#   print(llave,":",diccionario[llave])

tabla = int(input("Ingresa un numero: "))
for i in range(11):
    print(tabla, "x", i, "=", tabla*i)
print("\n")

factorial = int(input("Ingresa el valor del factorial: "))
resultado=1
for i in range(1,factorial+1):
    resultado=resultado*i
print(f"{factorial}! es {resultado}")