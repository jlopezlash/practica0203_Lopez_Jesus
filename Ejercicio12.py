#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
#el número de veces que aparece la letra en la frase.
a = input('Escribe una frase ')
b = input('Dime una letra de esa frase ')
x = 0
for i in a:
    if i == b:
        x +=1       #+=1 es lo mismo que 1+1
print ('La letra', b, 'aparece', x, 'veces')