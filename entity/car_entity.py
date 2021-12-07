from sqlalchemy.sql.expression import column
import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, String, Integer, ForeignKey
#from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Car(db.Base,SerializerMixin):
    __tablename__ = 'car'
    id= Column(String(256), name="id", primary_key=True, default=generate_uuid) 
    color = Column(String(20), nullable=True)
    placa = Column(Integer, nullable=True)
    fabricante = Column(String(50), nullable=True)
    modelo = Column(String(30), nullable=True)
    kilometraje = Column(Integer, nullable=True)
    
    persona_id = Column(String(256), ForeignKey('persona.id'))

