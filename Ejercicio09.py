'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
#que tenga tantas líneas como el número introducido, como el triángulo de más abajo
1
3 1
5 3 1
7 5 3 1
'''
Altura = int(input('Dime un número entero '))
for i in range(1, Altura + 1, 2):
    print(1 * i)
