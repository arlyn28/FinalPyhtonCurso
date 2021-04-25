while True:
    try:
        n = input("Ingrese la altura de la pirámide: ")
        height = int(n)

        if height == 0:
            print("Neutro")
        elif height < 0:
            print("Negativo")
        else:
            print("Positivo")
        
        for i in range(height):
            if height >8:
                print('Incorrecto')
            else:
                print (" "*(height-1*i)+("#")+("#"*(1*i)))


    except ValueError:
        continue      