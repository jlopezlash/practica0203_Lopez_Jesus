#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range(1, 11):
    for y in range(1, 11):
        print(i * y, end='\t')
    print('')