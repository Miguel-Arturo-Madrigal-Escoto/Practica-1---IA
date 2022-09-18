

class Aspiradora:

    def __init__(self, posicion: str, estado: int):
        self.posicion = posicion   

        self.cuarto_actual['A'] = estado
        self.cuarto_actual['B'] = estado

        if posicion == 'izq':
            self.cuarto = 'A'
        else:
            self.cuarto = 'B'
        

    

    def limpiar(self):
        self.cuarto_actual[self.cuarto] = 0

    
    def izquierda(self):
        self.posicion  = 'izq'
        self.cuarto = 'A' 


    def derecha(self):
        self.posicion  = 'der'
        self.cuarto = 'B' 



