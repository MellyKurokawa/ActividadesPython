#Creamos una variable y le pedimos al usuario que ingrese una palabra
word = input("Por favor, ingrese una palabra: ")

#Creamos una función que nos diga si la palabra es un palíndromo
def isPalindrome(word):
    firstLetter = 0 #inicializamos en cero, que representa la primera letra a la izq.
    lastLetter = len(word) - 1 #largo de la palabra -1, que es la última letra

#usamos for para verificar todos los caracteres de la palabra
    for letter in range(0, len(word)): # verifica la palabra desde el índice hasta el largo de la palabra
        if word[firstLetter] == word[lastLetter]: #comparamos si la letra del índice es igual a la última
            #si es así
            firstLetter += 1 #se incrementa en 1 y pasa a la siguiente letra
            lastLetter -= 1 #se resta 1 y pasa a la siguiente letra

        else: #si la letra no es igual de la primera a la última
            return False #no es palíndroma y retorna como false
    
    return True #si al pasar por todo el ciclo no imprime false, entonces imprime true diciendo que es palíndroma

if isPalindrome(word): #Si el resultado de la función es palíndroma, evaluando la palabra
    
    print("La palabra ingresada es un palíndromo") #si es así se imprime que es un palíndromo
else:
    print("La palabra ingresada no es un palíndromo") #si no, que no lo es
