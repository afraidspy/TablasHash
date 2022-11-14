# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 06:23:43 2022

@author: guest
"""

from HashTableDispersionAbierta import TablaDispersionAbierta


table = TablaDispersionAbierta(7)
table.agregar("Saúl")
table.agregar("Diana")
table.agregar("Ulises")
table.agregar("Javier")
table.agregar("Fernando")
table.agregar("Pedro")
table.agregar("Lola")



table.imprimir()

print("Existe Pedro",table.contiene("Pedro"))
print("Existe Fernando",table.contiene("Fernando"))
print("Existe Mario",table.contiene("Mario"))

table.eliminar("Diana")

table.imprimir()
