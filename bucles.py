import random

# Ejemplo 1: Contador simple con while True
contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador >= 5:  # Salir del bucle cuando el contador llegue a 5
        break

# Ejemplo 2: Solicitar entrada del usuario hasta que sea válida
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == 'salir':  # Salir del bucle si el usuario escribe 'salir'
        print("¡Adiós!")
        break
    else:
        print(f"Escribiste: {entrada}")

# Ejemplo 3: Bucle infinito con condición interna

while True:
    numero = random.randint(1, 10)
    print(f"Número generado: {numero}")
    if numero == 7:  # Salir del bucle si se genera el número 7
        print("¡Se generó el número 7! Fin del bucle.")
        break
    
    
caca = 10
if caca == 11:
    print ("que bien")
else:
    print ("que mal")