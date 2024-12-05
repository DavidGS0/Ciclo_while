#Ciclo while

#while condicion.
    #Bloqueo de codigo a repetir

#Definir una variable que lleve el control del ciclo
numero= 1

while numero <=5:# condicion para iterar n veces...
    print(numero)
    numero += 1

#Contaremos hacia atras
numero = 10

while numero >=1:
    print(numero)
    numero -= 1

#Crear un programa que sume los numeros ingresados por el usuario hasta que el usuario ingrese 0.

suma = 0

numero = int(input("Ingresa Un Numero O Pulsa 0 Para Salir: "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa Un Numero O Pulsa 0 Para Salir: "))

print (f"La Suma Total Es: {suma}")

#Condiciones dinamicas
#Son aleatorias y pueden cambiar con la ejecucion de codigo.

##Simulacion basada en una condicion externa,
#Simularemos el crecimiento de una poblacion hasta que alcance un limite.

poblacion =1000
limite = 5000
tasa_crecimiento =1.1

while poblacion < limite:
    print(f"Poblacion actual: {poblacion}")
    poblacion = int (poblacion*tasa_crecimiento)

print(f"Poblacion final alcanzada: {poblacion}")

