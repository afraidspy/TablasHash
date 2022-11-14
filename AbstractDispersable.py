# -*- coding: utf-8 -*-
"""
@author: guest
"""

from abc import ABC, abstractmethod

class Dispersable(ABC):
    @abstractmethod
    def esta_vacia():
        pass
    @abstractmethod
    def vaciar():
        pass
    @abstractmethod
    def cantidad_elementos():
        pass
    @abstractmethod
    def agregar():
        pass
    @abstractmethod
    def contiene(elemento):
        pass
    @abstractmethod
    def obtener(indice):
        pass
    @abstractmethod
    def eliminar(elemento):
        pass
    