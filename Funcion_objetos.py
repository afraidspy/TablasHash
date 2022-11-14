# -*- coding: utf-8 -*-
"""
@author: guest
"""


class Alumno:
    def __init__(self,nombre, num_cuenta,edad):
        self.nombre = nombre
        self.num_cuenta = num_cuenta
        self.edad = edad
       

alumno =  Alumno("Sonia","42322",21)

print("Hash_01: " ,alumno.__hash__())
print("Hash_02: " , hash(alumno))