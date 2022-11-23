import math

cadena1 = "010101010101101101110110010101010010111010"
cadena2 = "000000000000000000000000000000000000000000"
cadena3 = "010101010101101101110110010101010010111010"

def entropia(cadena):

    # Calcula la probabilidad de los caracteres en la cadena
    prob = [ float(cadena.count(c)) / len(cadena) for c in dict.fromkeys((cadena)) ]

    # Calcula la entropia de Shanon
    entropy = (-1) * (sum([ p * math.log(p) / math.log(2.0) for p in prob ]))

    if entropy == 0:
        entropy = (sum([ p * math.log(p) / math.log(2.0) for p in prob ]))

    return entropy

print("La entropia de la primera cadena es" , entropia(cadena1))
print("La entropia de la segunda cadena es" , entropia(cadena2))
print("La entropia de la tercera cadena es", entropia(cadena3))

