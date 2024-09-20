from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from fastapi.params import Depends 
from app.api.eschemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta  
from app.api.models.modelosAPP import Usuario 
from app.database.configuration import sessionLocal, engine

#para que una api funcione debe tener un archivo enrutador
rutas=APIRouter() #Estoe s conocido como ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite conexion hacia la base de datos

def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#programación de cada uno de los seficios que ofrecerá nuestra api 

#y que son los servicio web?, son operaciones en la base de datos, y por lo general se programan basados en un modelo 

#registrando o guardando un usuario en la base de datos 

@rutas.post("/usuarios")#normalmente los endpoints se ponen en "" y con /
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)): 
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            ciudad=datosPeticion.ciudad
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.datosPeticion
        )

@rutas.get("/usuarios")
def buscarUsuario():
    pass

