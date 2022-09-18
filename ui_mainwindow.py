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
        MainWindow.resize(852, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 852, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.labelA.setText("")
        self.labelB.setText("")
    # retranslateUi

