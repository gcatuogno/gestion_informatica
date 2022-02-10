from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.newSupplyWindows import NewSupplyForm
from database.supply import addSupplier

class NewSupplyWindows(QWidget, NewSupplyForm):

    def __init__(self, parent=None):
        # Heredamos de la clase padre.
        super().__init__(parent)

        # Configuramos la ventana
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Asignamos Funciones a los botones
        self.saveButton.clicked.connect(self.addSupply)
        self.cancelButton.clicked.connect(self.close)

    #Funcion para verificar los Inputs
    def checkInput(self):

        #Obtenemos los valores escritos por el usuario.
        name = self.nameLineEdit.text()
        cif = self.cifLineEdit.text()
        adress = self.adressLineEdit.text()
        phone = self.phoneLineEdit.text()
    
        
        errosCount = 0

        # Verificamos que todos los campos sean validos
        if name == "":
            print("El campo Razon Social es obligatorio")
            errosCount += 1

        if cif == "":
            print("El campo Cif es obligatorio")
            errosCount += 1

        if adress == "":
            print("El campo Direccion es obligatorio")
            errosCount += 1

        if phone == "":
            print("El campo Telefono es obligatorio")
            errosCount += 1
        
        if errosCount == 0:
            return True

    # Funcion para borrar los input
    def cleanInput(self):

        self.nameLineEdit.clear()
        self.cifLineEdit.clear()
        self.adressLineEdit.clear()
        self.phoneLineEdit.clear()

    # Funcion para añadir Proveedores
    def addSupply(self):

        #Obtenemos los valores escritos por el usuario.
        name = self.nameLineEdit.text()
        cif = self.cifLineEdit.text()
        adress = self.adressLineEdit.text()
        phone = self.phoneLineEdit.text()
        
        if self.checkInput():
            data = (name, cif, adress, phone)

            if addSupplier(data):
                self.cleanInput()
    

