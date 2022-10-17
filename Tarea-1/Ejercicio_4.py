import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('./resources/metro.csv')
df = df.iloc[: , 1:]

metro = df['origen'].tolist()
metro = [*set(metro)]

result = [(x,y,z) for x,y,z in zip(df['origen'], df['destino'], df['longitud'])]
print(len(metro))

aux = {i:[] for i in metro}
for i in result:
    aux[i[0]].append((i[1], i[2]))

print(aux)
print()
print(aux['Pantitlán'])