

class Aspiradora:

    def __init__(self, posicion: str, estado: int):
        self.posicion = posicion
        if posicion == 'izq':
            self.cuarto = 'A'
        else:
            self.cuarto = 'B'
        self.cuarto_actual[self.cuarto] = estado
    

    def limpiar(self):
        self.cuarto_actual[self.cuarto] = 0

    
    def izquierda(self):
        self.posicion  = 'izq'
        self.cuarto = 'A' 


    def derecha(self):
        self.posicion  = 'der'
        self.cuarto = 'B' 



