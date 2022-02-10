# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectSupplierWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class SelectSupplyForm(object):
    def setupUi(self, SelectSupplyForm):
        if not SelectSupplyForm.objectName():
            SelectSupplyForm.setObjectName(u"SelectSupplyForm")
        SelectSupplyForm.resize(1518, 367)
        self.supplierTableWidget = QTableWidget(SelectSupplyForm)
        self.supplierTableWidget.setObjectName(u"supplierTableWidget")
        self.supplierTableWidget.setGeometry(QRect(20, 110, 1461, 192))
        self.searchByComboBox = QComboBox(SelectSupplyForm)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(130, 70, 261, 31))
        self.searchButton = QPushButton(SelectSupplyForm)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(1320, 70, 151, 31))
        icon = QIcon()
        icon.addFile(u"./assetes/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.label_6 = QLabel(SelectSupplyForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 70, 141, 21))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.searchLineEdit = QLineEdit(SelectSupplyForm)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(430, 70, 861, 31))
        self.confirmButton = QPushButton(SelectSupplyForm)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(1352, 310, 121, 31))
        self.confirmButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(SelectSupplyForm)

        QMetaObject.connectSlotsByName(SelectSupplyForm)
    # setupUi

    def retranslateUi(self, SelectSupplyForm):
        SelectSupplyForm.setWindowTitle(QCoreApplication.translate("SelectSupplyForm", u"Seleccion de Proveedor", None))
        self.searchButton.setText(QCoreApplication.translate("SelectSupplyForm", u"Buscar", None))
        self.label_6.setText(QCoreApplication.translate("SelectSupplyForm", u"Buscar Por:", None))
        self.confirmButton.setText(QCoreApplication.translate("SelectSupplyForm", u"Confirmar", None))
    # retranslateUi

