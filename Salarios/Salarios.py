#Le pedimos al usuario que ingrese su salario mensual
salario = float(input("Ingrese su salario mensual: "))
#Le pedimos al usuario que ingrese su puntuación
puntuacion = int(input("Ingrese su puntuación: "))

#Función para calcular el nivel de rendimiento y la cantidad de dinero recibido
def calcularSM(salario, puntuacion):
    #Revisa en qué rango de puntuación se encuentra y se asigna al que corresponde
    if puntuacion >= 0 and puntuacion <= 3:
        rendimiento = "Inaceptable"
    elif puntuacion >= 4 and puntuacion <= 6:
        rendimiento = "Aceptable"
    elif puntuacion >= 7 and puntuacion <= 10:
        rendimiento = "Meritorio"
    else:
        # Si la puntuación no está dentro del rango, despliega el mensaje de error
        rendimiento = "Puntuación no válida, inténtelo de nuevo"  

    #Calcula la cantidad de dinero por el salario por la proporción de la puntuación sobre 10
    dinero = salario * (puntuacion / 10)
    #Regresa el nivel de rendimiento y la cantidad de dinero que recibió
    return rendimiento, dinero 

# Llamamos a la función calcular_rendimiento para obtener el nivel y la cantidad de dinero recibido
rendimiento, cantidad_dinero = calcularSM(salario, puntuacion)

# Imprimimos el nivel de rendimiento y la cantidad de dinero recibido formateados adecuadamente
print(f"Nivel de Rendimiento: {rendimiento}")
print(f"Cantidad de Dinero Recibido: ${cantidad_dinero}")

