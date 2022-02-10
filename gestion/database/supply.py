from database.models import Supply_db
from database import db 


# Funcion para añadir un proveedor.
def addSupplier(data):
    # Guardamos los datos del nuevo producto y los enviamos la base de datos
    supplier = Supply_db(name= data[0], cif= data[1], adress = data[2], phone= data[3])
    db.session.add(supplier)
    db.session.commit()
    print("Proveedor {} añadido correctamente". format(supplier.name))
    return True

#Funcion para actualizar un proveedor.
def updateSupplier(id, data):
    # Obtenemos el producto a editar
    supplierEdit = db.session.query(Supply_db).filter_by(id = id).first()

    # Modificamos los datos.
    supplierEdit.name = data[0]
    supplierEdit.cif = data[1]
    supplierEdit.adress = data[2]
    supplierEdit.phone = data[3]
    
    # Enviamos la informacion.
    db.session.commit()
    print("El Proveedor fue editado con exito")
    return True

# Funcion para eliminar un proveedor.
def deleteSupplier(id):
    # Borramos el Producto.
    db.session.query(Supply_db).filter_by(id = id).delete()
    db.session.commit()

    return True

# Funcion para seleccionar todos los proveedores
def selectAllSupplier():
    supplier = db.session.query(Supply_db).all()
    listsupplier = []

    for i in supplier:
        supply = [i.id, i.name, i.cif, i.adress, i.phone]
        listsupplier.append(supply)

    return listsupplier

# Funcion para buscar un proveedor por ID.
def selectSupplierById(id):
    supplier = db.session.query(Supply_db).filter_by(id=id).first()     
    return supplier

# Funcion para buscar un Proveedor por nombre
def selectSupplierByName(name):
    name = "%{}%".format(name)
    supplier = db.session.query(Supply_db).filter(Supply_db.name.like(name)).all()
    listsupplier = []

    for i in supplier:
        supply = [i.id, i.name, i.cif, i.adress, i.phone]
        listsupplier.append(supply)

    return listsupplier

# Funcion para buscar un Proveedor por cif
def selectSupplierByCif(cif):
    cif = "%{}%".format(cif)
    supplier = db.session.query(Supply_db).filter(Supply_db.cif.like(cif)).all()
    listsupplier = []

    for i in supplier:
        supply = [i.id, i.name, i.cif, i.adress, i.phone]
        listsupplier.append(supply)

    return listsupplier
