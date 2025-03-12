from fastapi import FastAPI
from fastapi import FastAPI, HTTPException #pocesamiento de respuestas
from typing import Optional
from pydantic import BaseModel
from models import modelConductor

app= FastAPI()
app= FastAPI(
    title='Examne 2do Parcial',
    description='Diana Ruiz',
    version='2.0.1'
)

#Modelo de Validaciones
class modelConductor(BaseModel):
    nombre:str
    tipoLicencia:str
    NLicencia:int

#diccionario o lsita de objetos
conductores=[
    {"Nombre":"Numero1", "tipoLicencia":"A", "NLicencia": 123456789129},
    {"nombre":"Numero2", "tipoLicencia":"B", "NLicencia": 456123445456},
    {"nombre":"NUmero3", "tipoLicencia":"C", "NLicencia": 135456932468},
    {"nombre":"Numero4", "tipoLicencia":"D", "NLicencia": 257357098765}
]

#Consultar todos los Conectores
@app.get('/todosConductores', tags=['Todos los Conductores'])
def leerConductores():
    return{'Los usuarios registrados son':conductores}


#Agregar Conductor
@app.post('/conductor/', tags=['Añadir Conductor'])
def agregarConductor(conductor:dict):
    for cdr in conductores:
        if cdr["NLicencia"] == conductor.get("NLicencia"):
            raise HTTPException(status_code=400, detail="id ya existe")
    conductores.append(conductor)
    return conductor


#Editar conductor
@app.put('/conductor/{NLicencia}', tags=['Editar Conducor'])
def actualizarConductor(licencia:int, conductorActualizado:dict):
    for index, usr in enumerate(conductores):
        if usr["NLicencia"] == licencia:
           conductores[index].update(conductorActualizado)
           return conductores[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")