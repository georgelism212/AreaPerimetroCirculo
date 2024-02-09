#programa para calcular el area y perimetro de un circulo de radio R

import math

#imput 
r= imput("ingrese el radio: ")
r=int(r)

#processing
a=math .pi* r**2
p= 2 * math.pi * r 
# output
print ("El area es: " + str (a))
print ("El perimetro es: "+ str (p))
