import pandas as pd
import sys
from collections import deque
from math import sin, cos, sqrt, atan2, radians



'''Ejercicio 4.2 Best First Search, A*'''


df = pd.DataFrame()
df = pd.read_csv('metro.csv')
df = df.iloc[: , 1:]

metro = df['origen'].tolist()
metro = [*set(metro)]

result = [(x,y,z) for x,y,z in zip(df['origen'], df['destino'], df['longitud'])]
print(len(metro))

aux = {i:[] for i in metro}
for i in result:
    aux[i[0]].append((i[1], i[2]))

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
result = [(w,x,y,z) for  w,x,y,z in zip(dl['linea'],dl['nombre'], dl['lat'], dl['lon'])]

def busca_destino(nombre):
    cons = (None,None,None,None)
    for r in result :
        if r[1] == nombre:
            cons = r
            break
    return cons

coordenadas = {}
i = 0
for r in result :
    if r[1] not in coordenadas :
        coordenadas[r[1]]  =(r[2],r[3])
    else:
        i+=1
estimated_cost  = {}
#lazaro = (cons[2],cons[3])
obj =  busca_destino("Lazaro Cardenas")
print(obj)
#Tenemos ls costos estimados utilizando una formula que calcula las distancias entre puntos geograficos. En este caso de una estacion a Lazaro Cardenas 
for k in coordenadas:
    if k not in estimated_cost :
        estimated_cost[k] =  distances(coordenadas[k],(obj[2],obj[3]))
        
    else:
        continue
#print(estimated_cost)

def mejor_seleccion(minimo,hijos,costos,ruta):
    return
def best_first_search(origen,destino):
    return 



 

#print()


