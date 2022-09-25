from time import sleep
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QCoreApplication
from PySide2 import QtGui, QtCore
from src.aspiradora import Aspiradora

from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Práctica 1- Simulador Aspiradora')

        self.pixmapAspiradoraBasura = QtGui.QPixmap(f'img/aspiradora_basura.jpg').scaled(400,500, QtCore.Qt.KeepAspectRatio)
        #self.ui.labelA.setPixmap(pixmapAspiradoraBasura)

        self.pixmapAspiradora = QtGui.QPixmap(f'img/aspiradora.png').scaled(400,500, QtCore.Qt.KeepAspectRatio)

        self.pixmapBasura = QtGui.QPixmap(f'img/basura.jpeg').scaled(400,500, QtCore.Qt.KeepAspectRatio)
        #self.ui.labelB.setPixmap(pixmapBasura)
        self.aspiradora = Aspiradora()

        self.ui.pushButtonStart.clicked.connect(self.start)
        #self.estadoActual()
        

    @Slot()
    def start(self):
        self.ui.labelA.clear()
        self.ui.labelB.clear()
        self.aspiradora = Aspiradora()
        self.init()
    
    def estadoActual(self):
        self.ui.labelA.clear()
        self.ui.labelB.clear()

        if self.aspiradora.cuartos['A'] == 1 and self.aspiradora.cuarto == 'B':
            self.ui.labelA.setPixmap(self.pixmapBasura)
        
        if self.aspiradora.cuartos['B'] == 1 and self.aspiradora.cuarto == 'A':
            self.ui.labelB.setPixmap(self.pixmapBasura)
        
        if self.aspiradora.cuartos['A'] == 1 and self.aspiradora.cuarto == 'A':
            self.ui.labelA.setPixmap(self.pixmapAspiradoraBasura)
        
        if self.aspiradora.cuartos['B'] == 1 and self.aspiradora.cuarto == 'B':
            self.ui.labelB.setPixmap(self.pixmapAspiradoraBasura)
        
        if self.aspiradora.cuartos['B'] == 0 and self.aspiradora.cuarto == 'B':
            self.ui.labelB.setPixmap(self.pixmapAspiradora)

        if self.aspiradora.cuartos['A'] == 0 and self.aspiradora.cuarto == 'A':
            self.ui.labelA.setPixmap(self.pixmapAspiradora)

        
    def actualizar(self):
        QCoreApplication.processEvents()
        sleep(1)
        self.estadoActual()

    def datosFinales(self):
        self.ui.labelAspiradas.setText(str(self.aspiradora.puntajes['aspiradas']))
        self.ui.labelDesplazamientos.setText(str(self.aspiradora.puntajes['desplazamientos']))
        self.ui.labelMovimientosTotales.setText(str(self.aspiradora.movimientos))
        self.ui.labelPromedio.setText(f"{ 0 if self.aspiradora.movimientos == 0 else (self.aspiradora.puntajes['aspiradas'] + self.aspiradora.puntajes['desplazamientos'])/self.aspiradora.movimientos }")

    def init(self):       
          
        while self.aspiradora.cuartos['A'] != 0 or self.aspiradora.cuartos['B'] != 0:
            print('Habitación A limpia' if self.aspiradora.cuartos['A'] == 0 else 'Habitación A sucia')
            print('Habitación B limpia' if self.aspiradora.cuartos['B'] == 0 else 'Habitación B sucia')
            self.actualizar()
            if self.aspiradora.cuartos[self.aspiradora.cuarto] == 1 and self.aspiradora.posicion == 'izq':       
                print('Aspirando habitación A')
                self.aspiradora.limpiar()
                self.actualizar()                
                self.aspiradora.derecha()
                print('Aspirandora moviendose a la derecha')

            elif self.aspiradora.cuartos[self.aspiradora.cuarto] == 1 and self.aspiradora.posicion == 'der':
                print('Aspirando habitación B')
                self.aspiradora.limpiar()
                self.actualizar()
                self.aspiradora.izquierda()
                print('Aspirandora moviendose a la izquierda')
 
            elif self.aspiradora.cuartos[self.aspiradora.cuarto] == 0 and self.aspiradora.posicion == 'izq':
                self.aspiradora.derecha()
                print('Aspirandora moviendose a la derecha')
                           
            elif self.aspiradora.cuartos[self.aspiradora.cuarto] == 0 and self.aspiradora.posicion == 'der':
                self.aspiradora.izquierda()
                print('Aspirandora moviendose a la izquierda')
        
            elif self.aspiradora.cuartos['A'] == 0 and self.aspiradora.cuartos['B'] == 0:
                print('Ya quedó')         
                      
        print('Ya están limpias')
        self.estadoActual()
        self.datosFinales()
        



