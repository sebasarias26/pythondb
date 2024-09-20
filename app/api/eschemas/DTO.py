from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPetición(BaseModel):
    nombre:str 
    edad:int
    telefono:str
    correo:str
    contraseña:str
    fechaRegistro:date
    ciudad:str
    class Config:
        orm_mode=True

class UsuarioDTORespuesta():
    id:int
    nombre:str
    telefono:str
    ciudad:str
    class Config:
        orm_mode=True

class gastoDTOPetición():
    monto:int
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class gastoDTORespuesta():
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class CategoriaDTOPetición():
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta():
    nombreCategoria:str
    fotoIcono:str
    class Config:
        orm_mode=True

class MetodoPagoDTOPetición():
    nombre:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class MetodoPagoDTORespuesta():
    nombre:str
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class facturadeoDTOPetición():
    numeroTransaccion:int
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

class facturadeoDTORespuesta():
    valor:int
    descripcion:str
    class Config:
        orm_mode=True

