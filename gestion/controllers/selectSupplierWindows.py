from PySide2.QtWidgets import QWidget, QFileDialog, QAbstractItemView, QTableWidgetItem
from PySide2.QtCore import Qt
from database.supply import selectAllSupplier
from views.selectSupplierWindows import SelectSupplyForm


class SelectSupplyWindows(QWidget, SelectSupplyForm):

    def __init__(self, parent=None):

        # Heredamos de la clase padre.
        super().__init__(parent)

        # Configramos la ventana
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Configramos la tabla
        self.table_config()
        self.populateTable(selectAllSupplier())

        # Asignamos Funciones a los botones
        self.confirmButton.clicked.connect(self.confirmSupplier)
        
    # Fun que configura la tabla.
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

    # Funcion que envia la informacion del proveedor seleccionado.
    def supplier(self):
        # Tomamos la celda seleccionada.
        selectRow = self.supplierTableWidget.selectedItems()
        supplier = selectRow[1]
        return supplier

    # Accion Boton confirmar.
    def confirmSupplier(self):

        if self.supplierTableWidget.selectedItems():
            supplier = self.supplier()
            #newArticleWindows.NewArticleWindows.selectSupplier(self, supplier)
            self.close()
            return supplier
            
            
