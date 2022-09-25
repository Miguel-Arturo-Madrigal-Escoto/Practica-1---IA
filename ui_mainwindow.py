# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 794)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelA = QLabel(self.centralwidget)
        self.labelA.setObjectName(u"labelA")
        self.labelA.setMinimumSize(QSize(400, 500))
        self.labelA.setMaximumSize(QSize(400, 500))
        self.labelA.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelA.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelA)

        self.labelB = QLabel(self.centralwidget)
        self.labelB.setObjectName(u"labelB")
        self.labelB.setMinimumSize(QSize(400, 500))
        self.labelB.setMaximumSize(QSize(400, 500))
        self.labelB.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelB.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelB)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.labelDesplazamientos = QLabel(self.centralwidget)
        self.labelDesplazamientos.setObjectName(u"labelDesplazamientos")
        self.labelDesplazamientos.setMinimumSize(QSize(0, 30))
        self.labelDesplazamientos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.labelDesplazamientos)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.labelAspiradas = QLabel(self.centralwidget)
        self.labelAspiradas.setObjectName(u"labelAspiradas")
        self.labelAspiradas.setMinimumSize(QSize(0, 30))
        self.labelAspiradas.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.labelAspiradas)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.labelPromedio = QLabel(self.centralwidget)
        self.labelPromedio.setObjectName(u"labelPromedio")
        self.labelPromedio.setMinimumSize(QSize(0, 30))
        self.labelPromedio.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.labelPromedio)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.labelMovimientosTotales = QLabel(self.centralwidget)
        self.labelMovimientosTotales.setObjectName(u"labelMovimientosTotales")
        self.labelMovimientosTotales.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.labelMovimientosTotales)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.bateria = QProgressBar(self.centralwidget)
        self.bateria.setObjectName(u"bateria")
        self.bateria.setValue(100)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.bateria)


        self.gridLayout.addLayout(self.formLayout_4, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButtonStart = QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.horizontalLayout.addWidget(self.pushButtonStart)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.labelA.setText("")
        self.labelB.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                   Desplazamientos  (5 pts):", None))
        self.labelDesplazamientos.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"                             Aspiradas (10 pts):", None))
        self.labelAspiradas.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"                                           Promedio:", None))
        self.labelPromedio.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"                         Movimientos totales: ", None))
        self.labelMovimientosTotales.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"                                               Bater\u00eda:", None))
        self.label.setText("")
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_4.setText("")
    # retranslateUi

