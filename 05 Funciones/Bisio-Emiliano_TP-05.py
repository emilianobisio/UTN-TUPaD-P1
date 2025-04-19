# Ejercicio 1

# Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# Ejercicio 2

# Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
saludar_usuario("Marcos")

# Ejercicio 3

# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

# Definicion de funciones
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo con radio {radio} es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo con radio {radio} es: {calcular_perimetro_circulo(radio)}")

# Ejercicio 5

# Definicion de funciones
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese los segundos a convertir en horas: "))
print(f"{segundos} son {segundos_a_horas(segundos)} hora/s.")

# Ejercicio 6

# Definicion de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingrese el número para imprimir su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Ejercicio 7

# Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b

    resultados = [suma, resta, producto, division]

    return tuple(resultados)

# Programa principal
a = 10
b = 5

tupla_resultados = operaciones_basicas(a, b)

operaciones = ["Suma", "Resta", "Multiplicación", "División"]
for i in range(len(tupla_resultados)):
    print(f"{operaciones[i]}: {tupla_resultados[i]}")

# Ejercicio 8

# Definicion de funciones
import math

def calcular_imc(peso, altura):
    imc = peso / math.pow(altura, 2)
    return imc

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es: {round(calcular_imc(peso, altura), 2)}")

# Ejercicio 9

# Definicion de funciones
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{celsius}°C son {celsius_a_fahrenheit(celsius)}°F.")

# Ejercicio 10

# Definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
numero_1 = float(input("Ingrese el número 1: "))
numero_2 = float(input("Ingrese el número 2: "))
numero_3 = float(input("Ingrese el número 3: "))

print(f"El promedio de la suma de {numero_1}, {numero_2} y {numero_3} es: {calcular_promedio(numero_1, numero_2, numero_3)}")


