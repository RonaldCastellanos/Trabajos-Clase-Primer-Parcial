import os 
os.system('cls' if os.name == 'nt' else 'clear')

#imprime 10 valores con el ciclo while

#i=0
#while i<10:
#    print(i)
#    i+=1

#print("ciclo controlado pro bedderin ")

#while True:
#    entrada = input("ingresa S para salir ")
#    if entrada == "S":
#        break
#    print("Escribiste: ", entrada)

#   print ("ciclo controlado pro bedderin 2")
print("ciclo controlado pro bedderin ")
bandera= True
while bandera != False:
        bandera = input("ingresa S para salir ")
        print(bandera.upper())
        salir=bandera.upper()
        if salir == "S":
            bandera = False
        print("salir del ciclo")    
