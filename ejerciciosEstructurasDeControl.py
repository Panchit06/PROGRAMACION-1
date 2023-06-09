# Ejercicios estructura condicional simple:
# Ejercicio 1
"""
letra1 = input("Ingrese la primera letra: ")
letra2 = input('Ingrese la segunda letra: ')

if letra1 == letra2:
    print('Las letras son iguales')
else:
    print('Las letras son diferentes')
"""
# Ejercicio 2
"""
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if palabra1 == palabra2:
    print("Las palabras son iguales.")
else:
    print("Las palabras son diferentes.")
"""
# Ejercicio 3
"""
genero = input('Ingrese "f" si es femenino o "m" si es masculino')

if genero == "f":
    print("Vota en la mesa femenina")
elif genero == "m":
    print("Vota en la mesa masculina")
else:
    print('Ha ingresado una letra erronea, ingrese "m" o "f" segun corresponda')
"""
# Ejercicio 4
"""
numero1 = input('Ingese el primer numero: ')
numero2 = input('Ingese el segundo numero: ')

if numero1 > numero2:
    print("El primer número es mayor.")
elif numero1 < numero2:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
"""
# Ejercicio 5
"""
tipo_cambio = input(
    "Ingrese el tipo de cambio que desea realizar ('p' para pesos a dólares, 'd' para dólares a pesos): ")

if tipo_cambio == "p":
    cantidad_pesos = float(input("Ingrese la cantidad de pesos: "))
    tipo_cambio_dolar = float(
        input("Ingrese el valor actual de 1 dólar en pesos: "))
    cantidad_dolares = cantidad_pesos / tipo_cambio_dolar
    print("El equivalente en dólares es: " + cantidad_dolares")
elif tipo_cambio == "d":
    cantidad_dolares = float(input("Ingrese la cantidad de dólares: "))
    tipo_cambio_peso = float(
        input("Ingrese el valor actual de 1 peso en dólar: "))
    cantidad_pesos = cantidad_dolares * tipo_cambio_peso
    print("El equivalente en pesos es: " + cantidad_pesos")
else:
    print("Tipo de cambio no válido. Por favor, ingrese 'p' o 'd'.")
"""
# Ejercicio 6
"""
edad_usuario = input('Ingrese su edad: ')

if edad_usuario <= 16:
    print('No vota')
else:
    print('Puede votar')
"""
# Ejercicios estructura condicional compuesto (IF anidados)
# Ejercicio 1
"""
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
"""
# Ejercicio 2
"""
importe = float(input("Ingrese el importe a pagar: "))
forma_pago = int(input("Seleccione la forma de pago (1 - Contado, 2 - Tarjeta, 3 - Débito): "))

if forma_pago == 1:
    descuento = importe * 0.1
    importe_total = importe - descuento
    print("Importe: " + importe)
    print("Descuento: " + descuento)
    print("Importe total: " + importe_total)
elif forma_pago == 2:
    interes = importe * 0.1
    importe_total = importe + interes
    print("Importe: " + importe)
    print("Interés: " + interes)
    print("Importe total: " + importe_total)
elif forma_pago == 3:
    descuento = importe * 0.05
    importe_total = importe - descuento
    print("Importe: " + importe)
    print("Descuento: "+ descuento)
    print("Importe total: "+ importe_total)
else:
    print("Forma de pago no válida. Por favor, seleccione 1, 2 o 3.")
"""
# Ejercicio 3
"""
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

mayor = max(numero1, numero2, numero3)

print("El número mayor es:", mayor)

if mayor % 2 == 0:
    print("El número mayor es par.")
else:
    print("El número mayor es impar.")
"""
# Ejercicio 4
"""
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 7.")
"""
# Ejercicio 5
"""
numero = int(input("Ingrese un número del 1 al 12: "))

if numero == 1:
    print("Enero")
elif numero == 2:
    print("Febrero")
elif numero == 3:
    print("Marzo")
elif numero == 4:
    print("Abril")
elif numero == 5:
    print("Mayo")
elif numero == 6:
    print("Junio")
elif numero == 7:
    print("Julio")
elif numero == 8:
    print("Agosto")
elif numero == 9:
    print("Septiembre")
elif numero == 10:
    print("Octubre")
elif numero == 11:
    print("Noviembre")
elif numero == 12:
    print("Diciembre")
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 12.")
"""
