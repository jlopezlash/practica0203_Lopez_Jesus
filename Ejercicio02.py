#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.
Número01 = float(input('Dime un número '))
Número02 = float(input('Dime otro número '))
if Número02 == 0:
    print('¡ERROR!' )
else:
    print('La solución es', (Número01/Número02))