# #CICLO WHILE

# while condicion:
# bloque de codigo a repetir


# #definir una variable que lleve el control del ciclo
# numero = 1
# while numero <= 5:      #condicion para iterar n veces
#     print (numero)
#     numero += 1


# # contaremos hacia atras
# numero = 10
# while numero >= 1:
#     print (numero)
#     numero -=1


# #crear un programa que sume los numeros ingresados por el usuario hasta que el usuario ingrese 0
# suma = 0 
# numero = int(input("ingresa un numero o pulsa 0 para salir: "))

# while numero != 0:
#     suma += numero 
#     numero = int(input("ingresa un numero o pulsa 0 para salir: "))
# print (f"la suma total es: {suma}")


# condiciones dinamicas
# son aleatorias y pueden cambiar con la ejecucion del codigo

# simulacion basa en una condicion externa

# #simularemos el crecimiento de una poblacion hasta que alcance un limite 
# poblacion = 1000
# limite = 5000
# tasa_crecimiento = 1.1
# while poblacion < limite:
#  print (f"poblacion actual: {poblacion}")
#  poblacion = int(poblacion * tasa_crecimiento)
# print (F"poblacion final: {poblacion}")
    

#lecturas de un sensor 
#simular la lectura de un sensor que medira valores aleatorios hasta que alcance un valor objetivo

# import random

# sensor = random.randint(0,50)
# objetivo = 40
# contador = 1

# while sensor < objetivo:
#     print ( f"en la lectura numero {contador}, el valor del sensor es : {sensor}")
#     sensor += random.randint(1,10)
#     contador += 1
#     print (f"la lectura final alcanzada fue: {sensor}")
