import os 
os.system('cls' if os.name == 'nt' else 'clear')

palabra= input("Escriba una palabra: ").upper()

palabra_reversa = palabra [::-1]

if palabra_reversa [::-1] == palabra:
    print(palabra+" Es un polindromo")
else:
    print(palabra+" No es un polindromo")

