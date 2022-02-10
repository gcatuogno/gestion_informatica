# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestionWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class GestionDeProductosForm(object):
    def setupUi(self, gestionDeProductosForm):
        if not gestionDeProductosForm.objectName():
            gestionDeProductosForm.setObjectName(u"gestionDeProductosForm")
        gestionDeProductosForm.resize(2269, 1135)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/gestion-de-datos.png", QSize(), QIcon.Normal, QIcon.Off)
        gestionDeProductosForm.setWindowIcon(icon)
        self.addArticleButton = QPushButton(gestionDeProductosForm)
        self.addArticleButton.setObjectName(u"addArticleButton")
        self.addArticleButton.setEnabled(True)
        self.addArticleButton.setGeometry(QRect(90, 60, 91, 101))
        self.addArticleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addArticleButton.setAcceptDrops(False)
        self.addArticleButton.setStyleSheet(u"QPushButton:hover\n"
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
        self.addArticleButton.setIcon(icon1)
        self.addArticleButton.setIconSize(QSize(80, 80))
        self.addArticleButton.setAutoDefault(False)
        self.addArticleButton.setFlat(True)
        self.deleteArticleButton = QPushButton(gestionDeProductosForm)
        self.deleteArticleButton.setObjectName(u"deleteArticleButton")
        self.deleteArticleButton.setEnabled(True)
        self.deleteArticleButton.setGeometry(QRect(480, 60, 91, 101))
        self.deleteArticleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteArticleButton.setAcceptDrops(False)
        self.deleteArticleButton.setStyleSheet(u"QPushButton:hover\n"
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
        self.deleteArticleButton.setIcon(icon2)
        self.deleteArticleButton.setIconSize(QSize(80, 80))
        self.deleteArticleButton.setAutoDefault(False)
        self.deleteArticleButton.setFlat(True)
        self.editArticleButton = QPushButton(gestionDeProductosForm)
        self.editArticleButton.setObjectName(u"editArticleButton")
        self.editArticleButton.setEnabled(True)
        self.editArticleButton.setGeometry(QRect(290, 60, 91, 101))
        self.editArticleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editArticleButton.setAcceptDrops(False)
        self.editArticleButton.setStyleSheet(u"QPushButton:hover\n"
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
        self.editArticleButton.setIcon(icon3)
        self.editArticleButton.setIconSize(QSize(80, 80))
        self.editArticleButton.setAutoDefault(False)
        self.editArticleButton.setFlat(True)
        self.label = QLabel(gestionDeProductosForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 160, 121, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(gestionDeProductosForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 160, 121, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(gestionDeProductosForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 160, 131, 21))
        self.label_3.setFont(font)
        self.articleTableWidget = QTableWidget(gestionDeProductosForm)
        self.articleTableWidget.setObjectName(u"articleTableWidget")
        self.articleTableWidget.setGeometry(QRect(60, 290, 2161, 791))
        self.homeButton = QPushButton(gestionDeProductosForm)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setEnabled(True)
        self.homeButton.setGeometry(QRect(2130, 70, 91, 101))
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
        self.userLevelLabel = QLabel(gestionDeProductosForm)
        self.userLevelLabel.setObjectName(u"userLevelLabel")
        self.userLevelLabel.setGeometry(QRect(1940, 30, 171, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.userLevelLabel.setFont(font1)
        self.userNameLabel = QLabel(gestionDeProductosForm)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setGeometry(QRect(1940, 10, 171, 16))
        self.userNameLabel.setFont(font1)
        self.label_4 = QLabel(gestionDeProductosForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1870, 10, 71, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(gestionDeProductosForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1860, 30, 81, 16))
        self.label_5.setFont(font1)
        self.searchLineEdit = QLineEdit(gestionDeProductosForm)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(530, 220, 861, 31))
        self.searchButton = QPushButton(gestionDeProductosForm)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1420, 220, 151, 31))
        icon5 = QIcon()
        icon5.addFile(u"./assetes/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon5)
        self.searchByComboBox = QComboBox(gestionDeProductosForm)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(230, 220, 261, 31))
        self.label_6 = QLabel(gestionDeProductosForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 225, 141, 21))
        self.label_6.setFont(font)
        self.label_7 = QLabel(gestionDeProductosForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(620, 160, 211, 21))
        self.label_7.setFont(font)
        self.updateButton = QPushButton(gestionDeProductosForm)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setEnabled(True)
        self.updateButton.setGeometry(QRect(680, 60, 91, 101))
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
        self.notificationLabel = QLabel(gestionDeProductosForm)
        self.notificationLabel.setObjectName(u"notificationLabel")
        self.notificationLabel.setGeometry(QRect(370, 20, 1421, 21))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.notificationLabel.setFont(font2)
        self.minStockButton = QPushButton(gestionDeProductosForm)
        self.minStockButton.setObjectName(u"minStockButton")
        self.minStockButton.setEnabled(True)
        self.minStockButton.setGeometry(QRect(880, 60, 91, 101))
        self.minStockButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minStockButton.setAcceptDrops(False)
        self.minStockButton.setStyleSheet(u"QPushButton:hover\n"
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
        icon7 = QIcon()
        icon7.addFile(u"./assetes/icons/portapapeles.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minStockButton.setIcon(icon7)
        self.minStockButton.setIconSize(QSize(80, 80))
        self.minStockButton.setAutoDefault(False)
        self.minStockButton.setFlat(True)
        self.label_8 = QLabel(gestionDeProductosForm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(860, 160, 141, 21))
        self.label_8.setFont(font)

        self.retranslateUi(gestionDeProductosForm)

        self.addArticleButton.setDefault(False)
        self.deleteArticleButton.setDefault(False)
        self.editArticleButton.setDefault(False)
        self.homeButton.setDefault(False)
        self.updateButton.setDefault(False)
        self.minStockButton.setDefault(False)


        QMetaObject.connectSlotsByName(gestionDeProductosForm)
    # setupUi

    def retranslateUi(self, gestionDeProductosForm):
        gestionDeProductosForm.setWindowTitle(QCoreApplication.translate("gestionDeProductosForm", u"Gestion de Productos", None))
        self.addArticleButton.setText("")
        self.deleteArticleButton.setText("")
        self.editArticleButton.setText("")
        self.label.setText(QCoreApplication.translate("gestionDeProductosForm", u"A\u00f1adir Articulo", None))
        self.label_2.setText(QCoreApplication.translate("gestionDeProductosForm", u"Editar Articulo", None))
        self.label_3.setText(QCoreApplication.translate("gestionDeProductosForm", u"Eliminar Articulo", None))
        self.homeButton.setText("")
        self.userLevelLabel.setText(QCoreApplication.translate("gestionDeProductosForm", u"Seleccione un Usuario", None))
        self.userNameLabel.setText(QCoreApplication.translate("gestionDeProductosForm", u"Seleccione un Usuario", None))
        self.label_4.setText(QCoreApplication.translate("gestionDeProductosForm", u"Usuario:", None))
        self.label_5.setText(QCoreApplication.translate("gestionDeProductosForm", u"Permisos:", None))
        self.searchButton.setText(QCoreApplication.translate("gestionDeProductosForm", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("gestionDeProductosForm", u"Buscar Por:", None))
        self.label_7.setText(QCoreApplication.translate("gestionDeProductosForm", u"Actualizar Base de Datos", None))
        self.updateButton.setText("")
        self.notificationLabel.setText("")
        self.minStockButton.setText("")
        self.label_8.setText(QCoreApplication.translate("gestionDeProductosForm", u"Realizar Pedidos", None))
    # retranslateUi

