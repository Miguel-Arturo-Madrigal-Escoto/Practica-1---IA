

import random

class Aspiradora:

    def __init__(self):
        self.posicion = random.choice(['izq', 'der'])
        self.cuartos = {}

        # ! aspirada: 10pts
        # ? desplazamiento: 5pts
        self.puntajes = {
            'aspiradas'      : 0,
            'desplazamientos': 0
        } 

        self.movimientos = 0

        self.cuartos['A'] = random.randint(0, 1)
        self.cuartos['B'] = random.randint(0, 1)

        if self.posicion == 'izq':
            self.cuarto = 'A'
        else:
            self.cuarto = 'B'
        

    def limpiar(self):
        self.cuartos[self.cuarto] = 0
        self.movimientos += 1
        self.puntajes['aspiradas'] += 10

    
    def izquierda(self):
        self.posicion  = 'izq'
        self.cuarto = 'A' 
        self.movimientos += 1
        self.puntajes['desplazamientos'] += 5


    def derecha(self):
        self.posicion  = 'der'
        self.cuarto = 'B' 
        self.movimientos += 1
        self.puntajes['desplazamientos'] += 5



