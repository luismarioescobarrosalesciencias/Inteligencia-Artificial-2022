#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejercicio_4.py
----------------
Ejercicio 4.2 Best First Search, A*

Equipo:
    - Anzaldúa Díaz Andrea Fernanda
    - Escobar Rosales Luis Mario
    - Garcia Toxqui Demian Oswaldo
    - Padilla Lara Diego Javier
'''

from audioop import reverse
from fileinput import close
import pandas as pd
import sys
from collections import deque
from math import sin, cos, sqrt, atan2, radians


df = pd.DataFrame()
df = pd.read_csv('metro.csv')
df = df.iloc[: , 1:]

metro = df['origen'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').tolist()
metro = [*set(metro)]

result = [(x,y,z) for x,y,z in zip(df['origen'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'), 
                                   df['destino'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'),
                                   df['longitud'])]

aux = {i:[] for i in metro}

for i in result:
    aux[i[0]].append((i[1], i[2]))

#diccionario con los hijos de los nodos 
hijos ={j:[] for j in metro}

for j in result:
    hijos[j[0]].append(j[1])


#calcula la distancia de coordenadas geograficas
def distances(point1,point2):
# approximate radius of earth in km
    R = 6373.0
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])

    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
    #print(distance)

dl = pd.DataFrame()
dl = pd.read_csv('LineasMetro.csv')
#df = pd.read_csv('./resources/LineasMetro.csv')
dl = dl.iloc[: , 1:5]
linea = dl['nombre'].tolist()
linea = [*set(linea)]
r1 = [(w,x,y,z) for  w,x,y,z in zip(dl['linea'],dl['nombre'], dl['lat'], dl['lon'])]


#funcion que ayuda a ubicar los datos de una estacion (linea,nombre,lat,long)
def busca_destino(nombre):
    cons = (None,None,None,None)
    for r in r1 :
        if r[1] == nombre:
            cons = r
            break
    return cons

coordenadas = {}
i = 0
for r in r1 :
    if r[1] not in coordenadas :
        coordenadas[r[1]]  =(r[2],r[3])
    else:
        i+=1
estimated_cost  = {}
#lazaro = (cons[2],cons[3])
obj =  busca_destino("Lazaro Cardenas")
#print(obj)


#Tenemos ls costos estimados utilizando una formula que calcula las distancias entre puntos geograficos. En este caso de una estacion a Lazaro Cardenas 
for k in coordenadas:
    if k not in estimated_cost :
        estimated_cost[k] =  distances(coordenadas[k],(obj[2],obj[3]))
        
    else:
        continue
#print(estimated_cost)

def minimu(lista_hijos,cost):
    nombre = lista_hijos[0]
    minimo = cost[lista_hijos[0]]
    for h in lista_hijos:
        if  cost[h] < minimo:
            nombre =  h
            minimo = cost[h]
    return nombre



#funcion que elige el mejor nodo para continuar la ruta 
def mejor_seleccion(hijos,costos,ruta):
    nombre = hijos[0]
    #en la lista de hijos rescatar, sus costos y quedarse con el de menor costo
    #ver si el hijo ya esta en la ruta , si el hijo con el costo minimo no esta , lo agregamos a la ruta y actualizamos 
    #regresamos el nombre del hijo que se eligio para continuar con el trayecto 
    minimo =  costos[hijos[0]]
    for h in hijos :
       # minimo = costos[hijos[0]]
        if costos[h] < minimo and h not in ruta:
            nombre = h
            minimo = costos[h]
    return nombre




def best_first_search(destino,origen,costos):
    ruta = [origen]
    encontrado = False
    guarda = origen
    trayectorias = hijos[guarda]
    while len(trayectorias) and encontrado!= True:
        if destino in ruta :
            encontrado = True
            break
        guarda = mejor_seleccion(trayectorias,costos,ruta)
        #print("Hola")
       # print(guarda)
        trayectorias = hijos[guarda]
        if destino in trayectorias:
            ruta.append(guarda)
            break
        ruta.append(guarda)
    #print(ruta)
    ruta.append(destino)
    ruta.reverse()

    return ruta
r = best_first_search("Coyoacan","Lazaro Cardenas",estimated_cost)
print("Algoritmo best first search")
print(r) 

def astar(origen,destino):
    openList =  set([origen])
    closed = set()
    g= {}
    p = {}
    g[origen] = 0
    p[origen] = origen
    while  len(openList) > 0 :
        n = None
        for v in openList:
            #print(n)
           # if v== None: print("rayos")
            if n == None or g[v]+estimated_cost[v] < g[n] + estimated_cost[n]:
                n=v
        if n == destino or n not in aux or hijos[n] == None  :
            pass
        else:
            for (m,costo) in aux[n]:
                if m not in openList and m  not in closed:
                    openList.add(m)
                    p[m] = n
                    g[m] = g[n] +costo
                else:
                    if g[m]>g[n]+costo:
                        g[m] = g[n]+ costo
                        p[m] = n
                        if m in closed:
                            closed.remove(m)
                            openList.add(m)
        if n == None:
            return []
        if n== destino:
            camino = []
            while p[n] != n:
                camino.append(n)
                n= p[n]
            camino.append(origen)
           # camino.reverse()
            return camino
        openList.remove(n)
        closed.add(n)
    return None
                

r = astar("Lazaro Cardenas","Coyoacan")
print("Algoritmo A*")
print(r)

#print()


