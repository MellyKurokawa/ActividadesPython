# Solicitamos al usuario la cantidad a convertir
cantidad = int(input("Ingrese la cantidad que desea convertir a monedas: "))

#Definimos las variables en cero; para contar las monedas
monedas20 = 0
monedas10 = 0
monedas5 = 0
monedas1 = 0

"""
Para calcular las monedas tomamos como ejemplo lo primero:

monedas20 = cantidad // 20
Dividimos la cantidad entre 20 usando división entera //, así sabemos el número máximo de monedas de $20 que caben en la cantidad

cantidad %= 20
Se usa para actualizar la cantidad total
%= calcula la división de cantidad por 20 y luego actualiza cantidad con el resultado, ahora cantidad contiene el valor restante 
después de quitar todas las monedas de $20

"""
# Calculamos la cantidad de monedas de $20 que caben en la cantidad ingresada
monedas20 = cantidad // 20
cantidad %= 20

# Calculamos el número de monedas de $10 que caben en la cantidad ingresada
monedas10 = cantidad // 10
cantidad %= 10

# Calculamos el número de monedas de $5 que caben en la cantidad ingresada
monedas5 = cantidad // 5
cantidad %= 5

# El resto de la cantidad usa monedas de $1
monedas1 = cantidad

# Imprimimos el resultado, dependiendo la cantidad de monedas ingresadas
print("Monedas de $20:", monedas20)
print("Monedas de $10:", monedas10)
print("Monedas de $5:", monedas5)
print("Monedas de $1:", monedas1)



