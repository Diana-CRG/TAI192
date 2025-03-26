from fastapi import FastAPI, HTTPException, Depends #pocesamiento de respuestas
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelusuario, modeloAuth
from genToken import createToken
from middleware import BearerJWT

from DB.conexion import Session, engine, Base
from models.modelsDB import User

from fastapi.encoders import jsonable_encoder

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
@app.get('/todosusuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    db=Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as e:
         return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                     "Excepción":str(e) })

    finally:
        db.close()



#Endpoint buscar por id
@app.get('/usuario/{id}', tags=['Operaciones CRUD 2'])
def buscarUno(id:int):
    db=Session()
    try:
        consultauno=db.query(User).filter(User.id == id).first()
        if not consultauno:

           return JSONResponse(status_code=404, content= {"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content= jsonable_encoder(consultauno))
    
    except Exception as e:
         return JSONResponse(status_code=500,
                            content={"message":"Error al consultar",
                                     "Excepción":str(e) })

    finally:
        db.close()



#Endpoint Agregar Nuevos
@app.post('/usuario/', response_model=modelusuario,tags=['Operaciones CRUD'])
def agregarUsuarios(usuario:modelusuario):
   db = Session()
   try:
       db.add(User(**usuario.model_dump()))
       db.commit()
       return JSONResponse(status_code=201,
                            content={"message":"Usuario Guardado",
                                     "usuario":usuario.model_dump() })
   except Exception as e:
       db.rollback()
       return JSONResponse(status_code=500,
                            content={"message":"Error al guardar Usuario",
                                     "Excepción":str(e) })
   
   finally:
       db.close()






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