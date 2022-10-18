#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio_2.py
----------------
Ejercicio 2 Agentes

Equipo:
    - Anzaldúa Díaz Andrea Fernanda
    - Escobar Rosales Luis Mario
    - Garcia Toxqui Demian Oswaldo
    - Padilla Lara Diego Javier
"""

import entornos_f
from random import choice



class DosCuartos(entornos_f.Entorno):
    """
    Clase para un entorno de dos cuartos. 
    Muy sencilla solo regrupa métodos.
    El estado se define como (robot, A, B)
    donde robot puede tener los valores "A", "B"
    A y B pueden tener los valores "limpio", "sucio"
    Las acciones válidas en el entorno son 
        ("ir_A", "ir_B", "limpiar", "nada").
    
    Todas las acciones son válidas en todos los estados.
    Los sensores es una tupla (robot, limpio?)
    con la ubicación del robot y el estado de limpieza
    """
    def acción_legal(self, acción):
        return acción in ("subir", "bajar", "ir_derecha", "ir_izquierda", "limpiar", "nada")

    def transición(self, estado, acción):
        robot, a, b, c, d, e, f = estado
        if a == b == c == d == e == f == "limpio" and acción is "nada":
            c_local = 0 
        elif acción is "ir_derecha" or "ir_izquierda" or "limpiar":
            c_local = 1
        else:
            c_local = 2

        return ((estado, c_local) if a is "nada" else
                (("B", a, b,c,d,e,f), c_local) if acción is "ir_derecha" and robot == "A" else
                (("C", a, b,c,d,e,f), c_local) if acción is "ir_derecha" and robot == "B" else
                (("B", a, b,c,d,e,f), c_local) if acción is "ir_izquierda" and robot == "C" else
                (("A", a, b,c,d,e,f), c_local) if acción is "ir_izquierda" and robot == "B" else
                (("E", a, b,c,d,e,f), c_local) if acción is "ir_derecha" and robot == "D" else
                (("F", a, b,c,d,e,f), c_local) if acción is "ir_derecha" and robot == "E" else
                (("E", a, b,c,d,e,f), c_local) if acción is "ir_izquierda" and robot == "F" else
                (("D", a, b,c,d,e,f), c_local) if acción is "ir_izquierda" and robot == "E" else
                (("D", a, b,c,d,e,f), c_local) if acción is "bajar" and robot == "A" else
                (("A", a, b,c,d,e,f), c_local) if acción is "subir" and robot == "D" else
                (("F", a, b,c,d,e,f), c_local) if acción is "bajar" and robot == "C" else
                (("C", a, b,c,d,e,f), c_local) if acción is "subir" and robot == "F" else
                ((robot, "limpio", b,c,d,e,f), c_local) if robot is "A" else
                ((robot, a, "limpio",c,d,e,f), c_local) if robot is "B" else
                ((robot, a, b,"limpio",d,e,f), c_local) if robot is "C" else
                ((robot, a, b, c, "limpio",e,f), c_local) if robot is "D" else
                ((robot, a, b, c, d ,"limpio",f), c_local) if robot is "E" else
                ((robot, a, b, c, d ,e ,"limpio"), c_local))

    def percepción(self, estado):
        return estado[0], estado[" ABCDEF".find(estado[0])]


class AgenteAleatorio(entornos_f.Agente):
    """
    Un agente que solo regresa una accion al azar entre las acciones legales
    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, _):
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos_f.Agente):
    """
    Un agente reactivo simple
    """
    def programa(self, percepción):
        robot, situación = percepción
        return ('limpiar' if situación == 'sucio' else
                'ir_derecha' if robot == 'B' else
                'bajar' if robot == 'C' else
                'ir_izquierda' if robot == 'F' else
                'ir_izquierda' if robot == 'E' else
                'subir' if robot == 'D' else
                'ir_derecha')


class AgenteReactivoModeloDosCuartos(entornos_f.Agente):
    """
    Un agente reactivo basado en modelo
    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos
        la tupla se compone por estado del robot y el estado de los cuartos
        """
        self.modelo = ['A', 'sucio', 'sucio', 'sucio','sucio','sucio', 'sucio']

    def programa(self, percepción):
        robot, situación = percepción

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[' ABCDEF'.find(robot)] = situación

        # Decide sobre el modelo interno
        a, b, c,d,e,f = self.modelo[1], self.modelo[2], self.modelo[3],self.modelo[4], self.modelo[5], self.modelo[6]
        return ('nada' if a == b == c == d == e == f == 'limpio' else
                'limpiar' if situación == 'sucio' else
                'ir_derecha' if robot == 'B' else
                'bajar' if robot == 'C' else
                'ir_izquierda' if robot == 'F' else
                'ir_izquierda' if robot == 'E' else
                'subir' if robot == 'D' else
                'ir_derecha')


def prueba_agente(agente):
    entornos_f.imprime_simulación(
        entornos_f.simulador(
            DosCuartos(),
            agente,
            ["A", "sucio", "sucio","sucio","sucio","sucio", "sucio"],
            100
        ),
        ["A", "sucio", "sucio","sucio","sucio","sucio", "sucio"]
    )

def test():
    """
    Prueba del entorno y los agentes
    """
    print("Prueba del entorno con un agente aleatorio")
    prueba_agente(AgenteAleatorio(["subir", "bajar", "ir_derecha", "ir_izquierda", "limpiar", "nada"]))

    print("Prueba del entorno con un agente reactivo")
    prueba_agente(AgenteReactivoDoscuartos())

    print("Prueba del entorno con un agente reactivo con modelo")
    prueba_agente(AgenteReactivoModeloDosCuartos())
    

if __name__ == "__main__":
    test()