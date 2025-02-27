from fastapi import FastAPI, HTTPException #pocesamiento de respuestas
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelusuario, modeloAuth
from genToken import createToken

app= FastAPI(
    title='Mi primer API S192',
    description='Diana Ruiz',
    version='1.0.1'
)



#diccionario o lsita de objetos
usuarios=[
    {"id":1, "nombre":"Diana", "edad":23, "correo":"diana123@gmail.com"},
    {"id":2, "nombre":"Juan", "edad":20,"correo":"juanrd4@gmail.com"},
    {"id":3, "nombre":"Manuel", "edad":32,"correo":"manu567@gmail.com"},
    {"id":4, "nombre":"Valeria", "edad":30,"correo":"valejim34@gmail.com"}
]
#Endpoint home

@app.get('/', tags=['Hola Mundo'])
def home():
    return{'Hello':'World FastAPI'}


@app.post('/Auth', tags=['Autentificación'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == 'diana@example.com' and autorizacion.passw =='12345':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(token)
    else:
        return {'Aviso':"Usuario sin autentificacion"}






#Endpoint CONSULTA TODOS
@app.get('/todosusuarios', response_model=List[modelusuario], tags=['Operaciones CRUD'])
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

#Endpoint Actualizar
@app.put('/usuarios/{id}', response_model=modelusuario, tags=['Operaciones CRUD'])
def actualizarUsuarios(id:int, usuarioActualizado:modelusuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
           usuarios[index]=usuarioActualizado.model_dump()
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