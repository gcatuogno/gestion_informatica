from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from database.supply import deleteSupplier, selectAllSupplier, selectSupplierByCif, selectSupplierByName
from PySide2.QtCore import Qt
from views.gestionProveedoresWindows import GestionDeProveedoresForm
from controllers.newSupplyWindows import NewSupplyWindows
from controllers.editSupplyWindows import EditSupplyWindows
from database import db
from database.models import User_db



class GestionDeProveedoresWindows(QWidget, GestionDeProveedoresForm):

    # Constructor.
    def __init__(self, parent=None, userId = None):
         # Metodo init clase padre.
        super().__init__(parent)

        # Funcion que crea la ventana.
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Identificacion de usuario.
        self.userId = userId
        user = self.user(userId)

        # Iniciamos Funciones.
        self.table_config()
        self.populateTable(selectAllSupplier())
        self.populateComboBox()
        self.populateLabelUser(user)

        # Configuramos los botones.
        self.addSupplyButton.clicked.connect(self.addSupplierWindows)
        self.editSupplyButton.clicked.connect(self.editSupplierWindows)
        self.deleteSupplyButton.clicked.connect(self.deleteSupplier)
        self.searchButton.clicked.connect(self.searchSupplier)
        self.updateButton.clicked.connect(lambda: self.populateTable(selectAllSupplier()))
        self.homeButton.clicked.connect(self.main)
    

    # Configuracion de la tabla.
    def table_config(self):
        #Establecemos los encabezados
        column_headers =("ID", "Razon Social", "CIF", "Direccion", "Telefono")
        self.supplierTableWidget.setColumnCount(len(column_headers))  
        self.supplierTableWidget.setHorizontalHeaderLabels(column_headers)
        # Funcion quer permite seleccionar toda una fila con un click 
        self.supplierTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)   

    # Metodo para abrir la ventana añadir un proveedor.
    def addSupplierWindows(self):
        windows = NewSupplyWindows(self)
        windows.show()
        
    # Metodo que abre la ventana editar proveedor.
    def editSupplierWindows(self):
        selected_row = self.supplierTableWidget.selectedItems()
        if selected_row:
            supplierId = int(selected_row[0].text())
            windows = EditSupplyWindows(self, supplierId)
            windows.show()
        self.supplierTableWidget.clearSelection()

    # Metodo para eliminar un proveedor.
    def deleteSupplier(self):
        select_row = self.supplierTableWidget.selectedItems()

        if select_row:
            supplierId = int(select_row[0].text())
            deleteSupplier(supplierId)
            self.populateTable(selectAllSupplier())

    # Metodo para buscar proveedores.
    def searchSupplier(self):
        # Seleccionamos nuestros filtros de busqueda
        option_selectec = self.searchByComboBox.currentText()
        parameter = self.searchLineEdit.text()

        #Realizamos las verificaciones y la busqueda.
        if parameter == "":
            print("Debes Seleccionar una opcion")
        else:
            if option_selectec == "Razon Social":
                self.searchSuppliertByName(parameter)

            if option_selectec == "CIF":
                self.searchSuppliertByCifs(parameter)

    # Buscar Proveedor por Razon Social.
    def searchSuppliertByName(self, name):
        data = selectSupplierByName(name)
        self.populateTable(data)
        
    # Buscar Proveedor por Cif.
    def searchSuppliertByCif(self, cif):
        data = selectSupplierByCif(cif)
        self.populateTable(data)
        
    # Funcion para Cargar los datos en la tabla.
    def populateTable(self, data):
        # Verificamos la candidad de lineas
        self.supplierTableWidget.setRowCount(len(data))

        # Llenamos la tabla con un bucle for
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.supplierTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    # Funcion para cargar datos en el comboBox.
    def populateComboBox(self):

        cbData = "Razon Social", "CIF"
        self.searchByComboBox.addItems(cbData)

    # Funcion que vuelve al menu main.
    def main(self):
        self.close()

    # Identificaicion de usuario. 
    def user(self, userId):
        user = db.session.query(User_db).filter_by(id = userId).first()
        return user

    # Informacion del usuario.
    def populateLabelUser(self, user):
        self.userNameLabel.setText(user.userName)
        self.userLevelLabel.setText(user.userLevel)