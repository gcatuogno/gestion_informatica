from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from database.users import addUser
from views.newUserWindows import NewUserForm

class NewUserWindows(QWidget, NewUserForm):

    # Constructor.
    def __init__(self, parent=None):
        # Metodo init clase padre.
        super().__init__(parent)

        # Funcion que crea la ventana.
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Cargamos los datos.
        self.populateComboBox()

        # Funcion de los botones.
        self.addUserButton.clicked.connect(self.newUser)
        self.cancelButton.clicked.connect(self.close)
        
    #Funcion para verificar los Inputs
    def checkInput(self):

        #Obtenemos los valores escritos por el usuario.
        name = self.userNameLineEdit.text()
        password = self.userPaswordLineEdit.text()
        
        errosCount = 0

        # Verificamos que todos los campos sean validos
        if name == "":
            print("El campo Nombre es obligatorio")
            errosCount += 1

        if password == "":
            print("El campo Clave es obligatorio")
            errosCount += 1

        return True

    # Funcion para borrar los input
    def cleanInput(self):

        self.userNameLineEdit.clear()
        self.userPaswordLineEdit.clear()

    # Funcion para añadir Usuarios
    def newUser(self):
        print("Estoy en la funcion")
        #Obtenemos los valores escritos por el usuario.
        name = self.userNameLineEdit.text()
        password = self.userPaswordLineEdit.text()
        level = self.levelComboBox.currentText()
 
        if self.checkInput():
            data = (name, password, level)

            if addUser(data):
                self.cleanInput()
                self.close()
    
    # Funcion que carga datos en el combobox
    def populateComboBox(self):
        cb_option = ("","Acceso a Productos", "Acceso a Proveedores", "Acceso a Productos + Proveedores", "Administrador")
        self.levelComboBox.addItems(cb_option)