from database import db
from sqlalchemy import Column, Integer, String

# Clase Producto.
class Product_db(db.Base):
    __tablename__ ='products'
    id = Column(Integer, primary_key= True, nullable= False)
    description = Column (String, nullable= False)
    code = Column (String, nullable= False)
    location = Column(String, nullable= False)
    qty = Column(Integer, nullable= False)
    minQty = Column(Integer, nullable= False)
    buyPrice = Column(Integer, nullable= False)
    sellPrice = Column(Integer, nullable= False)
    supply = Column(Integer, nullable= False)

    def __init__(self, description, code, location, buyPrice, sellPrice, qty, minQty, supply):
        self.description = description
        self.code = code
        self.location = location
        self.buyPrice = buyPrice
        self.sellPrice = sellPrice
        self.qty = qty
        self.minQty = minQty
        self.supply = supply

    def __str__(self):
        return 'ID {} descripcion {} codigo {}'.format(self.id, self.description, self.code)

# Clase Proveedor.
class Supply_db(db.Base):
    __tablename__ ='supply'
    id = Column(Integer, primary_key= True, nullable= False)
    name = Column(String, nullable= False)
    cif = Column(String, nullable= False)
    adress = Column(String, nullable= False)
    phone = Column (Integer, nullable= False)

    def __init__(self, name, cif, adress, phone):
        self.name = name
        self.cif = cif
        self.adress = adress
        self.phone = phone

    def __str__(self):
        return 'ID {} Razon Social {} CIF {}'. format(self.id, self.name, self.cif)

#Clase Usuario.
class User_db(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True, nullable= True)
    userName = Column(String, nullable= False)
    password = Column(String, nullable= False)
    userLevel = Column(String, nullable= False)

    def __init__(self, userName, password, userLevel):
        self.userName = userName
        self.password = password
        self.userLevel = userLevel

    def __str__(self):
        return 'ID {} Nombre de Usuario {} Nivel de Acceso {}'.format(self.id, self.userName, self.userLevel)
