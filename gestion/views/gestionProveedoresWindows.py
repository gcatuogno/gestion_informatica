# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestionProveedoresWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class GestionDeProveedoresForm(object):
    def setupUi(self, gestionDeProveedoresForm):
        if not gestionDeProveedoresForm.objectName():
            gestionDeProveedoresForm.setObjectName(u"gestionDeProveedoresForm")
        gestionDeProveedoresForm.resize(2269, 1146)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/gestion-de-datos.png", QSize(), QIcon.Normal, QIcon.Off)
        gestionDeProveedoresForm.setWindowIcon(icon)
        self.addSupplyButton = QPushButton(gestionDeProveedoresForm)
        self.addSupplyButton.setObjectName(u"addSupplyButton")
        self.addSupplyButton.setEnabled(True)
        self.addSupplyButton.setGeometry(QRect(90, 60, 91, 101))
        self.addSupplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSupplyButton.setAcceptDrops(False)
        self.addSupplyButton.setStyleSheet(u"QPushButton:hover\n"
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
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assetes/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addSupplyButton.setIcon(icon1)
        self.addSupplyButton.setIconSize(QSize(80, 80))
        self.addSupplyButton.setAutoDefault(False)
        self.addSupplyButton.setFlat(True)
        self.deleteSupplyButton = QPushButton(gestionDeProveedoresForm)
        self.deleteSupplyButton.setObjectName(u"deleteSupplyButton")
        self.deleteSupplyButton.setEnabled(True)
        self.deleteSupplyButton.setGeometry(QRect(480, 60, 91, 101))
        self.deleteSupplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteSupplyButton.setAcceptDrops(False)
        self.deleteSupplyButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:rgb(255, 134, 97);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assetes/icons/delete-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteSupplyButton.setIcon(icon2)
        self.deleteSupplyButton.setIconSize(QSize(80, 80))
        self.deleteSupplyButton.setAutoDefault(False)
        self.deleteSupplyButton.setFlat(True)
        self.editSupplyButton = QPushButton(gestionDeProveedoresForm)
        self.editSupplyButton.setObjectName(u"editSupplyButton")
        self.editSupplyButton.setEnabled(True)
        self.editSupplyButton.setGeometry(QRect(290, 60, 91, 101))
        self.editSupplyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editSupplyButton.setAcceptDrops(False)
        self.editSupplyButton.setStyleSheet(u"QPushButton:hover\n"
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
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assetes/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editSupplyButton.setIcon(icon3)
        self.editSupplyButton.setIconSize(QSize(80, 80))
        self.editSupplyButton.setAutoDefault(False)
        self.editSupplyButton.setFlat(True)
        self.label = QLabel(gestionDeProveedoresForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 160, 141, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(gestionDeProveedoresForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 160, 141, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(gestionDeProveedoresForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 160, 161, 21))
        self.label_3.setFont(font)
        self.supplierTableWidget = QTableWidget(gestionDeProveedoresForm)
        self.supplierTableWidget.setObjectName(u"supplierTableWidget")
        self.supplierTableWidget.setGeometry(QRect(60, 340, 2161, 771))
        self.homeButton = QPushButton(gestionDeProveedoresForm)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setEnabled(True)
        self.homeButton.setGeometry(QRect(2110, 70, 91, 101))
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setAcceptDrops(False)
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
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"./assetes/icons/pagina-de-inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QSize(80, 80))
        self.homeButton.setAutoDefault(False)
        self.homeButton.setFlat(True)
        self.label_4 = QLabel(gestionDeProveedoresForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1850, 10, 71, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.userNameLabel = QLabel(gestionDeProveedoresForm)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setGeometry(QRect(1920, 10, 171, 16))
        self.userNameLabel.setFont(font1)
        self.userLevelLabel = QLabel(gestionDeProveedoresForm)
        self.userLevelLabel.setObjectName(u"userLevelLabel")
        self.userLevelLabel.setGeometry(QRect(1920, 30, 171, 16))
        self.userLevelLabel.setFont(font1)
        self.label_5 = QLabel(gestionDeProveedoresForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1840, 30, 81, 16))
        self.label_5.setFont(font1)
        self.searchButton = QPushButton(gestionDeProveedoresForm)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1370, 250, 151, 31))
        icon5 = QIcon()
        icon5.addFile(u"./assetes/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon5)
        self.searchLineEdit = QLineEdit(gestionDeProveedoresForm)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(480, 250, 861, 31))
        self.searchByComboBox = QComboBox(gestionDeProveedoresForm)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(180, 250, 261, 31))
        self.label_6 = QLabel(gestionDeProveedoresForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 250, 141, 21))
        self.label_6.setFont(font)
        self.label_7 = QLabel(gestionDeProveedoresForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(680, 160, 211, 21))
        self.label_7.setFont(font)
        self.updateButton = QPushButton(gestionDeProveedoresForm)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setEnabled(True)
        self.updateButton.setGeometry(QRect(740, 60, 91, 101))
        self.updateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateButton.setAcceptDrops(False)
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
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"./assetes/icons/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateButton.setIcon(icon6)
        self.updateButton.setIconSize(QSize(80, 80))
        self.updateButton.setAutoDefault(False)
        self.updateButton.setFlat(True)

        self.retranslateUi(gestionDeProveedoresForm)

        self.addSupplyButton.setDefault(False)
        self.deleteSupplyButton.setDefault(False)
        self.editSupplyButton.setDefault(False)
        self.homeButton.setDefault(False)
        self.updateButton.setDefault(False)


        QMetaObject.connectSlotsByName(gestionDeProveedoresForm)
    # setupUi

    def retranslateUi(self, gestionDeProveedoresForm):
        gestionDeProveedoresForm.setWindowTitle(QCoreApplication.translate("gestionDeProveedoresForm", u"Gestion de Proveedores", None))
        self.addSupplyButton.setText("")
        self.deleteSupplyButton.setText("")
        self.editSupplyButton.setText("")
        self.label.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"A\u00f1adir Proveedor", None))
        self.label_2.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Editar Proveedor", None))
        self.label_3.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Eliminar Proveedor", None))
        self.homeButton.setText("")
        self.label_4.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Usuario:", None))
        self.userNameLabel.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Seleccione un Usuario", None))
        self.userLevelLabel.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Seleccione un Usuario", None))
        self.label_5.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Permisos:", None))
        self.searchButton.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Buscar Por:", None))
        self.label_7.setText(QCoreApplication.translate("gestionDeProveedoresForm", u"Actualizar Base de Datos", None))
        self.updateButton.setText("")
    # retranslateUi

