#Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")

#Ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Ejercicio 3

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par.")

#Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a.")
elif edad >= 12 and edad < 18:
    print("Adolescente.")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven.")
else:
    print("Adulto/a.")

#Ejercicio 5

password = input("Introduzca su contraseña: ")
longitud_password = len(password)

if longitud_password >= 8 and longitud_password <= 14:
    print("Ha ingresado un contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#media (mean)
media = mean(numeros_aleatorios)
print(f"Media: {media}")

#mediana (median)
mediana = median(numeros_aleatorios)
print(f"Mediana: {mediana}")

#moda (mode)
moda = mode(numeros_aleatorios)
print(f"Moda: {moda}")


if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("Sin sesgo.")

#Ejercicio 7

palabra = input("Ingrese una frase o palabara: ")

if palabra.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    print(f"{palabra}!")
else:
    print(palabra) 

#Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")

opcion = int(input("Ingrese opción correspondiente: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La opción ingresada es incorrecta.")

#Ejercicio 9

magnitud = int(input("Magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else: 
    print("Extremo (puede causar graves daños a gran escala).")

#Ejercicio 10

hemisferio = input("Ingrese en cúal hemisferio se encuentra: N(norte) o S(sur): ").upper()
mes = input("Ingrese el nombre del mes: ").lower()
dia = int(input("Ingrese el día del mes: "))

if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    elif hemisferio == "S": 
        print("Verano")
    else:
        print("Hemisferio Inválido")

if (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    elif hemisferio == "S": 
        print("Otoño")
    else:
        print("Hemisferio Inválido")

if (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    elif hemisferio == "S": 
        print("Invierno")
    else:
        print("Hemisferio Inválido")

if (mes == "septiembre" and dia >= 21) or mes == "octubre" or mes == "noviembre" or (mes == "diciembre" and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    elif hemisferio == "S": 
        print("Primavera")
    else:
        print("Hemisferio Inválido")





