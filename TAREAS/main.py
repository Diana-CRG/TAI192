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
    {"id":2, "Titulo":"Hacer un proyecto nuevo de FastAPI ", "Descripcion":"Repasar todos los temas vistos hasta el momento", "Vencimiento":"20-02-25", "Estado":"Pendiente"},
    {"id":3, "Titulo":"Vocabulario de Ingles", "Descripcion":"Repasar lista de verbos irregulares", "Vencimiento":"23-02-25", "Estado":"Pendiente"},
    {"id":4, "Titulo":"Diagramas UML", "Descripcion":"Hacer los diagramas de secuencia y casos de uso del proyecto", "Vencimiento":"12-02-25", "Estado":"Completada"},
    {"id":5, "Titulo":"Presentacion de interaccion de maquina-computadora", "Descripcion":"Investigar sobre los perifericos y como es su interaccion con la maquina", "Vencimiento":"13-02-25", "Estado":"Completada"},
]


#Endpoint CONSULTAR Tareas
@app.get('/todasTareas', tags=['Mostrar Tareas'])
def verTareas():
    return{'Las tareas registradas son':tareas}

#Endpoint para obtener una tarea por ID
@app.get('/tareas/{id}', tags=['Mostrar Tarea por ID'])
def tareaEsp(id: int):
    for tarea in tareas:
        if tarea["id"] == id: 
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


#Crear una nueva tarea
@app.post("/tareaNueva", tags=["Agregar Tarea Nueva"])
def crear_tarea(nueva_tarea: dict):
    for tarea in tareas:
        if tarea["id"] == nueva_tarea["id"]:
            raise HTTPException(status_code=400, detail="ID ya existe")
    
    tareas.append(nueva_tarea)
    return {"mensaje": "Tarea creada correctamente", "tarea": nueva_tarea}


#Actualizar una tarea existente
@app.put("/tareaActualizada/{id}", tags=["Modificar Tarea Existente"])
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index].update(tarea_actualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#Eliminar una tarea
@app.delete("/tareaEliminada/{id}", tags=["Eliminar Tareas"])
def eliminarTarea(id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            del tareas[index]
            return {"mensaje": "Tarea eliminada correctamente"}
    
    raise HTTPException(status_code=404, detail="Tarea no encontrada")