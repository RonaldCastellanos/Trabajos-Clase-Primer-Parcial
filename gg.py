import os 
os.system('cls' if os.name == 'nt' else 'clear')

texto = input("Ingrese un texto: ")
letras = input("Ingrese tres letras: ").lower()

# Contar la cantidad de veces que aparecen las letras
letras_encontradas = [letra for letra in letras]
contador = {letra: texto.lower().count(letra) for letra in letras_encontradas}

# Contar la cantidad de palabras
palabras = texto.split()

# Obtener la primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]

# Invertir el orden de las palabras
palabras_invertidas = palabras[::-1]

# Unir las palabras con espacios intermedios
texto_invertido = " ".join(palabras_invertidas)

# Verificar si la palabra "python" se encuentra en el texto
python_encontrado = "python" in texto.lower()

# Imprimir los resultados
print("Análisis del texto:")
print("Cantidad de veces que aparecen las letras:")
for letra, cantidad in contador.items():
    print(f"{letra}: {cantidad}")

print(f"Cantidad de palabras: {len(palabras)}")
print(f"Primera letra del texto: {primera_letra}")
print(f"Última letra del texto: {ultima_letra}")
print(f"Texto con palabras en orden invertido: {texto_invertido}")
print(f"Python se encuentra en el texto: {python_encontrado}")