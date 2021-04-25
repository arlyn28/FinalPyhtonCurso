alumno = str(input('Ingrese su nombre completo: '))

valor = 1
suma = 0
while valor < 4 :
    nota = int(input(f"Ingrese nota {valor} : ") )
    if 0<= nota <11:
        suma += nota
        valor+=1
    else:
        print("La nota debe ser entre 0 - 10 ")