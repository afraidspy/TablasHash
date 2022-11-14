# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 03:25:53 2022

@author: guest
"""

from HashTableDispersionCerrada import HashTable


table = HashTable(7)

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
