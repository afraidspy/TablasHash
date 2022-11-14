# -*- coding: utf-8 -*-
"""
@author: guest
"""
from AbstractDispersable import Dispersable

class TablaDispersionAbierta(Dispersable):
    
    def __init__(self,tam=100):
        self.tam = tam
        self.cubetas = []
        self.cubetas = [[] for i in range(self.tam)]
        self.cuantos = 0
    
    def esta_vacia(self):
        return self.cuantos == 0
    
    def vaciar(self):
        self.cubetas = []
        self.cubetas = [[] for i in range(self.tam)]
        self.cuantos = 0
  
    def cantidad_elementos(self):
        return self.cuantos
    
    def agregar(self,elemento):
        indice_funcion = abs(hash(elemento) % self.tam)
        self.cubetas[indice_funcion].append(elemento)
        self.cuantos += 1

    def contiene(self,elemento):
        indice_funcion = abs(hash(elemento) % self.tam)
        return elemento in self.cubetas[indice_funcion]
    
    def obtener(self,indice):
        return self.cubetas[indice]
    
    def eliminar(self,elemento):
        indice_funcion = abs(hash(elemento) % self.tam)
        if elemento in self.cubetas[indice_funcion]:
            lista_posicion = self.cubetas[indice_funcion]
            lista_posicion.remove(elemento)
        
    def imprimir(self):
        print("Imprimir...")
        for i in self.cubetas:
            if len(i)!=0:
                print(i)
     
            