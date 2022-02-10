# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editSupplyWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditSupplyForm(object):
    def setupUi(self, editSupplyForm):
        if not editSupplyForm.objectName():
            editSupplyForm.setObjectName(u"editSupplyForm")
        editSupplyForm.resize(903, 487)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        editSupplyForm.setWindowIcon(icon)
        self.nameLineEdit = QLineEdit(editSupplyForm)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(210, 140, 641, 41))
        self.label = QLabel(editSupplyForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 140, 141, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.cifLineEdit = QLineEdit(editSupplyForm)
        self.cifLineEdit.setObjectName(u"cifLineEdit")
        self.cifLineEdit.setGeometry(QRect(210, 200, 241, 31))
        self.label_2 = QLabel(editSupplyForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 200, 41, 31))
        self.label_2.setFont(font)
        self.locationLineEdit = QLineEdit(editSupplyForm)
        self.locationLineEdit.setObjectName(u"locationLineEdit")
        self.locationLineEdit.setGeometry(QRect(210, 260, 641, 31))
        self.label_6 = QLabel(editSupplyForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 260, 101, 31))
        self.label_6.setFont(font)
        self.label_8 = QLabel(editSupplyForm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 60, 341, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.saveButton = QPushButton(editSupplyForm)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(610, 380, 81, 91))
        self.saveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveButton.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u"./assetes/icons/floppy-disk.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QSize(80, 71))
        self.saveButton.setFlat(True)
        self.cancelButton = QPushButton(editSupplyForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(730, 380, 81, 91))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#ff9090;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assetes/icons/button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)
        self.cancelButton.setIconSize(QSize(80, 71))
        self.cancelButton.setFlat(True)
        self.label_4 = QLabel(editSupplyForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 310, 91, 31))
        self.label_4.setFont(font)
        self.phoneLineEdit = QLineEdit(editSupplyForm)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setGeometry(QRect(210, 310, 241, 31))

        self.retranslateUi(editSupplyForm)

        QMetaObject.connectSlotsByName(editSupplyForm)
    # setupUi

    def retranslateUi(self, editSupplyForm):
        editSupplyForm.setWindowTitle(QCoreApplication.translate("editSupplyForm", u"Editar Proveedor", None))
        self.label.setText(QCoreApplication.translate("editSupplyForm", u"Razon Social:", None))
        self.label_2.setText(QCoreApplication.translate("editSupplyForm", u"CIF:", None))
        self.label_6.setText(QCoreApplication.translate("editSupplyForm", u"Direccion:", None))
        self.label_8.setText(QCoreApplication.translate("editSupplyForm", u"Editar Proveedor", None))
        self.saveButton.setText("")
        self.cancelButton.setText("")
        self.label_4.setText(QCoreApplication.translate("editSupplyForm", u"Telefono:", None))
    # retranslateUi

