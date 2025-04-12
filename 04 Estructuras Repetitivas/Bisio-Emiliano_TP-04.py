# Ejercicio 1

for num in range(1,100+1):
    print(num)

# Ejercicio 2

numero = int(input("Ingrese un número entero: "))
count = 0

for digito in str(numero):
    count += 1

print(f"El número {numero} tiene {count} digitos.")

# Ejercicio 3

inicio = int(input("Valor inicial: "))
fin = int(input("Valor final: "))
acumulador = 0

for num in range(inicio + 1, fin):
    acumulador += num

print(f"La sumatoria de los números comprendidos entre {inicio} y {fin} (excluyendo ambos) es: {acumulador}.")

# Ejercicio 4

numero = int(input("Ingrese un número entero: "))
sumatoria = 0

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese un número entero: "))

print(f"Sumatoria: {sumatoria}")

# Ejercicio 5

import random
numero_aleatorio = random.randint(0,9)
intentos = 1

numero_usuario = int(input("Adivine un número entre 0 y 9: "))

while numero_usuario != numero_aleatorio:
    intentos += 1
    numero_usuario = int(input("Adivine un número entre 0 y 9: "))

print(f"Intentos: {intentos}")

# Ejercicio 6

for num in range(100, 0 - 1, -1):
    if num % 2 == 0:
        print(num)

# Ejercicio 7

fin = int(input("Ingrese un número entero positivo: "))
acumulador = 0

for numero in range(0, fin + 1):
    acumulador += numero

print(f"La sumatoria de todos los número comprendidos entre 0 y {fin} es: {acumulador}")

# Ejercicio 8

cantidad_numeros = 100
contador = 1
pares = 0
impares = 0
negativos = 0
positivos = 0

while cantidad_numeros >= contador:
    numero = int(input(f"Número entero {contador}: "))

    if numero < 0:
        negativos += 1
    else:
        positivos += 1
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Negativos: {negativos}")
print(f"Positivos: {positivos}")

# Ejercicio 9

cantidad_numeros = 5
contador = 1
acumulador = 0
media = 0

while cantidad_numeros >= contador:
    numero = int(input(f"Número entero {contador}: "))
    acumulador += numero
    contador += 1

media = acumulador / cantidad_numeros
print(f"La media es: {media}")

# Ejercicio 10

numero = input("Ingresa un número: ")
numero_invertido = ""

for digito in reversed(numero):
    numero_invertido += digito

print(f"El número ingresado invertido es: {numero_invertido}.");