from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.loginWindows import LoginForm
from database import db
from database.models import User_db
from controllers.mainMenuWindows import MainMenuWindows

class LoginWindows(QWidget, LoginForm):

# Constructor.
    def __init__(self, parent=None):
        # Metodo init clase padre.
        super().__init__(parent)

        # Funcion que crea la ventana.
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Cargamos datos.
        self.populateComboBox()

        # Añadimos funcion a los botones.
        self.loginButton.clicked.connect(self.login)

    # Funcion que carga los datos al comboBox.
    def populateComboBox(self):
        cbData = ("Seleccione Nivel de Usuario", "Acceso a Productos", "Acceso a Proveedores", "Acceso a Productos + Proveedores", "Administrador")
        self.selectTypeUserComboBox.addItems(cbData)

    #Funcion que realiza las validaciones en el Login
    def login(self):
        
        if self.userLineEdit.text() == "":
            self.mensageLogin.setText("Introduce todos los datos")
            
        if self.paswordLineEdit.text() == "":
            self.mensageLogin.setText("Introduce todos los datos")
        else:
            userId = self.checkUser()
            self.mensageLogin.setText("")
        if userId == False:
            self.mensageLogin.setText("No se pudo hacer el Login")

        else:
            self.mainMenu(userId)
            self.mensageLogin.setText("")

    # Funcion que veririca el usuario.
    def checkUser(self):

        userName = self.userLineEdit.text()
        password = self.paswordLineEdit.text()
        userLevel = self.selectTypeUserComboBox.currentText()
        search = db.session.query(User_db).filter_by(userName = userName, password = password, userLevel = userLevel).first()
        print(search)
        if search == None:
            return False
        
        else:
            return search.id

    #Funcion que envia al mainMenu
    def mainMenu(self, userId):
        windows = MainMenuWindows(self, userId)
        windows.show()
