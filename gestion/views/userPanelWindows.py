# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userPanelWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UserPanelFrom(object):
    def setupUi(self, userPanelFrom):
        if not userPanelFrom.objectName():
            userPanelFrom.setObjectName(u"userPanelFrom")
        userPanelFrom.resize(1031, 525)
        self.userTableWidget = QTableWidget(userPanelFrom)
        self.userTableWidget.setObjectName(u"userTableWidget")
        self.userTableWidget.setGeometry(QRect(40, 210, 941, 291))
        self.addUserButton = QPushButton(userPanelFrom)
        self.addUserButton.setObjectName(u"addUserButton")
        self.addUserButton.setGeometry(QRect(40, 30, 81, 81))
        self.addUserButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addUserButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assetes/icons/add-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addUserButton.setIcon(icon)
        self.addUserButton.setIconSize(QSize(80, 80))
        self.addUserButton.setFlat(True)
        self.deleteUserButton = QPushButton(userPanelFrom)
        self.deleteUserButton.setObjectName(u"deleteUserButton")
        self.deleteUserButton.setGeometry(QRect(210, 30, 81, 81))
        self.deleteUserButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteUserButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#ff937d;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assetes/icons/delete-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteUserButton.setIcon(icon1)
        self.deleteUserButton.setIconSize(QSize(80, 80))
        self.deleteUserButton.setFlat(True)
        self.seachUserLineEdit = QLineEdit(userPanelFrom)
        self.seachUserLineEdit.setObjectName(u"seachUserLineEdit")
        self.seachUserLineEdit.setGeometry(QRect(210, 170, 501, 22))
        self.label = QLabel(userPanelFrom)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 170, 151, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.homeButton = QPushButton(userPanelFrom)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(890, 30, 81, 81))
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assetes/icons/pagina-de-inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon2)
        self.homeButton.setIconSize(QSize(80, 80))
        self.homeButton.setFlat(True)
        self.updateButton = QPushButton(userPanelFrom)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(390, 30, 81, 81))
        self.updateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assetes/icons/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon3)
        self.updateButton.setIconSize(QSize(80, 80))
        self.updateButton.setFlat(True)
        self.label_2 = QLabel(userPanelFrom)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(userPanelFrom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 120, 131, 21))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(userPanelFrom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 120, 131, 21))
        self.label_4.setFont(font1)

        self.retranslateUi(userPanelFrom)

        QMetaObject.connectSlotsByName(userPanelFrom)
    # setupUi

    def retranslateUi(self, userPanelFrom):
        userPanelFrom.setWindowTitle(QCoreApplication.translate("userPanelFrom", u"Panel de Usuarios", None))
        self.addUserButton.setText("")
        self.deleteUserButton.setText("")
        self.label.setText(QCoreApplication.translate("userPanelFrom", u"Buscar Usuario:", None))
        self.homeButton.setText("")
        self.updateButton.setText("")
        self.label_2.setText(QCoreApplication.translate("userPanelFrom", u"A\u00f1adir Usuario", None))
        self.label_3.setText(QCoreApplication.translate("userPanelFrom", u"Eliminar Usuario", None))
        self.label_4.setText(QCoreApplication.translate("userPanelFrom", u"Actualizar", None))
    # retranslateUi

