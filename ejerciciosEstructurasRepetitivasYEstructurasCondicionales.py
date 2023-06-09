# Ejercicio 1
"""
contador_pares = 0
contador_impares = 0
sumatoria_pares = 0

for i in range(4):
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        contador_pares += 1
        sumatoria_pares += numero
    else:
        contador_impares += 1

print("Cantidad de numeros pares:", contador_pares)
print("Cantidad de numeros impares:", contador_impares)
print("Sumatoria de los números pares:", sumatoria_pares)
"""
# Ejercicio 2
"""
cantidad_mayores_100 = 0
cantidad_menores_100 = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

for i in range(10):
    numero = float(input("Ingrese un número: "))

    if numero > 100:
        cantidad_mayores_100 += 1
    elif numero < 100:
        cantidad_menores_100 += 1

    if numero > numero_maximo:
        numero_maximo = numero
    if numero < numero_minimo:
        numero_minimo = numero

print("Cantidad de números mayores a 100:", cantidad_mayores_100)
print("Cantidad de números menores a 100:", cantidad_menores_100)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)
"""
# Ejercicio 3
"""
contador_mujeres = 0
contador_varones = 0
contador_mayores_edad = 0
contador_menores_edad = 0

for i in range(15):
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ")

    if sexo == "F":
        contador_mujeres += 1
    elif sexo == "M":
        contador_varones += 1

    if edad >= 18:
        contador_mayores_edad += 1
    else:
        contador_menores_edad += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de personas mayores de edad:", contador_mayores_edad)
print("Cantidad de personas menores de edad:", contador_menores_edad)
"""
# Ejercicio 4
"""
sumatoria_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        print(numero)
        sumatoria_positivos += numero

print("Sumatoria de los números positivos:", sumatoria_positivos)
"""
# Ejercicio 5
"""
for i in range(15):
    numero = float(input("Ingrese un número negativo: "))

    numero_positivo = abs(numero)  # Utilizamos la función abs() para obtener el valor absoluto del número

    print(numero_positivo)
"""
