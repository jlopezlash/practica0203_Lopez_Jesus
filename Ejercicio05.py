#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre.
#Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y
#Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
#y muestre por pantalla el grupo que le corresponde.
Nombre = input('¿Cual es tu nombre? ')
Sexo = input('¿Cual es género (M o H)? ')
if Sexo == 'M':                     #Se ponen '' para elegir un dato
    if Nombre.lower() < 'M':
            Casa = 'Gryffindor'     #Se guarda el dato entre ''.
    else:
            Casa = 'Slytheryn'
else:
    if Sexo == 'H':
        if Nombre.lower() >'N':
            Casa = 'Gryffindor'
        else:
             Casa = 'Slytheryn'
print('Tu casa es', Casa)