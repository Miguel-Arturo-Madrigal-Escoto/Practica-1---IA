
from src.cuarto import Cuarto

class Aspiradora(Cuarto):

    def __init__(self, cuarto: Cuarto):
        self.posicion      = 'izq'
        self.cuarto_actual = cuarto
    

    def limpiar(self):
        self.cuarto_actual.estado = 0

    
    def izquierda(self, cuarto: Cuarto):
        self.posicion      = 'izq'
        self.cuarto_actual = cuarto


    def derecha(self, cuarto: Cuarto):
        self.posicion       = 'der'
        self.cuarto_actual  = cuarto



