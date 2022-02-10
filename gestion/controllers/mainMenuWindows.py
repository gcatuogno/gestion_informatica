from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.mainWindows import MainForm
from controllers.gestionWindows import GestionDeProductosWindows
from controllers.gestionProveedoresWindows import GestionDeProveedoresWindows
from controllers.userPanelWindows import UserPanelWindows
from database import db
from database.models import User_db

class MainMenuWindows(QWidget, MainForm):
    def __init__(self,  parent=None, userId = None):
        # Definimos el Id del usuario.
        self.userId = userId

        # Heredamos de la clase padre
        super().__init__(parent)

        # Configramos la ventana
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Identificamos el usuario.
        user = self.user(userId)
        userLevel = user.userLevel

        #Aplicamos condicionales a los botones
        if userLevel == "Acceso a Productos":
            self.productButton.clicked.connect(self.gestionProductos)
            self.supplyButton.setDisabled(True)
            self.userButton.setDisabled(True)

        if userLevel == "Acceso a Proveedores":
            self.productButton.setDisabled(True)
            self.supplyButton.clicked.connect(self.gestionProveedores)
            self.userButton.setDisabled(True)

        if userLevel == "Acceso a Productos + Proveedores":
            self.productButton.clicked.connect(self.gestionProductos)
            self.supplyButton.clicked.connect(self.gestionProveedores)
            self.userButton.setDisabled(True)

        if userLevel == "Administrador":
            self.productButton.clicked.connect(self.gestionProductos)
            self.supplyButton.clicked.connect(self.gestionProveedores)
            self.userButton.clicked.connect(self.gestionUsuarios)
        
    # Funcion que abre la ventana productos    
    def gestionProductos(self):
        windows = GestionDeProductosWindows(self, self.userId)
        windows.show()
        
    # Funcion que abre la ventana proveedores 
    def gestionProveedores(self):
        windows = GestionDeProveedoresWindows(self, self.userId)
        windows.show()
        
    # Funcion que abre la ventana gestion de usuarios 
    def gestionUsuarios(self):
        windows = UserPanelWindows(self)
        windows.show()

    # Funcion que busca al usuario
    def user(self, userId):
        user = db.session.query(User_db).filter_by(id = userId).first()
        return user

