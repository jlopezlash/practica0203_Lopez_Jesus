#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
Número = int(input('Dime un número entero '))
if Número % 2 == 0:         # % es una división
    print(Número, 'es par ')
else:
    print(Número, 'es impar ')