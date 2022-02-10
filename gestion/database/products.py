from sqlalchemy.sql.expression import desc
from database.models import Product_db
from database import db 

# Funcion para añadir un producto.
def addProduct(data):
    # Guardamos los datos del nuevo producto y los enviamos la base de datos
    product = Product_db(description = data[0], code = data[1], location = data[2], qty = data[3], minQty= data[4], buyPrice= data[5], sellPrice= data[6], supply= data[7])
    db.session.add(product)
    db.session.commit()
    print("Producto {} añadido correctamente". format(product.description))
    return True

# Funcion que actiliza un producto
def updateProduct(id, data):
    # Obtenemos el producto a editar
    productEdit = db.session.query(Product_db).filter_by(id = id).first()

    # Modificamos los datos.
    productEdit.description = data[0]
    productEdit.code = data[1]
    productEdit.location = data[2]
    productEdit.qty = data[3]
    productEdit.minQty = data[4]
    productEdit.buyPrice = data[5]
    productEdit.sellPrice = data[6]
    productEdit.supply= data[7]

    # Enviamos la informacion.
    db.session.commit()
    print("El Producto fue editado con exito")
    return True

# Funcion que borra un producto.
def deleteProduct(id):
    # Borramos el Producto.
    db.session.query(Product_db).filter_by(id = id).delete()
    db.session.commit()

    return True

# Funcion para seleccionar todos los productos
def selectAllProduct():

    products = db.session.query(Product_db).all()
    listproduct = []

    for i in products:
        product = [i.id, i.description, i.code, i.location, i.qty, i.minQty, i.buyPrice, i.sellPrice, i.supply]

        listproduct.append(product)

    return listproduct

# Funcion para buscar un producto por ID.
def selectProductById(id):
    products = db.session.query(Product_db).filter_by(id = id).first()
    return products

# Buscar un producto por descripcion.
def selectProductByDescription(description):

    description = "%{}%".format(description)
    products = db.session.query(Product_db).filter(Product_db.description.like(description)).all()
    listproduct = []

    for i in products:
        product = [i.id, i.description, i.code, i.location, i.buyPrice, i.sellPrice, i.qty, i.supply]
        listproduct.append(product)

    return listproduct

# Buscar un producto por codigo.
def selectProductByCode(code):

    code = "%{}%".format(code)
    products = db.session.query(Product_db).filter(Product_db.code.like(code)).all()
    listproduct = []

    for i in products:
        product = [i.id, i.description, i.code, i.location, i.buyPrice, i.sellPrice, i.qty, i.supply]
        listproduct.append(product)

    return listproduct

# Buscar un producto por ubicacion.
def selectProductBylocation(location):

    location = "%{}%".format(location)
    products = db.session.query(Product_db).filter(Product_db.location.like(location)).all()
    listproduct = []

    for i in products:
        product = [i.id, i.description, i.code, i.location, i.buyPrice, i.sellPrice, i.qty, i.supply]
        listproduct.append(product)

    return listproduct

# Buscar un producto por proveedor.
def selectProductBySupplier(supplier):

    supplier = "%{}%".format(supplier)
    products = db.session.query(Product_db).filter(Product_db.supplier.like(supplier)).all()
    listproduct = []

    for i in products:
        product = [i.id, i.description, i.code, i.location, i.buyPrice, i.sellPrice, i.qty, i.supply]
        listproduct.append(product)

    return listproduct

# Verifica los productos con bajo stock.
def checkMin(data):

    for i in data:
         if int(i[5]) >= int(i[4]):
                return False

# Crea una lista con los productos bajos de stock.
def minRequest(data):

    lowStock = []
    
    for i in data:

        minQty = int(i[5])
        stock = int(i[4])

        if minQty >= stock:
            productID = i[0]
            description = i[1]
            code = i[2]
            qtyRequest = minQty - stock
            supplier = i[8]
            request = [productID, description, code, qtyRequest, supplier]
            lowStock.append(request)

    print("Lista realizada con exito")
    return lowStock

