import os 
os.system('cls' if os.name == 'nt' else 'clear')

#Condiciones if

edad= int(input("Ingresa tu edad: "))
if edad >= 21:
    print("Eres mayor de edad")
elif edad >= 18:
    print("Eres cuidadano")
else:
    print("Eres menor de edad")
