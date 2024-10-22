#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
Edad = int(input('¿Cuantos años tienes? '))
for Años in range(1, Edad, 1):
        print('Has cumplido los años', Años)