m = float(input('Ingrese cantidad de dinero depositada en la cuenta de ahorros:'))

i= 0.04
for a in range (1,4):
    m = m* (1+i)
    print(f"El monto al final del año {a} es :{m}")
          
    #c1= c + c * i c * (1 + i)



print ('Modelo de la ecuacion  a*x^2 + b*x + c = 0')
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
#calculando  las  delta
delta = float(b**2-4*a*c)
          
if delta < 0:
    print('Ecuacion no presenta solución real')

elif delta ==0:
    s == float(-b/2*a)
    print ('Solucion unica: ',s)
else:
    x1 = float((-b+((b**2 - 4*a*c))**0.5)/(2*a))
    x2 = float((-b-((b**2 - 4*a*c))**0.5)/(2*a))
    print('Las soluciones son las siguientes')
    print('X1: ',x1)
    print('X2: ',x2)
