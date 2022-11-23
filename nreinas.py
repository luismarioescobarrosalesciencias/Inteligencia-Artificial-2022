import random
import numpy as np
import matplotlib.pyplot as plt
class cromosoma:
    def __init__(self,codigo_genetico,fitness):
        self.codigo_genetico=codigo_genetico
        self.fitness=fitness
    # Metodo que devuelve el fitness de un cromosoma
    def get_fitness(self):
        return self.fitness
    # Metodo que devuelve el codigo genetico de un cromosoma
    def get_codigo_genetico(self):
        return self.codigo_genetico
        
class n_reinas:
    def __init__(self, reinas):
        self.codigo_genetico = range(reinas)
    # Metodo que genera la poblacion inicial de individuos
    def genera_poblacion_inicial(self):
        poblacion_inicial=[]
        for n in range(400):
            individuo = self.genera_individuo()
            poblacion_inicial.append(individuo)
        return poblacion_inicial
    # Metodo que genera un nuevo individuo a partir de mezclar el gen primigeneo y obtener su atributo fitness
    def genera_individuo(self):
        nuevo_codigo_genetico = self.mezcla_gen_inicial() 
        fitness = self.obten_fitness(nuevo_codigo_genetico)
        return cromosoma(nuevo_codigo_genetico, fitness)
    # Metodo que recombina el gen inicial([0,1,2,3,4,5,6,7]) en un nuevo gen
    def mezcla_gen_inicial(self):
        return random.sample(self.codigo_genetico, len(self.codigo_genetico))
    # Metodo que obtiene el fitness mediante la resta de conflictos maximos y los conflictos de un individuo
    def obten_fitness(self, gen):
        conflictos = self.encuentra_conflictos(gen)
        return conflictos
    # Metodo que encuentra todos los conflictos posibles entre reinas(horizontal, diagonal ascendiente y diagonal
    # descendiente)
    def encuentra_conflictos(self, gen):
        conflictos_h = self.encuentra_conflictos_h(gen)
        conflictos_da = self.encuentra_conflictos_da(gen)
        conflictos_dd = self.encuentra_conflictos_dd(gen)
        return conflictos_h+conflictos_da+conflictos_dd
    # Metodo que encuentra conflictos en la linea horizontal entre reinas, se verifica la aparicion de 
    # las reinas en la misma fila
    def encuentra_conflictos_h(self, gen):
        conflictos = 0
        conflictos_lista = [0]*len(gen)
        for n in range(len(gen)):
            for m in range(len(gen)):
                if n==gen[m]:
                    agrega_n = conflictos_lista[n]+1
                    conflictos_lista[n]= agrega_n 
        for n in range(len(gen)):
            if conflictos_lista[n] > 1:
                agrega_n = conflictos_lista[n]
                conflictos = conflictos + agrega_n
        
        return conflictos
    # Metodo que encuentra conflictos en la diagonal descendiente con la formula del indice D = C - F 
    def encuentra_conflictos_dd(self, gen):
        conflictos = 0
        conflictos_lista = {}
        # Llenamos el diccionario
        for n in range((len(gen))):
            conflictos_lista[n] = 0 # Positivos
            conflictos_lista[-n] = 0 # Negativos
            conflictos_lista[0] = 0 # Para Cero
        # Recorremos nuestro gen y a partir de ahi por cada aparicion que haya de una reina en 
        # la diagonal con un indice en especifico sumamos una aparicion
        for n in range(len(gen)):
            columna = n
            fila = gen[n]
            indice_diagonal = columna - fila
            agrega_n = conflictos_lista.get(indice_diagonal)+1
            conflictos_lista[indice_diagonal] = agrega_n
        # Recorremos el diccionario de apariciones, si hay mas de una reina en la diagonal agregamos el numero
        # de reinas en conflicto
        for n in range((len(gen))):
            if conflictos_lista[n] > 1:# Positivos
                agrega_n = conflictos_lista[n]
                conflictos = conflictos + agrega_n
            if conflictos_lista[-n] > 1:# Negativos
                agrega_mn = conflictos_lista[-n]
                conflictos = conflictos + agrega_mn
            if conflictos_lista[0] > 1:# Para cero
                agrega_z = conflictos_lista[0]
                conflictos = conflictos + agrega_z
        return conflictos
    # Metodo que encuentra conflictos en la diagonal ascendiente con la formula del indice D = C + F 
    def encuentra_conflictos_da(self, gen):
        conflictos = 0
        conflictos_lista = {}
        # Llenamos el diccionario
        for n in range(((len(gen))*2)-1):
            conflictos_lista[n] = 0 # Positivos
        # Recorremos nuestro gen y a partir de ahi por cada aparicion que haya de una reina en 
        # la diagonal con un indice en especifico sumamos una aparicion
        for n in range(len(gen)):
            columna = n
            fila = gen[n]
            indice_diagonal = columna + fila
            agrega_n = conflictos_lista.get(indice_diagonal)+1
            conflictos_lista[indice_diagonal] = agrega_n
        # Recorremos el diccionario de apariciones, si hay mas de una reina en la diagonal agregamos el numero
        # de reinas en conflicto
        for n in range(((len(gen))*2)-1):
            if conflictos_lista[n] > 1:# Positivos
                agrega_n = conflictos_lista[n]
                conflictos = conflictos + agrega_n
        return conflictos
    # Metodo que selecciona de forma natural un individuo de la poblacion mediante una condicion de fitness maximo
    # en la que si el individuo tiene menor fitness entonces es elegido
    def seleccion(self, poblacion,fitness_maximo):
        i=0
        while True:
            candidato = random.choice(poblacion)
            if candidato.get_fitness() < fitness_maximo:
                return candidato
            i=i+1
            if i == 1000:#Para este punto no es posible seguir generando combinaciones geneticas
                return cromosoma([-1]*len(self.codigo_genetico), -1)
    # Metodo que combina el codigo genetico entre dos individuos para la creacion de uno nuevo
    def reproduccion(self, madre, padre):
        n=random.randint(0, len(madre.codigo_genetico))
        hijo_codigo_genetico = madre.codigo_genetico[:n] + padre.codigo_genetico[n:]
        fitness=self.obten_fitness(hijo_codigo_genetico)
        return cromosoma(hijo_codigo_genetico, fitness)
    # Metodo que muta a un individuo con un numero al azar
    def mutacion(self, individuo):
        n=random.randint(0, len(individuo.codigo_genetico)-1)        
        individuo.codigo_genetico[n]=n
        individuo.fitness = self.obten_fitness(individuo.codigo_genetico)
    # Metodo que genera una condicion de adaptacion, en este caso el fitness mayor de todos los de la poblacion
    def adaptacion(self, poblacion):
        fitness_maximo = 0
        lista_fitness = []
        for n in range(len(poblacion)):
            lista_fitness.append(poblacion[n].get_fitness())
        fitness_maximo = max(lista_fitness)
        return fitness_maximo
    # Metodo que soluciona el problema de las n reinas
    def solucion(self, poblacion):
        fitness_maximo = self.adaptacion(poblacion)
        hijo = cromosoma([0]*len(self.codigo_genetico), 0)
        while True:
            for n in range(len(poblacion)):
                print("\nAños restantes para la extincion (Fitness maximo) --------------------->",fitness_maximo)
                padre=self.seleccion(poblacion,fitness_maximo)
                print("Padre -> { Fitness:",padre.get_fitness(),"| Codigo Genetico:", padre.get_codigo_genetico(),"}")
                madre=self.seleccion(poblacion,fitness_maximo)
                print("Madre -> { Fitness:",madre.get_fitness(),"| Codigo Genetico:", madre.get_codigo_genetico(),"}")
                if padre.get_fitness() == -1 or madre.get_fitness() == -1:
                    print("\n-------------------- Se extinguieron los individuos ._. --------------------\n")
                    print("El descendiente que mas se acerco fue :")
                    return hijo
                hijo=self.reproduccion(padre, madre)
                print("Hijo  -> { Fitness:",hijo.get_fitness(),"| Codigo Genetico:", hijo.get_codigo_genetico(),"}")
                if hijo.fitness <= 0:
                    print("\n-------------------- Obtuvimos una respuesta >3< --------------------\n")
                    print("La configuracion siguiente resuelve el problema de las n reinas :")
                    return hijo
                if hijo.fitness < fitness_maximo:
                    fitness_maximo = fitness_maximo - 1
    # Metodo que encuentra la solucion al problema de las n-reinas
    def busca_solucion(self):
        poblacion_inicial=self.genera_poblacion_inicial()
        self.imprime_tablero(self.solucion(poblacion_inicial).get_codigo_genetico())
    def imprime_tablero(self,codigo_g):
        print("Hijo  -> { Codigo Genetico:", codigo_g,"}")
        tablero = np.zeros((len(codigo_g), len(codigo_g)), dtype=int)
        color = False
        for n in range (len(codigo_g)):
            for m in range(len(codigo_g)):
                if color == False:
                    tablero[n][m] = 0
                    color = True
                else:
                    tablero[n][m] = 1
                    color = False
            if color == False:
                color = True
            else:
                color = False
                    
        for n in range (len(codigo_g)):
            tablero[codigo_g[n]][n] = 2
        
        plt.matshow(tablero)
        plt.show()
    
        
            
        
if __name__=="__main__":
    
    solucion = n_reinas(8)     
    solucion.busca_solucion()

    
