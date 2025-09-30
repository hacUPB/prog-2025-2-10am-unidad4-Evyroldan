'''
Generar una lista con 199 números aleatorios entre 100 y 1000
Calcular el promedio de los valores de la lista
Calcular el mayor y el menor de la lista
'''

import random
numeros = []

for i in range(100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

suma = 0
for i in numeros: 
    suma += i

'''
 otra forma

 for i in range(len(numeros)):
    suma = += numeros[i]
'''

prom = suma / len(numeros)
print(f"promedio = {prom}")

mayor = max(numeros)
menor = min(numeros)


