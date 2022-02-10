from PySide2.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem
from PySide2.QtCore import Qt
from views.gestionWindows import GestionDeProductosForm
from controllers.newArticleWindows import NewArticleWindows
from controllers.editArticleWindows import EditArticleWindows
from database.products import deleteProduct, selectAllProduct, deleteProduct, selectProductBySupplier, selectProductByCode, selectProductByDescription, selectProductBylocation, checkMin, minRequest
from database import db
from database.models import User_db
from database.exportPdf import exportRequest

class GestionDeProductosWindows(QWidget, GestionDeProductosForm):

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


        # Configraciones Iniciales.
        self.table_config()
        self.populateTable(selectAllProduct())
        self.populateComboBox()
        self.populateLabelUser(user)
        self.minAlert()

        # Configuramos los botones.
        self.addArticleButton.clicked.connect(self.addProductWindows)
        self.updateButton.clicked.connect(self.update)
        self.editArticleButton.clicked.connect(self.editProduct)
        self.deleteArticleButton.clicked.connect(self.deleteProduct)
        self.searchButton.clicked.connect(self.searchProduct)
        self.homeButton.clicked.connect(self.main)
        self.minStockButton.clicked.connect(self.minStock)

    # Funcion que configura la tabla.
    def table_config(self):
        # Establecemos los encabezados.
        column_headers = ("ID", "Descripcion", "Codigo", "Ubicacion en almacen", "Cantidad Disponible", "Cantidad Minima", "Precio de Compra", "Precio de Venta","Proveedor")
        self.articleTableWidget.setColumnCount(len(column_headers))  
        self.articleTableWidget.setHorizontalHeaderLabels(column_headers)
        # Funcion quer permite seleccionar toda una fila con un click 
        self.articleTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Metodo que muestra la ventada nuevo producto.
    def addProductWindows(self):
        windows = NewArticleWindows(self)
        windows.show()
       
    # Metodo que muestra la ventana editar producto.
    def editProduct(self):
        selected_row = self.articleTableWidget.selectedItems()
        if selected_row:
            prodcutID = int(selected_row[0].text())
            windows = EditArticleWindows(self, prodcutID)
            windows.show()
        self.articleTableWidget.clearSelection()

    # Metodo para borrar un producto.
    def deleteProduct(self):
        select_row = self.articleTableWidget.selectedItems()

        if select_row:
            productId = int(select_row[0].text())
            deleteProduct(productId)
            self.populateTable(selectAllProduct())
        
    # Metodo que realiza la busqueda.
    def searchProduct(self):
        # Seleccionamos nuestros filtros de busqueda
        option_selectec = self.searchByComboBox.currentText()
        parameter = self.searchLineEdit.text()

        #Realizamos las verificaciones y la busqueda.
        if parameter == "":
            print("Debes Seleccionar una opcion")
        else:
            if option_selectec == "Descipcion":
                self.searchProductByDescription(parameter)

            if option_selectec == "Codigo":
                self.searchProductByCode(parameter)

            if option_selectec == "Proveedor":
                self.searchProductBySupplier(parameter)

            if option_selectec == "Ubicacion en almacen":
                self.searchProductByLocation(parameter)
            
    # Busca un producto por su Descripcion.
    def searchProductByDescription(self, description):
        data = selectProductByDescription(description)
        self.populateTable(data)

    # Busca un producto por su codigo.
    def searchProductByCode(self, code):
        data = selectProductByCode(code)
        self.populateTable(data)

    # Busca un producto por su proveedor.
    def searchProductBySupplier(self, supplier):
        data = selectProductBySupplier(supplier)
        self.populateTable(data)

    # Busca un producto por su ubicacion.
    def searchProductByLocation(self, location):
        data = selectProductBylocation(location)
        self.populateTable(data)
        
    # Metodo que carga los datos en la tabla.
    def populateTable(self, data):
        # Verificamos la candidad de lineas
        self.articleTableWidget.setRowCount(len(data))

        # Llenamos la tabla con un bucle for
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.articleTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 

    # Metodo que llena las opciones del combobox.
    def populateComboBox(self):
        cb_option = ("Descipcion", "Codigo", "Proveedor", "Ubicacion en almacen")
        self.searchByComboBox.addItems(cb_option)

    # Funcion que vuelve al menu main.
    def main(self):
        self.close()

    # Identificaicion de usuario. 
    def user(self, userId):
        user = db.session.query(User_db).filter_by(id = userId).first()
        return user

    # Funcion que informa al usuario de stock minimo
    def minAlert(self):

        data = selectAllProduct()
        if checkMin(data) == False:
            self.notificationLabel.setText("Tienes Productos con Bajo Stock")
        else:
            self.notificationLabel.setText("")

    # Funcion Boton Update
    def update(self):
        self.populateTable(selectAllProduct())
        self.minAlert()

    # Informacion del usuario.
    def populateLabelUser(self, user):
        self.userNameLabel.setText(user.userName)
        self.userLevelLabel.setText(user.userLevel)

    # Solicitar productos bajo stock.
    def minStock(self):
        data = selectAllProduct()
        lowStock = minRequest(data)
        exportRequest(lowStock)
        print("Pedido Solicitado")