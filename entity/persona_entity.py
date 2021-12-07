import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, String
#from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Persona(db.Base,SerializerMixin):
    __tablename__ = 'persona'
    id= Column(String(256), name="id", primary_key=True, default=generate_uuid) 
    nombre = Column(String(256), nullable=True)
    telefono = Column(String(256), nullable=True)
    email = Column(String(256), nullable=True)
    

