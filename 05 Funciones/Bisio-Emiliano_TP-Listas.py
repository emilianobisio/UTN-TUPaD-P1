# Ejercicio 1
lista_multiplos_4 = list(range(0,101,4))
print(lista_multiplos_4)

# Ejercicio 2
lista_paises = ["Argentina", "Brasil", "Italia", "España", "Eslovenia"]
print(lista_paises[-2])

# Ejercicio 3
lista_nombres = []
lista_nombres.append("Clara")
lista_nombres.append("Fran")
lista_nombres.append("Sofia")
print(lista_nombres)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[-3] = "loro"
animales[-1] = "oso"
print(animales)

# Ejercicio 5

""" Partiendo de la lista llama "numeros", con la función max(numeros) encontramos el mayor valor de la
lista, en este caso el número 22, y luego con el método remove() lo eliminamos de la misma.
Por útimo, mostramos por pantalla la lista sin el elemento 22. Por lo tanto, la lista "numeros" quedaria
[8,15,3,7] """

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Ejercicio 6
numeros = list(range(10,31,5))
print(numeros[0])
print(numeros[1])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ford"
autos[2] = "fiat"

# Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Ejercicio 9
compras = [ ["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"] ]
compras[2].append("jugo") # a)
compras[1][1] = "tallarines" # b)
compras[0].remove("pan") # c)
print(compras) # d)

# Ejercicio 10
lista_anidada = [ 15, True, [25.5, 57.9, 30.6], False ]
print(lista_anidada[0])
print(lista_anidada[1])
print(lista_anidada[2][0])
print(lista_anidada[2][1])
print(lista_anidada[2][2])
print(lista_anidada[3])
print(lista_anidada)