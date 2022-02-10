from PySide2.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem
from PySide2.QtCore import Qt
from database.supply import selectAllSupplier
from views.newArticleWindows import NewArticleForm
from database.products import addProduct
from database.supply import selectAllSupplier
from database.models import Supply_db
from database import db 

class NewArticleWindows(QWidget, NewArticleForm):

    def __init__(self, parent=None):
        # Heredamos de la clase padre.
        super().__init__(parent)

        # Configuramos la vetana
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Cargamos los datos
        self.table_config()
        self.populateTable(selectAllSupplier())
        self.populateComboBox()

        # Asignamos Funciones a los botones
        self.saveButton.clicked.connect(self.addArticle)
        self.cancelButton.clicked.connect(self.selectSupplier)
        self.selectSupplierButton.clicked.connect(self.selectSupplier)
        self.searchSupplierButton.clicked.connect(self.searchSupplier)

    # Configuracion de la tabla.
    def table_config(self):
        #Establecemos los encabezados
        column_headers =("ID", "Razon Social", "CIF", "Direccion", "Telefono")
        self.supplierTableWidget.setColumnCount(len(column_headers))  
        self.supplierTableWidget.setHorizontalHeaderLabels(column_headers)
        # Funcion quer permite seleccionar toda una fila con un click 
        self.supplierTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Funcion para Cargar los datos en la tabla
    def populateTable(self, data):
        # Verificamos la candidad de lineas
        self.supplierTableWidget.setRowCount(len(data))

        # Llenamos la tabla con un bucle for
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.supplierTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 

    #Funcion para verificar los Inputs
    def checkInput(self):

        #Obtenemos los valores escritos por el usuario.
        description = self.descriptionLineEdit.text()
        code = self.codeLineEdit.text()
        location = self.locationLineEdit.text()
        qty = self.qtySpinBox.value()
        minQty = self.qtyMinSpinBox.value()
        buyPrice = self.buyPriceSpinBox.value()
        sellPrice = self.sellPriceSpinBox.value()
        supply = self.proveedorlabel.text()
        
        errosCount = 0

        # Verificamos que todos los campos sean validos
        if description == "":
            print("El campo Descripcion es obligatorio")
            errosCount += 1

        if code == "":
            print("El campo Codigo es obligatorio")
            errosCount += 1

        if location == "":
            print("El campo Ubicacion es obligatorio")
            errosCount += 1

        if qty == "":
            print("El campo Cantidad es obligatorio")
            errosCount += 1

        if minQty == "":
            print("El campo Cantidad Minima es obligatorio")
            errosCount += 1

        if buyPrice == "":
            print("El campo Precio de Compra es obligatorio")
            errosCount += 1
        
        if sellPrice == "":
            print("El campo Precio de Venta es obligatorio")
            errosCount += 1

        if supply == "":
            print("El campo Proveedor es obligatorio")
            errosCount += 1
        
        if errosCount == 0:
            return True

    # Funcion para borrar los input
    def cleanInput(self):

        self.descriptionLineEdit.clear()
        self.codeLineEdit.clear()
        self.locationLineEdit.clear()
        self.qtySpinBox.setValue(0)
        self.qtyMinSpinBox.setValue(0)
        self.buyPriceSpinBox.setValue(0)
        self.sellPriceSpinBox.setValue(0)
        self.proveedorlabel.setText("Seleccione un Proveedor")

    # Funcion que carga datos en el combobox
    def populateComboBox(self):
        cb_option = ("Razon Social", "CIF")
        self.searchSuppliercomboBox.addItems(cb_option)

    # Seleccionar un proovedor.
    def selectSupplier(self):
        supplier = self.supplierTableWidget.selectedItems()
        name_supplier = str(supplier[1].text())
        self.proveedorlabel.setText(name_supplier)
        return name_supplier

    # Buscar Proveedor.
    def searchSupplier(self):
        option_select = self.searchSuppliercomboBox.currentText()
        parameter = self.searchSupplierLineEdit.text()

        if option_select == "Razon Social":
            listSupplier = self.selectSupplierByName(parameter)
            self.populateTable(listSupplier)

        if option_select == "CIF":
            listSupplier = self.selectSupplierByCif(parameter)
            self.populateTable(listSupplier)

    # Buscar Proovedor Por Razon Social.
    def selectSupplierByName(self, name):

        name = "%{}%".format(name)
        supplier = db.session.query(Supply_db).filter(Supply_db.name.like(name)).all()
        listsupplier = []

        for i in supplier:
            supply = [i.id, i.name, i.cif, i.adress, i.phone]
            listsupplier.append(supply)

        return listsupplier

    # Buscas Proovedor por CIF.
    def selectSupplierByCif(self, cif):

        cif = "%{}%".format(cif)
        supplier = db.session.query(Supply_db).filter(Supply_db.cif.like(cif)).all()
        listsupplier = []

        for i in supplier:
            supply = [i.id, i.name, i.cif, i.adress, i.phone]
            listsupplier.append(supply)

        return listsupplier

    # Funcion para añadir Articulos
    def addArticle(self):

        #Obtenemos los valores escritos por el usuario.
        description = self.descriptionLineEdit.text()
        code = self.codeLineEdit.text()
        location = self.locationLineEdit.text()
        qty = self.qtySpinBox.value()
        minQty = self.qtyMinSpinBox.value()
        buyPrice = self.buyPriceSpinBox.value()
        sellPrice = self.sellPriceSpinBox.value()
        supply = self.proveedorlabel.text()

        if self.checkInput():
            data = (description, code, location, qty, minQty, buyPrice, sellPrice, supply)

            if addProduct(data):
                self.cleanInput()
                self.close()
    

