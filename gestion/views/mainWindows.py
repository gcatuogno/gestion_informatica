# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainForm(object):
    def setupUi(self, mainForm):
        if not mainForm.objectName():
            mainForm.setObjectName(u"mainForm")
        mainForm.setWindowModality(Qt.NonModal)
        mainForm.resize(1073, 481)
        self.productButton = QPushButton(mainForm)
        self.productButton.setObjectName(u"productButton")
        self.productButton.setGeometry(QRect(80, 210, 221, 211))
        self.productButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.productButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#c68152;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assetes/icons/gestionProductos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.productButton.setIcon(icon)
        self.productButton.setIconSize(QSize(200, 200))
        self.productButton.setAutoExclusive(False)
        self.productButton.setFlat(True)
        self.supplyButton = QPushButton(mainForm)
        self.supplyButton.setObjectName(u"supplyButton")
        self.supplyButton.setGeometry(QRect(420, 210, 221, 211))
        self.supplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.supplyButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#c68152;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assetes/icons/Gestionproveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supplyButton.setIcon(icon1)
        self.supplyButton.setIconSize(QSize(200, 200))
        self.supplyButton.setFlat(True)
        self.userButton = QPushButton(mainForm)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setGeometry(QRect(740, 210, 221, 211))
        self.userButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.userButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#c68152;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assetes/icons/Gestion Usuarios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userButton.setIcon(icon2)
        self.userButton.setIconSize(QSize(200, 200))
        self.userButton.setFlat(True)
        self.label = QLabel(mainForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 30, 291, 131))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.retranslateUi(mainForm)

        QMetaObject.connectSlotsByName(mainForm)
    # setupUi

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QCoreApplication.translate("mainForm", u"Form", None))
        self.productButton.setText("")
        self.supplyButton.setText("")
        self.userButton.setText("")
        self.label.setText(QCoreApplication.translate("mainForm", u"Panel de Control", None))
    # retranslateUi

