# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newArticleWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewArticleForm(object):
    def setupUi(self, newArticleForm):
        if not newArticleForm.objectName():
            newArticleForm.setObjectName(u"newArticleForm")
        newArticleForm.resize(903, 1019)
        icon = QIcon()
        icon.addFile(u"./assetes/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        newArticleForm.setWindowIcon(icon)
        self.descriptionLineEdit = QLineEdit(newArticleForm)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")
        self.descriptionLineEdit.setGeometry(QRect(210, 140, 641, 41))
        self.label = QLabel(newArticleForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 140, 121, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.codeLineEdit = QLineEdit(newArticleForm)
        self.codeLineEdit.setObjectName(u"codeLineEdit")
        self.codeLineEdit.setGeometry(QRect(210, 200, 241, 31))
        self.label_2 = QLabel(newArticleForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 200, 81, 31))
        self.label_2.setFont(font)
        self.buyPriceSpinBox = QSpinBox(newArticleForm)
        self.buyPriceSpinBox.setObjectName(u"buyPriceSpinBox")
        self.buyPriceSpinBox.setGeometry(QRect(210, 410, 131, 31))
        self.buyPriceSpinBox.setMaximum(999999999)
        self.label_3 = QLabel(newArticleForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 410, 181, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(newArticleForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 310, 91, 31))
        self.label_4.setFont(font)
        self.qtySpinBox = QSpinBox(newArticleForm)
        self.qtySpinBox.setObjectName(u"qtySpinBox")
        self.qtySpinBox.setGeometry(QRect(210, 310, 131, 31))
        self.qtySpinBox.setMaximum(999999999)
        self.sellPriceSpinBox = QSpinBox(newArticleForm)
        self.sellPriceSpinBox.setObjectName(u"sellPriceSpinBox")
        self.sellPriceSpinBox.setGeometry(QRect(210, 460, 131, 31))
        self.sellPriceSpinBox.setMaximum(999999999)
        self.label_5 = QLabel(newArticleForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 460, 161, 31))
        self.label_5.setFont(font)
        self.searchSupplierButton = QPushButton(newArticleForm)
        self.searchSupplierButton.setObjectName(u"searchSupplierButton")
        self.searchSupplierButton.setGeometry(QRect(630, 560, 71, 31))
        self.searchSupplierButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proveedorlabel = QLabel(newArticleForm)
        self.proveedorlabel.setObjectName(u"proveedorlabel")
        self.proveedorlabel.setGeometry(QRect(210, 830, 651, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.proveedorlabel.setFont(font1)
        self.locationLineEdit = QLineEdit(newArticleForm)
        self.locationLineEdit.setObjectName(u"locationLineEdit")
        self.locationLineEdit.setGeometry(QRect(210, 260, 241, 31))
        self.label_6 = QLabel(newArticleForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 240, 101, 31))
        self.label_6.setFont(font)
        self.label_7 = QLabel(newArticleForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 270, 101, 31))
        self.label_7.setFont(font)
        self.label_8 = QLabel(newArticleForm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 60, 281, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.saveButton = QPushButton(newArticleForm)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(560, 850, 81, 91))
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
        self.cancelButton = QPushButton(newArticleForm)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(680, 850, 81, 91))
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
        self.supplierTableWidget = QTableWidget(newArticleForm)
        self.supplierTableWidget.setObjectName(u"supplierTableWidget")
        self.supplierTableWidget.setGeometry(QRect(210, 610, 581, 211))
        self.searchSuppliercomboBox = QComboBox(newArticleForm)
        self.searchSuppliercomboBox.setObjectName(u"searchSuppliercomboBox")
        self.searchSuppliercomboBox.setGeometry(QRect(210, 560, 161, 31))
        self.searchSupplierLineEdit = QLineEdit(newArticleForm)
        self.searchSupplierLineEdit.setObjectName(u"searchSupplierLineEdit")
        self.searchSupplierLineEdit.setGeometry(QRect(380, 560, 241, 31))
        self.label_9 = QLabel(newArticleForm)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 510, 241, 31))
        self.label_9.setFont(font)
        self.selectSupplierButton = QPushButton(newArticleForm)
        self.selectSupplierButton.setObjectName(u"selectSupplierButton")
        self.selectSupplierButton.setGeometry(QRect(710, 560, 71, 31))
        self.selectSupplierButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.qtyMinSpinBox = QSpinBox(newArticleForm)
        self.qtyMinSpinBox.setObjectName(u"qtyMinSpinBox")
        self.qtyMinSpinBox.setGeometry(QRect(210, 360, 131, 31))
        self.qtyMinSpinBox.setMaximum(999999999)
        self.label_10 = QLabel(newArticleForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 360, 171, 31))
        self.label_10.setFont(font)

        self.retranslateUi(newArticleForm)

        QMetaObject.connectSlotsByName(newArticleForm)
    # setupUi

    def retranslateUi(self, newArticleForm):
        newArticleForm.setWindowTitle(QCoreApplication.translate("newArticleForm", u"Nuevo Articulo", None))
        self.label.setText(QCoreApplication.translate("newArticleForm", u"Descripcion:", None))
        self.label_2.setText(QCoreApplication.translate("newArticleForm", u"Codigo:", None))
        self.label_3.setText(QCoreApplication.translate("newArticleForm", u"Precio de Compra:", None))
        self.label_4.setText(QCoreApplication.translate("newArticleForm", u"Cantidad:", None))
        self.label_5.setText(QCoreApplication.translate("newArticleForm", u"Precio de Venta:", None))
        self.searchSupplierButton.setText(QCoreApplication.translate("newArticleForm", u"Buscar", None))
        self.proveedorlabel.setText(QCoreApplication.translate("newArticleForm", u"Seleccione un Proveedor", None))
        self.label_6.setText(QCoreApplication.translate("newArticleForm", u"Ubicacion", None))
        self.label_7.setText(QCoreApplication.translate("newArticleForm", u"Almacen:", None))
        self.label_8.setText(QCoreApplication.translate("newArticleForm", u"Nuevo Articulo", None))
        self.saveButton.setText("")
        self.cancelButton.setText("")
        self.label_9.setText(QCoreApplication.translate("newArticleForm", u"Seleccione el Proveedor:", None))
        self.selectSupplierButton.setText(QCoreApplication.translate("newArticleForm", u"Select.", None))
        self.label_10.setText(QCoreApplication.translate("newArticleForm", u"Cantidad Minima:", None))
    # retranslateUi

