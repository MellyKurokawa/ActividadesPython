# Capturamos los datos del usuario con un input
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
email = input("Ingrese su correo electrónico: ")

"""
Se imprime con el caracter de escape ANSI 
 [0m se utiliza para restablecer el color del texto después de imprimir el mensaje vuelve al color predeterminado de la terminal.
{} indica la posición para el valor que que se ingresará en esa parte del código, ahí van los valores de nombre, edad y email
usando format() se insertan los valores de nombre, edad y email en las posiciones marcadas por {} 

"""
print("\033[1;36mMi nombre es {}\033[0m, \033[1;32mtengo {} años\033[0m y \033[1;35meste es mi correo electrónico {}\033[0m.".format(nombre, edad, email))