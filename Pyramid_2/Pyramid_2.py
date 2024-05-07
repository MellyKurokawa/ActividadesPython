#Pedimos al usuario que ingrese la altura de la piramide
pyramid = int(input("Introduce la altura de la pirámide, usando un entero positivo: "))
for height in range(1, pyramid+1, 2): #1, 3, 5.. de dos en dos
    for number in range(height, 0, -2): #vamos hasta height hasta el cero restandole 2.. 5, 3, 1
        print(number, end=" ") #agrego un espacio al final de cada número
    print("") #salto de linea