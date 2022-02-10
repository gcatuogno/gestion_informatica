from PySide2.QtWidgets import QApplication
from controllers.mainMenuWindows import MainMenuWindows
from controllers.loginWindows import LoginWindows
from database import db


if __name__=="__main__":
    #Creamos la base de datos.
    db.Base.metadata.create_all(db.engine)

    #Iniciamos la aplicacion.
    app = QApplication()
    windows = LoginWindows()
    windows.show()

    app.exec_()
