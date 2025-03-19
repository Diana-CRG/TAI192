from fastapi import FastAPI, HTTPException, Depends #pocesamiento de respuestas
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelusuario, modeloAuth
from genToken import createToken
from middleware import BearerJWT

from DB.conexion import Session, engine, Base
from models.modelsDB import User

app= FastAPI(
    title='Mi primer API S192',
    description='Diana Ruiz',
    version='1.0.1'
)

Base.metadata.create_all(bind=engine)



#Endpoint home

@app.get('/', tags=['Hola Mundo'])
def home():
    return{'Hello':'World FastAPI'}


@app.post('/Auth', tags=['Autentificación'])
def login(autorizacion: modeloAuth):
    if autorizacion.email == 'diana@example.com' and autorizacion.passw == '12345678':  # Mínimo 8 caracteres
        token: str = createToken(autorizacion.model_dump())
        return JSONResponse(content={"token": token})
    else:
        raise HTTPException(status_code=401, detail="Usuario sin autenticación")





#Endpoint CONSULTA TODOS
@app.get('/todosusuarios', dependencies=[Depends(BearerJWT())], response_model=List[modelusuario], tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios

#Endpoint Agregar Nuevos
@app.post('/usuario/', response_model=modelusuario,tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:modelusuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="id ya existe")
    usuarios.append(usuario)

    return usuario

@app.put('/usuarios/{id}', response_model=modelusuario, tags=['Operaciones CRUD'])
def actualizarUsuarios(id: int, usuarioActualizado: modelusuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")


#Endpoint Eliminar
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminarUsuarios(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
           del usuarios[index]
           return {'detail':'Usuario eliminado'}
    raise HTTPException(status_code=400, detail="El usuario no existe")