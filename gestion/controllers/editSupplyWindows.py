from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.editSupplyWindows import EditSupplyForm
from database.supply import selectSupplierById, updateSupplier

class EditSupplyWindows(QWidget, EditSupplyForm):

    #Constructor
    def __init__(self, parent=None, supplierID = None):
        # Declaramos la variable con el ID del Proveedor.
        self.supplierId = supplierID

        #Heredamos de la clase padre.
        super().__init__(parent)

        # Ajustamos la ventana.
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Cargamos los datos
        self.populateInputs()

        # Funcion de botones.
        self.saveButton.clicked.connect(self.addSupply)
        self.cancelButton.clicked.connect(self.close)

    # Funcion para verificar los Inputs
    def checkInput(self):

        #Obtenemos los valores escritos por el usuario.
        name = self.nameLineEdit.text()
        cif = self.cifLineEdit.text()
        adress = self.locationLineEdit.text()
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
        self.locationLineEdit.clear()
        self.phoneLineEdit.clear()

    # Funcion que llena los campos de los input con los datos del proveedor seleccionado.
    def populateInputs(self):
        data = selectSupplierById(self.supplierId)
        
        # Rellenamos los input
        self.nameLineEdit.setText(data.name)
        self.cifLineEdit.setText(data.cif)
        self.locationLineEdit.setText(data.adress)
        self.phoneLineEdit.setText(str(data.phone))
    
    # Funcion que añade el nuevo proveedor.
    def addSupply(self):
        #Obtenemos los valores escritos por el usuario.
        name = self.nameLineEdit.text()
        cif = self.cifLineEdit.text()
        adress = self.locationLineEdit.text()
        phone = self.phoneLineEdit.text()

        if self.checkInput():
            data = (name, cif, adress, phone)

            if updateSupplier(self.supplierId, data):
                self.cleanInput()
                self.close()
    