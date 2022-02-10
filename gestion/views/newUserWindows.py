# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newUserWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewUserForm(object):
    def setupUi(self, newUserForm):
        if not newUserForm.objectName():
            newUserForm.setObjectName(u"newUserForm")
        newUserForm.resize(464, 455)
        self.userNameLineEdit = QLineEdit(newUserForm)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setGeometry(QRect(60, 90, 361, 31))
        self.userPaswordLineEdit = QLineEdit(newUserForm)
        self.userPaswordLineEdit.setObjectName(u"userPaswordLineEdit")
        self.userPaswordLineEdit.setGeometry(QRect(60, 170, 361, 31))
        self.levelComboBox = QComboBox(newUserForm)
        self.levelComboBox.setObjectName(u"levelComboBox")
        self.levelComboBox.setGeometry(QRect(60, 250, 361, 31))
        self.label = QLabel(newUserForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 60, 201, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(newUserForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 140, 201, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(newUserForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 220, 201, 21))
        self.label_3.setFont(font)
        self.cancelButton = QPushButton(newUserForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(100, 330, 81, 81))
        self.cancelButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#ff8b8b;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assetes/icons/button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setIconSize(QSize(80, 80))
        self.cancelButton.setFlat(True)
        self.addUserButton = QPushButton(newUserForm)
        self.addUserButton.setObjectName(u"addUserButton")
        self.addUserButton.setGeometry(QRect(260, 330, 81, 81))
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
        icon1 = QIcon()
        icon1.addFile(u"./assetes/icons/add-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addUserButton.setIcon(icon1)
        self.addUserButton.setIconSize(QSize(80, 80))
        self.addUserButton.setFlat(True)

        self.retranslateUi(newUserForm)

        QMetaObject.connectSlotsByName(newUserForm)
    # setupUi

    def retranslateUi(self, newUserForm):
        newUserForm.setWindowTitle(QCoreApplication.translate("newUserForm", u"Nuevo Usuario", None))
        self.label.setText(QCoreApplication.translate("newUserForm", u"Nombre de Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("newUserForm", u"Clave de Acceso", None))
        self.label_3.setText(QCoreApplication.translate("newUserForm", u"Nivel de Acceso", None))
        self.cancelButton.setText("")
        self.addUserButton.setText("")
    # retranslateUi

