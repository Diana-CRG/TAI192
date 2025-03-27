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
@app.get('/todosusuarios', tags=['Operaciones CRUD 2'])
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


# Endpoint para actualizar usuario
@app.put('/usuario/{id}', tags=['Operaciones CRUD 2'])
def actualizar_usuario(id: int, usuario_actualizado: modelusuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        usuario.name = usuario_actualizado.name
        usuario.age = usuario_actualizado.age
        usuario.email = usuario_actualizado.email
        
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario actualizado", "usuario": jsonable_encoder(usuario)})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"message": "Error al actualizar usuario", "Excepción": str(e)})
    finally:
        db.close()

# Endpoint para eliminar usuario
@app.delete('/usuario/{id}', tags=['Operaciones CRUD 2'])
def eliminar_usuario(id: int):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db.delete(usuario)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado"})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"message": "Error al eliminar usuario", "Excepción": str(e)})
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






