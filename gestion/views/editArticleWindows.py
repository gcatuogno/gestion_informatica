# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editArticleWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditArticleForm(object):
    def setupUi(self, editArticleForm):
        if not editArticleForm.objectName():
            editArticleForm.setObjectName(u"editArticleForm")
        editArticleForm.resize(903, 1010)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        editArticleForm.setWindowIcon(icon)
        self.descriptionlineEdit = QLineEdit(editArticleForm)
        self.descriptionlineEdit.setObjectName(u"descriptionlineEdit")
        self.descriptionlineEdit.setGeometry(QRect(210, 140, 641, 41))
        self.label = QLabel(editArticleForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 140, 121, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.codelineEdit = QLineEdit(editArticleForm)
        self.codelineEdit.setObjectName(u"codelineEdit")
        self.codelineEdit.setGeometry(QRect(210, 200, 241, 31))
        self.label_2 = QLabel(editArticleForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 200, 81, 31))
        self.label_2.setFont(font)
        self.buyPriceSpinBox = QSpinBox(editArticleForm)
        self.buyPriceSpinBox.setObjectName(u"buyPriceSpinBox")
        self.buyPriceSpinBox.setGeometry(QRect(210, 410, 131, 31))
        self.buyPriceSpinBox.setMaximum(999999999)
        self.label_3 = QLabel(editArticleForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 410, 181, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(editArticleForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 320, 91, 31))
        self.label_4.setFont(font)
        self.qtySpinBox = QSpinBox(editArticleForm)
        self.qtySpinBox.setObjectName(u"qtySpinBox")
        self.qtySpinBox.setGeometry(QRect(210, 320, 131, 31))
        self.qtySpinBox.setMaximum(999999999)
        self.SellPriceSpinBox = QSpinBox(editArticleForm)
        self.SellPriceSpinBox.setObjectName(u"SellPriceSpinBox")
        self.SellPriceSpinBox.setGeometry(QRect(210, 460, 131, 31))
        self.SellPriceSpinBox.setMaximum(999999999)
        self.label_5 = QLabel(editArticleForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 460, 161, 31))
        self.label_5.setFont(font)
        self.locationlineEdit = QLineEdit(editArticleForm)
        self.locationlineEdit.setObjectName(u"locationlineEdit")
        self.locationlineEdit.setGeometry(QRect(210, 260, 241, 31))
        self.label_6 = QLabel(editArticleForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 240, 101, 31))
        self.label_6.setFont(font)
        self.label_7 = QLabel(editArticleForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 270, 101, 31))
        self.label_7.setFont(font)
        self.label_8 = QLabel(editArticleForm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 60, 281, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)
        self.searchSupplierLineEdit = QLineEdit(editArticleForm)
        self.searchSupplierLineEdit.setObjectName(u"searchSupplierLineEdit")
        self.searchSupplierLineEdit.setGeometry(QRect(370, 550, 241, 31))
        self.searchSupplierButton = QPushButton(editArticleForm)
        self.searchSupplierButton.setObjectName(u"searchSupplierButton")
        self.searchSupplierButton.setGeometry(QRect(620, 550, 71, 31))
        self.searchSupplierButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectSupplierButton = QPushButton(editArticleForm)
        self.selectSupplierButton.setObjectName(u"selectSupplierButton")
        self.selectSupplierButton.setGeometry(QRect(700, 550, 71, 31))
        self.selectSupplierButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_9 = QLabel(editArticleForm)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 500, 241, 31))
        self.label_9.setFont(font)
        self.saveButton = QPushButton(editArticleForm)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(550, 840, 81, 91))
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
        self.cancelButton = QPushButton(editArticleForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(670, 840, 81, 91))
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
        self.supplierTableWidget = QTableWidget(editArticleForm)
        self.supplierTableWidget.setObjectName(u"supplierTableWidget")
        self.supplierTableWidget.setGeometry(QRect(200, 600, 581, 211))
        self.proveedorlabel = QLabel(editArticleForm)
        self.proveedorlabel.setObjectName(u"proveedorlabel")
        self.proveedorlabel.setGeometry(QRect(200, 820, 651, 16))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        self.proveedorlabel.setFont(font2)
        self.searchSuppliercomboBox = QComboBox(editArticleForm)
        self.searchSuppliercomboBox.setObjectName(u"searchSuppliercomboBox")
        self.searchSuppliercomboBox.setGeometry(QRect(200, 550, 161, 31))
        self.qtyMinSpinBox = QSpinBox(editArticleForm)
        self.qtyMinSpinBox.setObjectName(u"qtyMinSpinBox")
        self.qtyMinSpinBox.setGeometry(QRect(210, 360, 131, 31))
        self.qtyMinSpinBox.setMaximum(999999999)
        self.label_10 = QLabel(editArticleForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 360, 171, 31))
        self.label_10.setFont(font)

        self.retranslateUi(editArticleForm)

        QMetaObject.connectSlotsByName(editArticleForm)
    # setupUi

    def retranslateUi(self, editArticleForm):
        editArticleForm.setWindowTitle(QCoreApplication.translate("editArticleForm", u"Editar Articulo", None))
        self.label.setText(QCoreApplication.translate("editArticleForm", u"Descripcion:", None))
        self.label_2.setText(QCoreApplication.translate("editArticleForm", u"Codigo:", None))
        self.label_3.setText(QCoreApplication.translate("editArticleForm", u"Precio de Compra:", None))
        self.label_4.setText(QCoreApplication.translate("editArticleForm", u"Cantidad:", None))
        self.label_5.setText(QCoreApplication.translate("editArticleForm", u"Precio de Venta:", None))
        self.label_6.setText(QCoreApplication.translate("editArticleForm", u"Ubicacion", None))
        self.label_7.setText(QCoreApplication.translate("editArticleForm", u"Almacen:", None))
        self.label_8.setText(QCoreApplication.translate("editArticleForm", u"Editar Articulo", None))
        self.searchSupplierButton.setText(QCoreApplication.translate("editArticleForm", u"Buscar", None))
        self.selectSupplierButton.setText(QCoreApplication.translate("editArticleForm", u"Select.", None))
        self.label_9.setText(QCoreApplication.translate("editArticleForm", u"Seleccione el Proveedor:", None))
        self.saveButton.setText("")
        self.cancelButton.setText("")
        self.proveedorlabel.setText(QCoreApplication.translate("editArticleForm", u"Seleccione un Proveedor", None))
        self.label_10.setText(QCoreApplication.translate("editArticleForm", u"Cantidad Minima:", None))
    # retranslateUi

