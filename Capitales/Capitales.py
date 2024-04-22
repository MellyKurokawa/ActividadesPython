#Pedimos al usuario que ingrese los datos
cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))

 #Inicializamos la variable capital con la cantidad a invertir
capital = cantidad

"""
Utilizamos un bucle for para iterar sobre cada año
range(1, años + 1) el bucle iterará desde el año 1 hasta el año ingresado

"""
for año in range(1, años + 1):
 
 """
 Por cada iteración del bucle, calculamos el nuevo capital utilizando la fórmula del interés compuesto
 (interes / 100) convierte el interés en una fracción decimal
 capital * (interes / 100) calcula el interés ganado durante ese año, multiplicando el capital por el interés
 += actualiza el valor de capital para el siguiente año de inversión, reflejando el interés ganado durante ese año
 """
 capital += capital * (interes / 100)

 #Imprimimos el resultado
 print("Capital tras", año, "año(s):", capital)