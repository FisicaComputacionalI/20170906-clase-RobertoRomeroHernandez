import numpy as np
import matplotlib.pyplot as plt
#Declaramos una funcion que nos devuelva f(x) = exp(-t)*cos(2pi*t)
def f(t):
  return np.exp(-t)* np.cos(2*np.pi*t)
#Definimos el rango de dos variables y el intervalo en el que cambian  
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
#Crear el grupo de graficas
plt.figure(1)
#Crear el lienzo con dos renglones, una columna y entra a la primes seccion
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.savefig('Dosfunciones.png')
plt.show()
