from fastapi import FastAPI
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


@app.get('/promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 6.1

#Obligatorio
@app.get('/usuario/{id}', tags=['parametro obligatorio'])
def consultaUsuario(id:int):
    #conectamos a la BD
    #consultamos
    return {'Se encontro usuario':id}


#Endpoint con parametro Opcional
@app.get('/usuario/', tags=['Parametro Opcional'])
def consultaUsuario2(id: Optional[int]=None):
    #conectamos a la BD
    #consultamos
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"Mensaje": "Usuario encontrado", "Usuario":usu}
            
           
        return {"Mensaje":f"Usuario NO encontrado con el id:{id}"} 
    else:

        return {"Mensaje":'No se proporciono un id'}



#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}