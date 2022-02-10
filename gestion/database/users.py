from database.models import User_db
from database import db 

# Funcion para añadir un usuario.
def addUser(data):
    # Guardamos los datos del nuevo producto y los enviamos la base de datos
    user = User_db(userName= data[0], password= data[1], userLevel= data[2])
    db.session.add(user)
    db.session.commit()
    #print("Usuario {} añadido correctamente". format(user.userName))
    return True

#Funcion para actualizar un usuario.
def updateUser(id, data):
    # Obtenemos el producto a editar
    userEdit = db.session.query(User_db).filter_by(id = id).first()

    # Modificamos los datos.
    userEdit.name = data[0]
    userEdit.password = data[1]
    userEdit.userLevel = data[2]
    
    # Enviamos la informacion.
    db.session.commit()
    #print("El Usuario fue editado con exito")
    return True

# Funcion para borrar un usuario.
def deleteUser(id):
    # Borramos el Producto.
    db.session.query(User_db).filter_by(id = id).delete()
    db.session.commit()
    return True

# Funcion para seleccionar todos los usuarios
def selectAllUser():
    user = db.session.query(User_db).all()
    listUser = []

    for i in user:
        user = [i.id, i.userName, i.password, i.userLevel]
        listUser.append(user)

    return listUser

# Funcion para buscar un usuario por ID.
def selectUserById(id):
    user = db.session.query(User_db).filter_by(id=id).first()     
    return user

# Funcion para buscar un Usuario por nombre
def selectUserByName(name):
    name = "%{}%".format(name)
    user = db.session.query(User_db).filter(User_db.name.like(name)).all()
    listUser = []

    for i in user:
        supply = [i.id, i.name, i.cif, i.adress, i.phone]
        listUser.append(supply)

    return listUser