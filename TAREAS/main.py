from fastapi import FastAPI, HTTPException #pocesamiento de respuestas
from typing import Optional

app= FastAPI(
    title='Repaso de FastAPI S192',
    description='Diana Ruiz',
    version='1.0.4'
)

#diccionario o lsita de objetos
tareas=[
    {"id":1, "Titulo":"Repasar los apuntes de virtualización", "Descripcion":"Aprender tipos de virtualización", "Vencimiento":"11-02-25", "Estado":"Completada"},
    {"id":2, "Titulo":"Hacer un proyecto nuevo de FastAPI ", "Descripcion":"Repasar todos los temas vistos hast el momento", "Vencimiento":"20-02-25", "Estado":"Pendiente"},
    {"id":3, "Titulo":"Vocabulario de Ingles", "Descripcion":"Repasar lista de verbos irregulares", "Vencimiento":"23-02-25", "Estado":"Pendiente"},
    {"id":4, "Titulo":"Diagramas UML", "Descripcion":"Hacer los diagramas de secuencia y casos de uso del proyecto", "Vencimiento":"12-02-25", "Estado":"Completada"},
    {"id":5, "Titulo":"Presentacion de interaccion de maquina-computadora", "Descripcion":"Investigar sobre los perifericos y como es su interaccion con la maquina", "Vencimiento":"13-02-25", "Estado":"Completada"},
]


#Endpoint CONSULTAR Tareas
@app.get('/todasTareas', tags=['Repaso Tareas'])
def verTareas():
    return{'Las tareas registradas son':tareas}