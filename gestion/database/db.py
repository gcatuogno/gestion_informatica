from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

#Motor que permite manejar la coneccion con la base de datos

engine = create_engine('sqlite:///database/suministros.db', connect_args={'check_same_thread': False})

#Creamos una Session que es la encargada de enviar la informacion.
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()


