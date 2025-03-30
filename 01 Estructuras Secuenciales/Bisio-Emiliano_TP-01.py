#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nomnbre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del círculo con radio {radio} es: {area}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos son: {horas} horas")

#Ejercicio 6
numero = int(input("Ingrese un número entero para mostrar su tabla de multiplicar: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Ejercicio 7
primer_numero = int(input("Ingrese el primer número entero: "))
segundo_numero = int(input("Ingrese el segundo número entero: "))
suma = primer_numero + segundo_numero
division = primer_numero / segundo_numero
producto = primer_numero * segundo_numero
resta = primer_numero - segundo_numero
print(f"{primer_numero} + {segundo_numero} = {suma}")
print(f"{primer_numero} / {segundo_numero} = {division}")
print(f"{primer_numero} * {segundo_numero} = {producto}")
print(f"{primer_numero} - {segundo_numero} = {resta}")

#Ejercicio 8
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"Su IMC es: {imc}")

#Ejercicio 9
celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} grados Celsius son: {fahrenheit} grados fahrenheit")

#Ejercicio 10
primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))
tercer_numero = float(input("Ingrese el tercer número: "))
promedio = (primer_numero + segundo_numero + tercer_numero) / 3
print(f"El promedio de los números ingresados es: {promedio}")