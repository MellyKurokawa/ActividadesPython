#Se importa la 
import random

#Se define la función del juego
def adivinaElNumero():
    print("¡Bienvenido a Adivina el Número!")
    print("Piensa en un número entre 1 y 50.")
    
    #Aquí se ingresa el número que debe de adivinar la máquina
    numAdivina = int(input("Ingrese el número que se tiene que adivinar: "))


    #Se inicia la variable del contador de los intentos
    intentos = 0 
    #Se inicia la variable del rango minimo a adivinar
    menor = 1
    #Se inicia la variable del rango máximo a adivinar
    mayor = 50
    #Se inicia la variable de las predicciones de la máquina
    numMaquina = 0
    
    while numMaquina != numAdivina:
        # La computadora hace una predicción
        numMaquina = random.randint(menor, mayor)
        
        #Imprime lo ingresado por la máquina y damos la respuesta si es o no el número
        print(f"¿Es {numMaquina} tu número secreto?")
        respuesta = input("Ingresa 'si' si es correcto, 'max' si tu número es mayor, o 'min' si es menor: ")
        
        if respuesta == 'si':
            print(f"¡La computadora adivinó tu número en {intentos} intentos!")
            #Aquí termina el bucle cuando la maquina adivina el número
            break
        # Ajusta el rango mínimo de búsqueda
        elif respuesta == 'max':
            menor = numMaquina + 1
            # Ajustar el rango máximo de búsqueda
        elif respuesta == 'min':
            mayor = numMaquina - 1
        else:
            print("Respuesta inválida. Por favor ingresa 'si', 'mas' o 'menos'.")
        
        #Se incrmenta el contador de los intentos
        intentos += 1


#Si la máquina no adivina el número, se despliega el siguiente mensaje
    if numMaquina != numAdivina:
        print("¡La computadora no pudo adivinar tu número! ¡Intenta de nuevo!")

# Llamar a la función principal del juego
adivinaElNumero()
