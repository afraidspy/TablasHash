# -*- coding: utf-8 -*-
"""

@author: guest
"""
from AbstractDispersable import Dispersable

class HashTable(Dispersable):
        
    def __init__(self, tam=100):
        self.tam = tam
        self.table = []
        self.table = [None for i in range(tam)]
        self.cuantos = 0

    def esta_vacia(self):
        return self.cuantos==0
    
    def vaciar(self):
        self.table = []
        self.table = [None for i in range(10)]
        self.cuantos = 0
    
    def cantidad_elementos(self):
        return self.cuantos
    
    def agregar(self, elemento):
        print("Agregar...", elemento)
        if self.cuantos == self.tam:
            raise NameError("Tabla llena")
        else: 
            indice_funcion = abs(hash(elemento)%self.tam)
            print("Indice función, ", indice_funcion)
            if self.table[indice_funcion] is None:
                print(indice_funcion)
                self.table[indice_funcion] = elemento
                self.cuantos += 1
            else:
                for i in range (indice_funcion + 1, self.tam):
                    if i == (self.tam-1) and self.table[i] != None:
                        print("Empezando desde arriba,,")
                        i = 0
                    if self.table[i] is None:
                        self.table[i] = elemento
                        self.cuantos += 1
                        break
             
    def contiene(self,elemento):
        if self.esta_vacia():
            return False
        else:
            indice_funcion = abs(hash(elemento)%self.tam)
            for i in range (self.tam):
                if i == self.tam - 1:
                    i = 0
                if self.table[indice_funcion] == elemento:
                    return True
                if i == indice_funcion:
                    return False
                return False    
            
    
    def obtener(self,indice):
        if indice >= 0 and indice < self.tam:
            return self.table[indice]
        else:
            return None
    
    def eliminar(self,elemento):
        if self.esta_vacia():
            print("Tabla vacía")
        else:
            indice_funcion = abs(hash(elemento)%self.tam)
            if self.table[indice_funcion] == elemento:
                self.table[indice_funcion] =  None
                return True
            else: 
                #Hubo una coalision
               for i in range (indice_funcion+1,self.tam):
                   if indice_funcion == self.tam -1:
                      i = 0
                   if self.table[indice_funcion] == elemento:
                       self.table[indice_funcion] =  None
                       return True
                   if i == indice_funcion:
                        break
            return False
                    

    def imprimir(self):
        print("Imprimir...")
        for i in self.table:
            if i != None:
                print(i)
                
    
    
    
    
            
    