
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
table = [None for i in range(10)]
print(table)


def funcion_dispersion(palabra,tam_tabla):
    suma_caracteres = 0
    for caracter in palabra :
        valor_ascci = ord(caracter)
        suma_caracteres += valor_ascci
    return suma_caracteres % tam_tabla



print("Sandra", funcion_dispersion("Sandra", 10))


print("Leonor", funcion_dispersion("Leonor", 10))

print("Mauricio", funcion_dispersion("Mauricio", 10))
print("Pedro", funcion_dispersion("Pedro", 10))
