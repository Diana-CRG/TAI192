from fastapi import FastAPI, HTTPException #pocesamiento de respuestas
from typing import Optional

app= FastAPI(
    title='Mi primer API S192',
    description='Diana Ruiz',
    version='1.0.1'
)

#diccionario o lsita de objetos
usuarios=[
    {"id":1, "nombre":"Diana", "edad":23},
    {"id":2, "nombre":"Juan", "edad":20},
    {"id":3, "nombre":"Manuel", "edad":32},
    {"id":4, "nombre":"Valeria", "edad":30}
]
#Endpoint home

@app.get('/', tags=['Hola Mundo'])
def home():
    return{'Hello':'World FastAPI'}

#Endpoint CONSULTA TODOS
@app.get('/todosusuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    return{'Los usuarios registrados son':usuarios}

#Endpoint Agregar Nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="id ya existe")
    usuarios.append(usuario)

    return usuario

#Endpoint Actualizar
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def actualizarUsuarios(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
           usuarios[index].update(usuarioActualizado)
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