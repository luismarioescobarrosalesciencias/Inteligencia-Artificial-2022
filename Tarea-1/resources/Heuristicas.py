from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import sys
from collections import deque
#point = (lat,long )
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

#leer el csv 


df = pd.DataFrame()
df = pd.read_csv('LineasMetro.csv')
#df = pd.read_csv('./resources/LineasMetro.csv')
df = df.iloc[: , 1:5]
linea = df['nombre'].tolist()
linea = [*set(linea)]
result = [(w,x,y,z) for  w,x,y,z in zip(df['linea'],df['nombre'], df['lat'], df['lon'])]
cons = (None,None,None,None)

for r in result :
    if r[1] == "Lazaro Cardenas":
        cons = r
        break
coordenadas = {}
i = 0
for r in result :
    if r[1] not in coordenadas :
        coordenadas[r[1]]  =(r[2],r[3])
    else:
        i+=1
estimated_cost  = {}
lazaro = (cons[2],cons[3])
print(lazaro)
#print(lazaro_lat,lazaro_lon)
for k in coordenadas:
    if k not in estimated_cost :
        estimated_cost[k] =  distances(coordenadas[k],lazaro)
        
    else:
        continue
 
print(len(valores))

'''
dic = {}
for line in result :
    if line[1] in dic:
        dic[line[1]]+=1
    else:
        dic[line[1]] =1
print(dic)
list2 =  [node for node in dic if dic[node]>1]
print(list2)
print(len(list2))

print("llalalal")
print(len(metro))
suma=0
for n in list2 :
    print(n,dic[n])
    suma+=  dic[n]
print(suma)



'''