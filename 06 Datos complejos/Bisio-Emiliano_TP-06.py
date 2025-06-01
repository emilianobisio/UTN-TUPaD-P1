# Ejercicio 1

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

# Agrego nuevas frutas y sus precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Ejercicio 2

# Actualizo los precios de las frutas Banana, Manzana y Melón
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Ejercicio 3

# Creo una lista que solo contenga las frutas sin los precios
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# Ejercicio 4

cantidad = 5
contador = 1
contactos = {}

while contador <= cantidad:
    nombre = input(f"Ingrese el nombre del contacto {contador}: ")
    numero = input(f"Ingrese el número del contacto {contador}: ")
    contactos[nombre] = numero
    contador += 1

print(contactos)

consulta = input("Ingrese el nombre del contacto a consultar: ")

if consulta in contactos.keys():
    print(contactos[consulta])
else:
    print("No se ha encontrado el contacto solicitado.")

# Ejercicio 5

frase = input("Ingrese una frase: ")
lista_frase = frase.split()
tupla_lista_frase = tuple(lista_frase)
palabras_unicas = set(lista_frase)
recuento = {}

for palabra in palabras_unicas:
    recuento[palabra] = tupla_lista_frase.count(palabra)

print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

# Ejercicio 6

cantidad = 3
alumnos = {}

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la primer nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))    
    nota3 = float(input("Ingrese la tercer nota: "))

    alumnos[nombre] = (nota1, nota2, nota3)    

print(f"Alumnos: {alumnos}")

for alumno in alumnos:
    acum = 0
    promedio = 0
    for nota in alumnos[alumno]:
        acum += nota
        promedio = acum / 3
    print(f"El promedio del alumno {alumno} es: {promedio:.2f}")

# Ejercicio 7

aprobados_parcial1 = {1, 2, 3, 4, 5}
aprobados_parcial2 = {3, 4, 5, 6, 7}
                    
# Estudiantes que aprobaron ambos parciales (la intersección de ambos sets)
ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)
                 
# Estudiantes que aprobaron solo uno de los dos parciales (diferencia simétrica)
solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
                    
# Lista total de estudiantes que aprobaron al menos un parcial (la unión de ambos sets)
total_aprobados = aprobados_parcial1.union(aprobados_parcial2)
                    
# Mostramos los resultados
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales)
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", total_aprobados)

# Ejercicio 8

productos = {
    "remeras": 120,
    "zapatillas": 340,
    "buzos": 99,
    "pantalones": 153
}

flag = True

while flag:

    print("1-Consultar stock de un producto.")
    print("2-Agregar unidades al stock de un producto existente.")
    print("3-Agregar un nuevo producto si no existe.")
    print("4-Salir.")
    opcion = int(input("Opción: "))

    match opcion:
        case 1:
            producto = input("Ingrese el nombre del producto: ")

            if producto in productos:
                print("El stock actual de", producto, "es:", productos[producto])
            else:
                print("El producto no existe.")
        
        case 2:
            producto = input("Ingrese el nombre del producto: ")

            if producto in productos:
                cantidad = int(input("Ingrese las unidades a agregar: "))
                productos[producto] = productos[producto] + cantidad
                print("El nuevo stock de", producto, "es:", productos[producto])
            else:
                print("El producto no existe.")
        
        case 3:
            producto = input("Ingrese el nombre del producto: ")

            if producto in productos:
                print("El producto ya existe!")
                print("El stock actual de", producto, "es:", productos[producto])
            else:
                cantidad = int(input("Ingrese el stock inicial: "))
                productos[producto] = cantidad
                print("El producto", producto, "se agregó con un stock de", cantidad)
        
        case 4:
            print("Saliendo...")
            flag = False
        
        case _:
            print("Opción incorrecta")

# Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de Inglés",
    ("miercoles", "20:00"): "Natación",
    ("jueves", "09:00"): "Turno Médico"
}

# Se muestra un mensaje al usuario para indicar el inicio de la consulta.
print("Consulta de Agenda")
    
# Solicitamos al usuario que ingrese el día.
dia = input("Ingrese el día de la semana (ejemplo: lunes, martes, etc.): ")
    
# Solicitar la hora.
hora = input("Ingrese la hora respetando el formato indicado (ejemplo: 8:00, 10:00): ")

# Se crea la clave a partir de los datos ingresados.
clave = (dia, hora)

# Verificamos si la clave existe en el diccionario.
if clave in agenda:
    print("La actividad programada es:", agenda[clave])
else:
    print("No hay ninguna actividad programada a esa hora.")

# Ejercicio 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(f"Original: {original}")
print(f"Invertido: {invertido}")

