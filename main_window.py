from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtCore import Slot, QCoreApplication
from PySide2 import QtGui, QtCore
from src.aspiradora import Aspiradora, cuartoA, cuartoB, aspiradora
from ui_mainwindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Práctica 1- Simulador Aspiradora')

        pixmapAspiradora = QtGui.QPixmap(f'img/aspiradora.png').scaled(400,500, QtCore.Qt.KeepAspectRatio)
        self.ui.labelA.setPixmap(pixmapAspiradora)

        pixmapBasuraAspiradora = QtGui.QPixmap(f'img/aspiradora_basura.jpg').scaled(400,500, QtCore.Qt.KeepAspectRatio)
        self.ui.labelB.setPixmap(pixmapBasuraAspiradora)

        pixmapBasura = QtGui.QPixmap(f'img/basura.jpeg').scaled(400,500, QtCore.Qt.KeepAspectRatio)
        self.ui.labelB.setPixmap(pixmapBasura)