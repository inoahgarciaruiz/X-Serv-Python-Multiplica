#!/usr/bin/python3

"""

   Make a Python script that, using for loops and range() functions, displays 
   in standard output (screen) multiplication tables 1-10

Author: Ainhoa Garcia-Ruiz Fuentes.       Date: 24/01/2018
Course: Servicios y Aplicaciones en Redes de Ordenadores.

"""

for m1 in range(1,11):
   print("\nTable of %d \n-----------" % m1 )
   for m2 in range(1,11):
        print('%d * %d = %d' % (m1, m2, m1 * m2))

