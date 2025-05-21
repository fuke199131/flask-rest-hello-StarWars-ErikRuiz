from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class TipoFavoritoEnum(enum.Enum):
    personaje = "personaje"
    planeta = "planeta"

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    correo = Column(String(120), unique=True, nullable=False)
    contraseña = Column(String(80), nullable=False)
    nombre = Column(String(120))
    apellido = Column(String(120))
    fecha_suscripcion = Column(DateTime)

    favoritos = relationship("Favorito", back_populates="usuario")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    genero = Column(String(50))
    año_nacimiento = Column(String(50))
    color_ojos = Column(String(50))

    favoritos = relationship("Favorito", back_populates="personaje")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    clima = Column(String(100))
    terreno = Column(String(100))
    poblacion = Column(String(100))

    favoritos = relationship("Favorito", back_populates="planeta")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    tipo = Column(Enum(TipoFavoritoEnum), nullable=False)

    usuario = relationship("Usuario", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")