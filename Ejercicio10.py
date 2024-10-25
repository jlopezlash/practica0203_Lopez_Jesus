#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por
#la contraseña hasta que introduzca la contraseña correcta.
Contraseña = 'Programacion'
while True:
    Contra = input('Dime tu contraseña ')
    if Contra == Contraseña:
        print('Contraseña Correcta')
        break
    if Contra != Contraseña:
        print('Contraseña incorrecta ')