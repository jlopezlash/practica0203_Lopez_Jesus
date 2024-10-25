'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
que tenga tantas líneas como el número introducido, como el triángulo de más abajo
1
3 1
5 3 1
7 5 3 1
'''
x = int(input('Dime un número entero '))
for i in range(1, x + 1, 2):
    for b in range(i, 0, -2):
        print(b, end=' ')
    print('')
