# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(639, 462)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/login.png", QSize(), QIcon.Normal, QIcon.Off)
        loginForm.setWindowIcon(icon)
        self.selectTypeUserComboBox = QComboBox(loginForm)
        self.selectTypeUserComboBox.setObjectName(u"selectTypeUserComboBox")
        self.selectTypeUserComboBox.setGeometry(QRect(370, 220, 201, 31))
        self.userLineEdit = QLineEdit(loginForm)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(230, 270, 341, 31))
        self.loginButton = QPushButton(loginForm)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(430, 370, 141, 41))
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.Titlelabel = QLabel(loginForm)
        self.Titlelabel.setObjectName(u"Titlelabel")
        self.Titlelabel.setGeometry(QRect(190, 130, 371, 71))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Titlelabel.setFont(font)
        self.label = QLabel(loginForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 270, 91, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.paswordLineEdit = QLineEdit(loginForm)
        self.paswordLineEdit.setObjectName(u"paswordLineEdit")
        self.paswordLineEdit.setGeometry(QRect(230, 320, 341, 31))
        self.label_2 = QLabel(loginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 320, 61, 31))
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(loginForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 50, 90, 90))
        icon1 = QIcon()
        icon1.addFile(u"./assetes/icons/gestion-de-datos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(90, 90))
        self.pushButton.setFlat(True)
        self.label_3 = QLabel(loginForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 215, 271, 31))
        self.label_3.setFont(font1)
        self.mensageLogin = QLabel(loginForm)
        self.mensageLogin.setObjectName(u"mensageLogin")
        self.mensageLogin.setGeometry(QRect(210, 30, 371, 71))
        self.mensageLogin.setFont(font)

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Login", None))
        self.loginButton.setText(QCoreApplication.translate("loginForm", u"Login", None))
        self.Titlelabel.setText(QCoreApplication.translate("loginForm", u"Suministros Informaticos", None))
        self.label.setText(QCoreApplication.translate("loginForm", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("loginForm", u"Clave:", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("loginForm", u"Seleccione Nivel de Acceso:", None))
        self.mensageLogin.setText("")
    # retranslateUi

