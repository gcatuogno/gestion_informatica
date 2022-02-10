from PySide2.QtWidgets import QWidget, QFileDialog, QAbstractItemView, QTableWidgetItem
from PySide2.QtCore import Qt
from database.users import deleteUser, selectAllUser, selectUserByName
from views.userPanelWindows import UserPanelFrom
from controllers.newUserWindows import NewUserWindows


class UserPanelWindows(QWidget, UserPanelFrom):

# Constructor.
    def __init__(self, parent=None):
        # Metodo init clase padre.
        super().__init__(parent)

        # Funcion que crea la ventana.
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Configuramos la ventana
        self.table_config()
        self.populateTable(selectAllUser())

        # Configuramos los botones.
        self.addUserButton.clicked.connect(self.addUSerWindows)
        self.deleteUserButton.clicked.connect(self.deleteUser)
        self.updateButton.clicked.connect(lambda: self.populateTable(selectAllUser()))
        self.homeButton.clicked.connect(self.close)
        
    # Funcion que configura la tabla.
    def table_config(self):
        # Establecemos los encabezados.
        column_headers = ("ID", "Usuario", "Clave", "Nivel de Acceso")
        self.userTableWidget.setColumnCount(len(column_headers))  
        self.userTableWidget.setHorizontalHeaderLabels(column_headers)
        # Funcion quer permite seleccionar toda una fila con un click 
        self.userTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Funcion que vuelve al menu main.
    def main(self):
        self.close()

    # Metodo que carga los datos en la tabla.
    def populateTable(self, data):
        # Verificamos la candidad de lineas
        self.userTableWidget.setRowCount(len(data))

        # Llenamos la tabla con un bucle for
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.userTableWidget.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) 

    # Metodo que muestra la ventada nuevo producto.
    def addUSerWindows(self):
        windows = NewUserWindows(self)
        windows.show()

    # Metodo que realiza la busqueda.
    def searchUser(self):
        # Seleccionamos nuestro parametro de busqueda
        parameter = self.searchLineEdit.text()

        #Realizamos las verificaciones y la busqueda.
        if parameter == "":
            print("Debes escribir un parametro")
        else:
            selectUserByName(parameter)

    # Metodo para borrar un usuario.
    def deleteUser(self):
        select_row = self.userTableWidget.selectedItems()

        if select_row:
            userId = int(select_row[0].text())
            deleteUser(userId)
            self.populateTable(selectAllUser())
            
    
