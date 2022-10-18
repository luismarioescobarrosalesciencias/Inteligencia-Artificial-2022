#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TopologicalSort.py
----------------
Ejercicio 3 Busqueda ciega, topological sort

Equipo:
    - Anzaldúa Díaz Andrea Fernanda
    - Escobar Rosales Luis Mario
    - Garcia Toxqui Demian Oswaldo
    - Padilla Lara Diego Javier
"""

class TopologicalSort(object):

    def __init__(self):
      self.data = None
    
    #Método encargado de buscar un nodo con ingrado = 0
    def ingrado(self,grafo):
      #Contador de ingrados
      concurrencias = {}
      for llaves in grafo.keys(): #Exploramos llaves.
        numeroApariciones = 0 #Número de apariciones.
        #print("Llave a comparar: " + llaves)
        indiceLlave = 0; #El índice de las concurrencias a iterar.
        for valores in grafo.values(): #Exploramos tuplas de valores.
          #print("Longitud de la tupla a la que apunta la llave: " + str(len(valores)))
          for j in range(len(valores)): #Comparamos llaves con tuplas de valores.
            #print("Comparando la llave -> "+llaves+" con el valor -> " + valores[j])
            if llaves == valores[j]: #Si encontramos el valor de la llave en la tupla de valores entonces agregamos un 1 a sus apariciones.
              numeroApariciones = numeroApariciones + 1

        concurrencias[llaves] = numeroApariciones

      for llaves in concurrencias.keys(): #Buscamos el nodo de Ingrado = 0 y devolvemos su llave.
        if concurrencias[llaves] == 0:
          return llaves

    # Método que realiza el algoritmo topologicalSort en un grafo dirigido.
    def topologicalSort(self,grafo):
      R = []
      grafoC = grafo.copy()
        
      while 0 < len(grafoC):
        i = self.ingrado(grafoC)
        R.append(i)
        grafoC.pop(i)
      return R

# ------------------ MAIN --------------------------

grafo1 = {
    'A':['C','D'],
    'B':['E','C'],
    'C':['D'],
    'D':[],
    'E':['A','C']
}

grafo2 = {
    1:[2,3],
    3:[4],
    2:[4,5],
    4:[5],
    5:[]
}

grafo3 = {
    'Inicio':['Pantalon', 'Playera'],
    'Pantalon':['Zapatos'],
    'Zapatos':['Lentes'],
    'Playera':['Sueter'],
    'Sueter':['Lentes'],
    'Lentes':['Llaves'],
    'Llaves':['Salir'],
    'Salir':[]
}
print("Ejercicio 2: Algoritmo TopologicalSort")
T = TopologicalSort()
print("\nGrafo 1:")
print(grafo1)
print("TopologicalSort del Grafo 1:")
TS = T.topologicalSort(grafo1)
print(TS)
print("\nGrafo 2:")
print(grafo2)
print("TopologicalSort del Grafo 2:")
TS = T.topologicalSort(grafo2)
print(TS)
print("\nGrafo 3:")
print(grafo3)
print("TopologicalSort del Grafo 3:")
TS = T.topologicalSort(grafo3)
print(TS)