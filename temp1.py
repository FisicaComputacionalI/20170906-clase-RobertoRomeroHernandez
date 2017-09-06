import numpy as np
import pylab as pl

x = [6000, 7000, 8000, 9000, 10000]
#Crea un vector (arreglo) con los valores del eje Y para cada valor del eje X
y = [  73,   80,   85,   87,    90]
#Grafica el vector x contra el vector y
pl.plot (x,y)
#Crea un vector (arreglo) con los valores del eje x
x1 = [7000, 8000, 9000, 10000, 11000]
#Crea un vector (arreglo) con los valores del eje Y para cada valor del eje X
y2 = [  80,   83,   85,    86,    88]
#Grafica el vector x contra el vector y
pl.plot (x1,y2)
pl.ylabel('Eficiencia[%]')
pl.xlabel('Voltaje [V]')
#Guarde la grafica en formato png
pl.savefig('temp1.png')
pl.show()
